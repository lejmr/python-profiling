import time

def slow_function(n: int = 1000_000) -> None:
    """A slow function to test profiling."""
    for i in range(n):
        i ** 2

if __name__ == "__main__":
    print("Super fast operation")
    start = time.perf_counter()
    slow_function(100_000_000)
    duration = time.perf_counter() - start
    print(f"Duration: {duration:.5f} seconds")