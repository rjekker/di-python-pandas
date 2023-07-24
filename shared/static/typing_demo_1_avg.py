def average(a, b, c):
    return a + b + c / 3


print(average(1, '5', 7))


# After:
# def average(a: int, b: int, c: int) -> float:
#     return (a + b + c) / 3


# print(average(1, 5, 7))
# print(average("this", "still", "runs"))
