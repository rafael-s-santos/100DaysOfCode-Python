def add(*args: int) -> int:
    """Sum all input values

    Returns:
        int: return the sum of all input values
    """
    total = 0
    for num in args:
        total += num
    return total
        


print(add(2, 2, 12))