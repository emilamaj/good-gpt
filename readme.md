# gg good-gpt
Bake AI into your command-line terminal: describe a command like `Delete all video files in current folder` and the assistant will run `del *.mp4 *.mov *.avi *.mkv`

## Installation
This tool is built using python. It has been tested on python 3.10 on both windows and linux.
To install Python, visit [python.org](https://www.python.org/downloads/)

After installing python, you can install the `good-gpt` package using pip
```bash
pip install good-gpt
```
or if you have multiple python installations:
```bash
pip3 install good-gpt
```

This will install the package, but you may not yet have the `gg` command available in your terminal. For that, you need to add the installation location to your PATH environment variable.
The installation location by default is `%APPDATA%\Python\Python3XX\Scripts\Lib\site-packages\good_gpt` on Windows and `$HOME/.local/lib/python3.XX/site-packages/good_gpt/` on linux.

If PATH is not correctly set, you need to run the `post_install.py` script to add the installation location to your PATH.

For that, find the location of the `post_install.py` script using the following command:
```bash
pip show good-gpt
```
and then navigate to the folder pointed by the `Location` field, and then navigate to the `good_gpt` folder, where you will find the `post_install.py` script.

Then run the script using the following command:
```bash
python post_install.py
```
or if you have multiple python installations:
```bash
python3 post_install.py
```
With the directory added to your PATH, you now simply need to restart your terminal to use the `gg` command. You can also run the following command to refresh the PATH environment variable, depending on your terminal:
```bash
source ~/.bashrc
```
or
```bash
source ~/.zshrc
```
Windows does not require a refresh, but you may need to close and reopen the terminal.

## Usage
On the first run, you will be asked to provide your OpenAI API key. You can get the API key by signing up at [openai.com](https://beta.openai.com/signup/)

Simply paste the API key when prompted and press enter. The API key will be stored in openai_api_key.env in the same folder as the gg command.

Here is an example on Windows 10:
```bash
C:\Users\user> gg current external ip address, only ipv4
Do you want to execute this suggested command for win32? [y/n]
--> curl ifconfig.me/ip -4
<Enter>
72.88.25.127
```

Here is an example on Ubuntu 20.04:
```bash
user@ubuntu:~$ gg current external ip address, only ipv4
Do you want to execute this suggested command for linux? [y/n]
--> dig +short myip.opendns.com @resolver1.opendns.com -4
yes
72.88.25.127
```
