# Python Project Setup Guide

This guide will help you set up and run this Python project using a virtual environment.

## Prerequisites

- Python 3.x installed on your system
- pip (Python package installer)

## Setup Instructions

### 1. Create Virtual Environment

For Windows:
```
python -m venv .venv
```

For macOS/Linux:
```
python3 -m venv .venv
```

### 2. Activate Virtual Environment

For Windows (Command Prompt):
```
.venv\Scripts\activate
```

For Windows (PowerShell):
```
.\.venv\Scripts\Activate.ps1
```

For macOS/Linux:
```
source .venv/bin/activate
```

### 3. Install Requirements

Once the virtual environment is activated (you'll see (.venv) at the beginning of your command line), install the required packages:
```
pip install -r requirements.txt
```

### 4. Set PYTHONPATH

Before running any scripts, you need to set the PYTHONPATH environment variable in your terminal session:

```bash
export PYTHONPATH=./src:$PYTHONPATH
```

This command needs to be executed in each new terminal session where you want to run the project's Python scripts.

### 5. Verify Installation

To see installed packages:
```
pip list
```

## Additional Notes

- Make sure Python is installed on your system before starting
- The virtual environment (.venv) should be created in the project root
- You'll see (.venv) at the start of your command line when the virtual environment is active
- To deactivate the virtual environment, simply type `deactivate` in the terminal

## Project Structure


## Usage

To run scripts in this project, make sure:
1. Your virtual environment is activated
2. You have set the PYTHONPATH (run the export command above)
3. You are in the project root directory

Example command:
```bash
python3 01-module/llm_call.py
```

## License

MIT License

This software is free to use, modify and share.

Copyright (c) 2024
