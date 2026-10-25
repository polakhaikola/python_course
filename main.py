# ============================================================
#  Problem 1: Swap the values of two variables
# ============================================================
def problem1():
    print("\n--- Problem 1: Swap Two Variables ---")
    a = input("Enter value of a: ")
    b = input("Enter value of b: ")
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a          # Pythonic swap
    print(f"After swap:  a = {a}, b = {b}")


# ============================================================
#  Problem 2: Distance between two points
# ============================================================
def problem2():
    print("\n--- Problem 2: Distance Between Two Points ---")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(f"Distance = {distance:.4f}")


# ============================================================
#  Problem 3: Check even or odd
# ============================================================
def problem3():
    print("\n--- Problem 3: Even or Odd ---")
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is an EVEN number.")
    else:
        print(f"{num} is an ODD number.")


# ============================================================
#  Problem 4: Check if a character is a vowel
# ============================================================
def problem4():
    print("\n--- Problem 4: Vowel or Not ---")
    ch = input("Enter a character: ").lower()

    if len(ch) != 1 or not ch.isalpha():
        print("Please enter a single alphabetic character.")
    elif ch in "aeiou":
        print(f"'{ch}' is a VOWEL.")
    else:
        print(f"'{ch}' is NOT a vowel (it is a consonant).")


# ============================================================
#  Problem 5: Convert marks to grade
#  (Typical university grading criteria)
# ============================================================
def problem5():
    print("\n--- Problem 5: Marks to Grade ---")
    marks = float(input("Enter student's marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter a value between 0 and 100.")
    elif marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Marks: {marks}  →  Grade: {grade}")


# ============================================================
#  Main — Run all problems
# ============================================================
if __name__ == "__main__":
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
