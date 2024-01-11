# We import all variables and functions
from modul_a import find_index
import random

# print(modul_a.test)
courses = ["PE", "History", "Math"]
index = find_index(courses, "History")
print(index)  # Prints 0

print(random.__file__)

file = open(r"C:\Users\libor\AppData\Local\Programs\Python\Python312\Lib\random.py")
print(file.read())
