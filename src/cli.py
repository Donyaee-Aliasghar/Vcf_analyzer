"""Main module for running the program and measuring its execution time."""

import time

from runner import runner


def main():
    """Main function with time package."""
    start = time.time()
    runner()
    end = time.time()

    print("-" * 40)

    # Show time process.
    print(f"[✨] Process time : >>> {end - start:.10f} s <<<")


# ============================================

# import timeit


# def main():
#     """main function with timeit package."""
#     if __name__ == "__main__":
#         execution_time = timeit.timeit(runner(), number=1)

#         print("-" * 40)

#         # Show time process.
#         print(f"[✨] Process time : >>> {execution_time:.10f} s <<<")


if __name__ == "__main__":
    main()
