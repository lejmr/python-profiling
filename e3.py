def slow_function(n: int = 1000_000) -> None:
    """A slow function to test profiling."""
    for i in range(n):
        i ** 2

if __name__ == "__main__":
    print("Super fast operation")
    slow_function(100_000_000)
    slow_function(100_000_000)
    slow_function(100_000_000)
    print("All is done.")
