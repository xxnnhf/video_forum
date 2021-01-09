# A simple Python script for extracting metadata from video files and zip them

## ![Alt Text](https://i.imgur.com/1zAgN36.gif)

## Requirements:

### How to Install the Requirements?

**Required Python version:** [Python 3.8+](https://www.python.org/downloads/)

**You must have pip installed. Please look up how to install them in your OS.**

**How to install python pip** - [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)

Download a release of this project or clone the repository then navigate to the folder where you placed the files on. Type `pip install -r requirements.txt` to get all the requirements installed in one go.

```
pip install -r requirements.txt
```

---

## Instructions

1 . Open the file `config.ini` in Notepad to change the folder directory

Examples:

- Windows

  ```
  [Section1]
  folderPath = C:/Videos/
  ```

- WSL

  ```
  [Section1]
  folderPath = /mnt/c/videos/
  ```

- Linux

  ```
  [Section1]
  folderPath = /home/
  ```

---

## How to run

- Windows

  - You can double-click as usual to run the script.

    or

  - Step 1 - Go to the folder directory that contains the Python script and press the SHIFT + Right-Click.

    Step 2 - Choose the _'Open PowerShell window here / Open CommandPrompt here'_ option.

    Step 3 - Type the following code and hit the enter key.

    ```
    python main.py
    ```

    or

    ```
    python3 main.py
    ```

- WSL and Linux

  ```
  python main.py
  ```

  or

  ```
  python3 main.py
  ```

---
