# ==========================================
# STRINGS
# ==========================================

name = "Python"

print(name)

# Indexing

print(name[0])
print(name[-1])

# Slicing

print(name[0:3])
print(name[2:])
print(name[:4])

# Length

print(len(name))

# Concatenation

first = "Hello"
second = "World"

print(first + " " + second)

# Repetition

print("Hi " * 3)

# Membership

print("Py" in name)

# String methods

text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print(text.replace("python", "Java"))

print(text.split())

print(text.startswith("python"))

print(text.endswith("ing"))

print(text.find("program"))

print(text.count("m"))

print(text.strip())