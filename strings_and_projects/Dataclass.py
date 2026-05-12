class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int

u = User("Somm", 18)
print(u)