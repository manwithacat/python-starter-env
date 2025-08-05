"""
🎓 seaborn_example.py — An Educational Script for Visual Feedback and Plotting

This script demonstrates how to generate a basic Seaborn plot with feedback for the user
during the data-loading and plotting phase. It includes a smart detection mechanism that:

1. Uses a terminal spinner (`yaspin`) when run in a real terminal
2. Falls back to plain print statements when executed in environments like
   the VS Code Debug Console, where animated spinners don't render correctly

🧠 Pedagogical Goals:
- Show how to conditionally handle terminal vs. non-terminal output
- Demonstrate the difference between interactive and non-interactive execution
- Reinforce the use of visual feedback (`print` or spinner) before GUI rendering (`plt.show()`)

🧪 Features:
- Loads the `penguins` dataset using Seaborn
- Adds a small delay to simulate data processing, and shows a spinner during this time
- Displays a histogram of flipper lengths by species
- Provides user-friendly console messages before and after rendering the plot

⚙️ How to Use:

Option 1: Run in the VS Code Terminal (correct rendering with spinner)
--------------------------------------------------------------
$ python seaborn_example.py

Option 2: Run with the VS Code Debugger (no spinner, but still clear output)
--------------------------------------------------------------
- Open this file in VS Code
- Press F5 or click ▶️ 'Run and Debug'
- Observe that fallback `print()` statements are used

Dependencies:
- seaborn
- matplotlib
- yaspin (only used when available and appropriate)

"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import time

def is_debug_console():
    """Return True if not running in a real terminal."""
    return not sys.stdout.isatty()

def main():
    if is_debug_console():
        print("🔄 Loading data and generating plot...")
        df = sns.load_dataset("penguins")
        time.sleep(2)  # Simulate work
        sns.histplot(data=df, x="flipper_length_mm", hue="species", kde=True)
        plt.title("Penguin Flipper Length by Species")
        print("📈 Displaying plot. Close the window to continue...")
        plt.show()
        print("✅ Plot window closed.")
    else:
        from yaspin import yaspin
        with yaspin(text="Loading data and generating plot...", color="cyan") as spinner:
            df = sns.load_dataset("penguins")
            time.sleep(2)  # Simulate work
            sns.histplot(data=df, x="flipper_length_mm", hue="species", kde=True)
            plt.title("Penguin Flipper Length by Species")
            spinner.ok("✅")

        print("📈 Displaying plot. Close the window to continue...")
        plt.show()
        print("✅ Plot window closed.")

if __name__ == "__main__":
    main()