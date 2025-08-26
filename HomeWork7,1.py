def say_hi(name, age):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a positive integer")
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print("OK")
