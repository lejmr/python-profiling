import os, time

def slow_function(n: int = 1000_000) -> None:
    """A slow function to test profiling."""
    for i in range(n):
        i ** 2

if __name__ == "__main__":
    print(os.getpid())
    time.sleep(5)
    while True:
        print("Super fast operation")
        slow_function()
        print("All is done.")
