from typing import List


def roots(l: List[int]) -> List[float]:
    return [x**0.5 for x in l]


print(roots(range(100)))
