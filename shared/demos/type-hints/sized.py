from typing import Sized

def even_length(l: Sized) -> bool:
    return len(l) % 2 == 0

print(even_length([1,2,3]))
print(even_length((1,2,3)))
print(even_length(dict()))
print(even_length("abc"))
print(even_length(None))