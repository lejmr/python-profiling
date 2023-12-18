import time

def slow_function(n: int = 1000_000) -> None:
    """A slow function to test profiling."""
    for i in range(n):
        i ** 2


def test_slow_function(benchmark) -> None:
    benchmark(slow_function)

if __name__ == "__main__":
    print("Super fast operation")
    start = time.time()
    slow_function(100_000_000)
    duration = time.time() - start
    print(f"Duration: {duration:.5f} seconds")