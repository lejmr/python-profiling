import time

def duration(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"Duration: {duration:.5f} seconds")
    return wrapper

@duration
def slow_function(n: int = 1000_000) -> None:
    """A slow function to test profiling."""
    for i in range(n):
        i ** 2

if __name__ == "__main__":
    print("Super fast operation")
    slow_function(100_000_000)