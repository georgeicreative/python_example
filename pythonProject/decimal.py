def binary(n):
    print(n%2)
    if n > 1:
        binary(n//2)
binary(21)