def fib(i):
    if not isinstance(i, int):
        raise TypeError("Input must be type int")
    if i < 0:
        raise ValueError("Input must be non-negative")
    if i == 0:
        return 0
    if i <= 2:
        return 1
    return fib(i - 1) + fib(i - 2)

if __name__ == "main":
    print(fib(36))