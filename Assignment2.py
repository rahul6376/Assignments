# 1 Tuple

t = (11, 22, 33, 44, 55)

print("First value =", t[0])
print("Last value =", t[-1])
print("Length =", len(t))
print("Some values =", t[1:4])


# 2 Tuple

cars = ("BMW", "Audi", "Honda", "Toyota")

print("Second car =", cars[1])
print("Last two cars =", cars[2:])
print("Total cars =", len(cars))


# 3 Set

s = {5, 10, 15, 20, 25}

print("Set =", s)
print("Length =", len(s))
print("15 present or not =", 15 in s)


# 4 Two Sets

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}

print("Union =", a | b)
print("Intersection =", a & b)


# 5 Dictionary

student = {
    "name": "Rohit",
    "roll": 12,
    "branch": "CSE"
}

print(student)
print("Name =", student["name"])
print("Roll =", student["roll"])
print("Branch =", student["branch"])


# 6 Largest, second largest and smallest

lst = [9, 25, 67, 14, 88, 45]

lst.sort()

print("Smallest =", lst[0])
print("Largest =", lst[-1])
print("Second Largest =", lst[-2])


# 7 Reverse List

x = [2, 4, 6, 8, 10]

print("Original =", x)

x.reverse()

print("Reverse =", x)


# 8 Tuple operations

n = (10, 15, 20, 25, 30, 35)

c = 0

for i in n:
    if i % 5 == 0:
        c += 1

print("Count =", c)
print("Sum =", sum(n))
print("Average =", sum(n) / len(n))


# 9 Dictionary marks

marks = {
    "Aman": 70,
    "Neha": 85,
    "Riya": 95,
    "Kunal": 80
}

high = max(marks, key=marks.get)
low = min(marks, key=marks.get)

print("Highest =", high, marks[high])
print("Lowest =", low, marks[low])

print("Marks above 80")

for k, v in marks.items():
    if v > 80:
        print(k, v)


# 10 Frequency of elements

arr = [1, 2, 1, 3, 2, 1, 4]

d = {}

for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)


# 11 Duplicate elements

arr = [10, 20, 30, 10, 40, 20, 50]

print("Duplicate values are")

for i in arr:
    if arr.count(i) > 1:
        print(i)