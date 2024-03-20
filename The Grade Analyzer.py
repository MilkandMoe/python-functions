# pylint: disable=missing-function-docstring
# def average_grade():
#     num1 = 85
#     num2 = 90
#     num3 = 100
#     grade_level = (num1 + num2 + num3) / 3
#     grade_level2 = max(grade_level)
#     grade_level3 = min(grade_level)
# print("Print grade: + average_grade()")

# print(average_grade())


# def average_grade(num1, num2, num3):
#     return (num1 + num2 + num3) / 3
# print(average_grade(23, 25, 76)) 
    

def highest_and_lowest_grades():
    average_grade = (85 + 90 + 100) / 3
    highest = max(average_grade)
    minimum = min(average_grade)
    print(f"Highest grade and lowest : + {highest} + {minimum}")
    
def categories():   
    if "A" == 100:
        print("Grade level: A")
    elif "B" == 90:
        print("Grade level: B")
    elif "C" == 80:
        print("Grade level: C")
    else:
        print("Not passing!")