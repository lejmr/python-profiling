def slow_function(n: int = 1000_000) -> None:
    """A slow function to test profiling."""
    for i in range(n):
        i ** 2

def a():
    print("a")
    slow_function()

def b():
    print("b")
    a()
    slow_function()

def c():
    print("c")
    b()
    slow_function()

if __name__ == "__main__":
    print("Super fast operation")
    a()
    b()
    c()
    print("All is done.")
