"""
🎓 pandas_example.py — Demonstrating Visual Feedback and Environment Detection

This script demonstrates how to provide feedback during data processing and 
how to gracefully handle cases where the runtime environment limits functionality.

🧠 Pedagogical Goals:
- Show how tools like Streamlit or yaspin can be used for richer, more engaging output.
- Demonstrate how to detect whether the script is being run in a proper terminal vs. inside
  the VS Code Debug Console.
- Help students understand that not all Python output is equal — terminal capabilities affect rendering.
- Encourage habits like graceful fallback and environment-aware scripting.

⚠️ Why this matters:
The VS Code Debug Console is not a full terminal. It lacks support for:
- Interactive spinners (e.g. yaspin)
- Streamlit’s runtime context
- ANSI control codes (used for overwriting, colouring, etc.)

As a result, some code that works perfectly in a real terminal will:
- Produce warnings
- Raise visible `SystemExit` exceptions
- Render awkwardly or flood the console with broken spinner frames

🚨 Termination Note:
This script starts a web server (via Streamlit) and runs indefinitely. 
You must **manually terminate it** using **Ctrl+C** in the terminal 
when you're finished viewing the page.

✅ This script detects when it's being misused in a non-terminal context 
and gives the user a clear, helpful message with instructions.

🧪 How to run correctly:
    streamlit run pandas_example.py

"""

import sys
import os
import warnings
import streamlit as st
import pandas as pd
import numpy as np


def make_streamlit_safe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str)

    return df

def is_debug_console():
    """Return True if running in VS Code Debug Console (not a real terminal)."""
    return not sys.stdout.isatty()


def main():
    if is_debug_console():
        print("⚠️  Please run this demo in a terminal: streamlit run pandas_example.py")
        return

    # Silence known fallback warning from Streamlit
    warnings.filterwarnings("ignore", category=UserWarning, module="streamlit")

    # Set seed for reproducibility
    np.random.seed(42)

    n_rows = 20
    df = pd.DataFrame({
        "Date": pd.date_range("2025-01-01", periods=n_rows, freq="D"),
        "Category": np.random.choice(["A", "B", "C"], size=n_rows),
        "Value": np.random.randint(80, 160, size=n_rows),
        "Offset": np.random.randint(-10, 10, size=n_rows),
        "Is_Active": np.random.choice([True, False], size=n_rows)
    })

    # Convert the Date column to ISO-format strings (YYYY-MM-DD) to ensure compatibility
    # with Streamlit's Arrow-based serialization engine. This prevents pyarrow errors 
    # caused by mixed datetime representations (e.g., Timestamp objects in object-typed columns).
    
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
   
    # ⚠️ Note: This makes the column a string, so you lose datetime functionality
    # (e.g., time-based filtering, sorting, or plotting).
   

    # Add a derived column
    df["Adjusted"] = df["Value"] + df["Offset"]

    st.title("📊 Pandas Data Exploration Demo")
    st.write("A slightly more complex DataFrame to demonstrate Streamlit features.")
    st.write("🧪 Column types:", df.dtypes.to_dict())
    st.dataframe(make_streamlit_safe(df))

    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    st.subheader("📊 Filtered View (Active Rows Only)")
    st.dataframe(make_streamlit_safe(df[df["Is_Active"]]))


if __name__ == "__main__":
    main()