import threading

def slow_function(n: int = 1000_000) -> None:
    """A slow function to test profiling."""
    for i in range(n):
        i ** 2

if __name__ == "__main__":
    print("Super fast operation")
    t1 = threading.Thread(target=slow_function, args=(100_000_000,))
    t2 = threading.Thread(target=slow_function, args=(100_000_000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("All is done.")
