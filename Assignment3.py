# 1. College Student Information
class CollegeStudent:
    def __init__(self, student_name, student_age, department):
        self.student_name = student_name
        self.student_age = student_age
        self.department = department

st = CollegeStudent("Rahul", 20, "BCA")

print("Student Details")
print("Name :", st.student_name)
print("Age :", st.student_age)
print("Department :", st.department)


# 2. Vehicle Class
class Vehicle:
    def __init__(self, company, vehicle_name, cost):
        self.company = company
        self.vehicle_name = vehicle_name
        self.cost = cost

v1 = Vehicle("Maruti", "Swift", 800000)
v2 = Vehicle("Honda", "City", 1200000)

print("\nVehicle 1")
print(v1.company, v1.vehicle_name, v1.cost)

print("\nVehicle 2")
print(v2.company, v2.vehicle_name, v2.cost)


# 3. Staff Class
class Staff:
    def __init__(self, staff_id, staff_name, monthly_salary):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.monthly_salary = monthly_salary

staff1 = Staff(201, "Rakesh", 45000)

print("\nStaff Information")
print("ID :", staff1.staff_id)
print("Name :", staff1.staff_name)
print("Salary :", staff1.monthly_salary)


# 4. Box Class
class Box:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def find_area(self):
        print("Area =", self.l * self.b)

box = Box(12, 4)
box.find_area()


# 5. RoundShape Class
class RoundShape:
    def __init__(self, r):
        self.r = r

    def find_area(self):
        result = 3.14 * self.r * self.r
        print("Circle Area =", result)

circle1 = RoundShape(5)
circle1.find_area()


# 6. Savings Account
class SavingsAccount:
    def __init__(self, holder_name, amount):
        self.holder_name = holder_name
        self.amount = amount

    def add_money(self, money):
        self.amount += money
        print("Amount Added:", money)
        print("Current Balance:", self.amount)

    def remove_money(self, money):
        if money <= self.amount:
            self.amount -= money
            print("Amount Withdrawn:", money)
            print("Current Balance:", self.amount)
        else:
            print("Balance Not Sufficient")

account = SavingsAccount("Ankit", 15000)

account.add_money(2000)
account.remove_money(4000)


# 7. Bird and Parrot Class
class Bird:
    def make_sound(self):
        print("Bird Sound")

class Parrot(Bird):
    def make_sound(self):
        print("Parrot Says Hello")

p = Parrot()
p.make_sound()


# 8. Human and Learner Class
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Learner(Human):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

    def show(self):
        print("\nStudent Record")
        print("Name :", self.name)
        print("Age :", self.age)
        print("Roll No :", self.roll)

learner1 = Learner("Neha", 18, 15)
learner1.show()


# 9. Simple Math Operations
class MathOperation:
    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        if y != 0:
            return x / y
        return "Cannot Divide By Zero"

a = float(input("\nEnter First Value: "))
b = float(input("Enter Second Value: "))

obj = MathOperation()

print("Sum =", obj.addition(a, b))
print("Difference =", obj.subtraction(a, b))
print("Product =", obj.multiplication(a, b))
print("Quotient =", obj.division(a, b))


# 10. Book Store Class
class BookStore:
    def __init__(self, title, writer, amount):
        self.title = title
        self.writer = writer
        self.amount = amount

    def display(self):
        print("\nBook Title :", self.title)
        print("Author :", self.writer)
        print("Price :", self.amount)

b1 = BookStore("Python Basics", "John Smith", 450)
b2 = BookStore("Database Concepts", "James Lee", 600)
b3 = BookStore("AI Fundamentals", "David Miller", 750)

b1.display()
b2.display()
b3.display()