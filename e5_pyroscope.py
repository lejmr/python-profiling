import os, time

import pyroscope
pyroscope.configure(
  application_name="my.python.app",
  server_address="http://localhost:4040",
)

def slow_function(n: int) -> None:
    """A slow function to test profiling."""
    for i in range(n):
        i ** 2

def slow_function_b(n: int) -> None:
    """A slow function to test profiling."""
    for i in range(n):
        slow_function_c(i + 2)

def slow_function_c(n: int) -> None:
    """A slow function to test profiling."""
    for i in range(n):
        slow_function(i + 3)


if __name__ == "__main__":
    print(os.getpid())
    time.sleep(5)
    while True:
        print("Super fast operation")
        slow_function(10)
        slow_function_b(1000)
        slow_function_c(10_000)
        print("All is done.")
