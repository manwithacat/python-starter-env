# slow_function.py

# This is a deliberately slow function that performs a large number of arithmetic operations.
# It exists solely to simulate computational workload for profiling purposes.
def slow_function():
    total = 0
    for i in range(10_000):
        for j in range(100):
            total += (i * j) % 7
    return total

# Entry point for the script
if __name__ == "__main__":
    print(slow_function())

# ------------------------------------------------------------
# 💡 How to profile this script from the command line:
#
# Option 1: Basic profiling with cProfile (sorted by time spent)
#     python -m cProfile -s time profiling_example.py
#
# Option 2: Save profile data to a file for later analysis
#     python -m cProfile -o profile.out profiling_example.py
#
# Option 3: Visualise the profile with snakeviz
#     snakeviz profile.out
#
#     🖥️ This launches a local web server and opens a browser window
#     with an interactive visualisation of the profiling data.
#     You can explore function call time, call stacks, and hotspots.
#
# ------------------------------------------------------------