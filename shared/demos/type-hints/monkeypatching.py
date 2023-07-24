class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def greet(p: Person) -> None:
    print("Hi", p.name, "from",  p.city)


r = Person("Reindert", 40)
r.city = "Amsterdam"
greet(r)
