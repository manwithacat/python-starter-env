# 🐍 Python Starter Environment

A stable, streamlined Python project template for experimentation and rich interactive display — without requiring Jupyter notebooks.

Includes:   
- Opinionated Python formatting with Black
- Debugging support via VS Code’s Debug Console
- Clean and minimal project scaffolding
- Optional Jupyter Notebook integration
- Web-based interactive visualisation using Streamlit
- Easy virtual environment setup and commands via make

Ideal for learners, data explorers, and developers who want to combine Python scripting with browser-based UIs — all inside a reproducible project structure.

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

### 🖥️ Activating the Virtual Environment (Cross-Platform)

Before running code or installing packages, activate the virtual environment:

#### macOS / Linux (bash or zsh):
```
source .venv/bin/activate
```

#### Windows – PowerShell:
```
. .venv\Scripts\Activate.ps1
```
> ⚠️ If you get a script execution error, temporarily allow it with:
> ```
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

#### Windows – Command Prompt (CMD):
```
.venv\Scripts\activate.bat
```### 🖥️ Activating the Virtual Environment (Cross-Platform)

Before running code or installing packages, activate the virtual environment:

#### macOS / Linux (bash or zsh):
```bash
source .venv/bin/activate
```

#### Windows – PowerShell:
```
. .venv\Scripts\Activate.ps1
```
> ⚠️ If you get a script execution error, temporarily allow it with:
> ```
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
> ```

#### Windows – Command Prompt (CMD):
```
.venv\Scripts\activate.bat
```

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

### 🧩 Optional: Avoid Streamlit link prompts in VS Code

To stop VS Code from asking you whether to open `localhost` links every time:

1. Open the Command Palette
2. Search for: `Preferences: Configure Trusted Domains`
3. Add: `http://localhost:*`
