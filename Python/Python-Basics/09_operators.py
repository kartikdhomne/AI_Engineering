# ==========================================
# OPERATORS
# ==========================================

# Arithmetic Operators

a = 20
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Comparison Operators

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Assignment Operators

x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)

# Logical Operators

age = 25
salary = 50000

print(age > 18 and salary > 30000)
print(age > 18 or salary > 100000)
print(not age < 18)

# Identity Operators

a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)

print(a is not c)

# Membership Operators

language = "Python"

print("Py" in language)
print("Java" not in language)

# Bitwise Operators

a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)