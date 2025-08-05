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