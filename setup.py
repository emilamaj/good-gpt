from setuptools import setup, find_packages

setup(
    name='good-gpt',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gg=good_gpt.good_gpt:main',
        ],
    },
    python_requires='>=3.6',
    install_requires=[
        'requests',  # Add any additional packages you need
    ],
    scripts=['scripts/gg'],  # Only necessary if you need custom scripting outside Python's entry_points
)
