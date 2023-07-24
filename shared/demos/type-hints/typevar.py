from typing import TypeVar, Dict, List

T = TypeVar("T", list, str)

def reverse(x: T) -> T:
    return x[::-1]

def values_as_list(d: Dict[T]) -> List[T]:
    return list(d.values())

print(reverse([3,4,5]))