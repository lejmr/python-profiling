import sys

def memory_consuming_function(n) -> list[int]:
    return [i for i in range(n)]

if __name__ == "__main__":
    n = 1000_000_000
    var = memory_consuming_function(n)
    var_size = sys.getsizeof(var)
    print(f"{n} ints consume {var_size/1024/1024}MB bytes which is {var_size / n}B per int ... interesting!")
    print(f"Size of one int is {sys.getsizeof(1)}B")