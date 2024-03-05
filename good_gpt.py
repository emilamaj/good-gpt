import sys
import os
import requests
import json

# Read OpenAI API key from file. First line of file should contain the raw API key.
with open("./openai_api_key.env", "r") as f:
    userAccessToken = f.readlines()[0].strip()


def get_response(
    message_thread,
    maxTokens=256,
    temperature=1.0,
    frequencyPenalty=0,
    presencePenalty=0,
):
    """
    Function to get a response from the OpenAI API, given a message thread.

    Args:
    message_thread (list of dict): A list of messages, each containing a role and a content field.
    maxTokens (int): The maximum number of tokens to generate.
    temperature (float): The sampling temperature.
    frequencyPenalty (float): Proportional penalty to the appearance of already generated tokens.
    presencePenalty (float): Flat penalty to the appearance of already generated tokens.

    Returns:
    str: The response from the OpenAI API.
    """
    # If the message thread is empty, return an empty string
    if len(message_thread) == 0:
        raise ValueError("Message thread is empty")

    # If the message thread is not empty, make a request to the OpenAI API
    url = "https://api.openai.com/v1/chat/completions"
    model = "gpt-3.5-turbo"

    # Make the request with timeout
    response = requests.post(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {userAccessToken}",
        },
        data=json.dumps(
            {
                "model": model,
                "messages": message_thread,
                "max_tokens": maxTokens,
                "temperature": temperature,
                "frequency_penalty": frequencyPenalty,
                "presence_penalty": presencePenalty,
            }
        ),
        timeout=10,  # Set the timeout value in seconds
    )

    # Return the response
    return response.json()["choices"][0]["message"]["content"]


def thread_add_message(message_content, thread=None):
    """
    Function to append a message to a message thread.
    Message thread is a list of dict, containing some messages assigned to different roles.
    The role of the new message is inferred from the last message in the thread.
    If the thread is empty, the role is assumed to be "system".

    Args:
    message_content (str): The content of the message to be added.
    thread (list of dict): The message thread to which the message should be added.

    Returns:
    list of dict: The updated message thread.
    """
    if thread is None:
        thread = [{"role": "system", "content": message_content}]
    else:
        if thread[-1]["role"] == "system":
            thread.append({"role": "user", "content": message_content})
        elif thread[-1]["role"] == "user":
            thread.append({"role": "assistant", "content": message_content})
        elif thread[-1]["role"] == "assistant":
            thread.append({"role": "user", "content": message_content})
        else:
            raise ValueError("Invalid role in message thread")
    return thread

def main():
    """
    Main function to run the shell command assistant.
    """
    # Process the input command
    user_command = " ".join(sys.argv[1:])
    if user_command == "":
        print("No command provided to good-gpt. Returning.")
        return

    # Send the command to the assistant
    system_message = "You are a shell command assistant. A desired command is specified using natural language. You provide directly a corresponding single-line command, raw, without any additional explanation."
    system_message += "# USER_SYSTEM_PLATFORM: " + sys.platform
    thread = thread_add_message(system_message)
    thread = thread_add_message(user_command, thread)
    suggested_command = get_response(thread)

    print(f"Suggested Command:\n{suggested_command}\n")
    print("Do you want to execute this command? [Y/n]")

    choice = input().lower()
    if choice in ['y', 'yes', 'ok', 'good', '']:
        # Execute the command for Unix-like systems
        print(f"Executing on platform: {sys.platform}")
        if sys.platform in ["linux", "darwin"]:
            os.system(f"{suggested_command}")
        # For Windows, you might need to adjust commands or use a translation layer
        elif sys.platform == "win32":
            os.system(f"{suggested_command}")
        else:
            print("Unsupported OS.")
    else:
        print("Command not executed.")

if __name__ == "__main__":
    main()
