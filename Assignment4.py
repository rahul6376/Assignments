# Question 1

numbers = [2, 5, 8, 11, 15, 17]

print("Prime Numbers:")

for num in numbers:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num)


# Question 2

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()


# Question 3

def check_numbers(lst):
    even_count = 0
    odd_sum = 0

    for n in lst:
        if n % 2 == 0:
            even_count = even_count + 1
        else:
            odd_sum = odd_sum + n

    print("Even Count =", even_count)
    print("Odd Sum =", odd_sum)


data = [1, 2, 3, 4, 5, 6]
check_numbers(data)


# Question 4

def simple_interest(p, r=5, t=2):
    si = (p * r * t) / 100
    return si

print(simple_interest(1000))
print(simple_interest(p=2000, r=10, t=3))


# Question 5 and 6

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"


s1 = Student("Rahul", 85)
s2 = Student("Amit", 65)

print(s1.name, s1.grade())
print(s2.name, s2.grade())


# Question 7

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print("Low Balance")

    def show(self):
        print("Balance =", self.__balance)


a1 = BankAccount(5000)

a1.deposit(1000)
a1.withdraw(2000)
a1.show()


# Question 8

try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    print("Answer =", n1 / n2)

except ZeroDivisionError:
    print("Division by zero not possible")

except ValueError:
    print("Invalid Input")


# Question 9

file = open("student.txt", "w")

file.write("Rahul 85")

file.close()

file = open("student.txt", "r")

print(file.read())

file.close()


# Question 10

try:
    file = open("numbers.txt", "r")

    total = 0
    count = 0

    for line in file:
        total = total + int(line)
        count = count + 1

    print("Total =", total)
    print("Average =", total / count)

    file.close()

except FileNotFoundError:
    print("File not found")