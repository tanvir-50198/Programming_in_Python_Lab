# Lab 05: Functions and Lists

# Question 1: Campus Resource Tracker
# A university wants to track resources such as laptops and projectors.
# 1. Display all resources.
# 2. Search resources by category.
# 3. Find resources with zero quantity.

resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

def display_resources(resources):
    for r in resources:
        print(r)

def search_by_category(resources, category):
    for r in resources:
        if r[2] == category:
            print(r)

def find_unavailable(resources):
    for r in resources:
        if r[3] == 0:
            print(r)

print("Question 1: Campus Resource Tracker")
print("\nAll Resources:")
display_resources(resources)

print("\nElectronics:")
search_by_category(resources, "Electronics")

print("\nUnavailable Resources:")
find_unavailable(resources)


# Question 2: Student Marks Investigator
# An instructor wants to analyze student marks.
# 1. Calculate the average marks.
# 2. Classify performance.
# 3. Display each student's report.

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

def calculate_average(marks):
    return sum(marks) / len(marks)

def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

def display_report(students):
    for s in students:
        average = calculate_average(s[2])
        result = classify_performance(average)
        print(s[0], s[1], round(average, 2), result)

print("\nQuestion 2: Student Marks Investigator")
print("\nStudent Report:")
display_report(students)