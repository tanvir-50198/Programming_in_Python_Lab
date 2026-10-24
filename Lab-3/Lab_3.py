a, b, temp = 10, 20, 0

#Problem 1. Write a Python program to swap the values of two variables.

print ("Before swap value of a and b is : ", a, b)
temp = a
a = b
b = temp

print ("After swap value of a and b is : ", a, b)

print()
print()

#Problem 2. Write a program to compute the distance between two points, taking input from the user.
#Distance formula:d =√︁(x2 − x1)2 + (y2 − y1)2

import math
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("distance of two points :", d)

print()
print()

#Problem 3. Write a program to check whether the given number is an even or odd number.

n = int(input("Enter a integer number : "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


print()
print()
#Problem 4. Take a character as input and determine whether it is a vowel. Print an appropriate message (vowel/not vowel)

ch = input("Enter a character : ").lower()

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
    print("Vowel")
else:
    print("Not Vowel")

print()
print()

#Problem 5. Write a program to convert a student’s marks of a course into a grade. Use the grading criteria of our university
marks = float(input("Enter student marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 85:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B+")
elif marks >= 75:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C+")
elif marks >= 65:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D+")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")
    