# 🐍 Python Starter Environment

A lightweight Python project starter kit for learning and experimentation.

Includes:
- Python formatting with **Black**
- Debugging via VS Code’s **Debug Console**
- Cleaner project defaults
- Optional **Jupyter Notebook** support
- Easy virtual environment setup via `make`

---

## 🚀 Quick Setup

1. **Clone this repo**

   ```bash
   git clone https://github.com/manwithacat/python-starter-env.git
   cd python-starter-env

1. **Create a virtual environment and install dependencies**

    ```bash
    make setup
    ```
This will:
- Create a local .venv folder
- Install packages listed in requirements.txt

1. **Activate your environment**
   ```bash
   source .venv/bin/activate
   ```
(On Windows PowerShell: .venv\Scripts\Activate.ps1)

## 🐞 Debugging in VS Code (Beginner-Friendly)

This project is configured to give you a **clean and simple debugging experience** using VS Code's **Debug Console** instead of the Terminal.

### ✅ What happens when you press `F5`

- VS Code runs your current Python file
- Output appears in the **Debug Console**
- No flashing terminal, no extra launch noise
- Errors and `print()` statements are easy to see
- You can still set breakpoints later when you're ready

### ✅ Why this matters for beginners

- Keeps the focus on your code, not VS Code internals
- Avoids confusing messages from `debugpy` or the terminal
- Provides a stable, readable output area while you learn

---

## ⚙️ How It Works (Under the Hood)

- We use a `launch.json` config that tells VS Code:
  - Run the current file
  - Use the internal debug console
  - Ignore unrelated Python internals (`justMyCode: true`)

You can find this setup in:   
`.vscode/launch.json`  
`.vscode/settings.json`  

## 🧪 Want to run your code without debugging?

You can always right-click a `.py` file and choose:

`Run Python File in Terminal`

This is helpful if you want input/output like a traditional console script.