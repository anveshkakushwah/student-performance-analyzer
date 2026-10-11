def get_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter {subject} marks: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")



def show_title():
    print("===== Student Performance Analyzer =====")


show_title()

def calculate_total(subjects):
    total = sum(subjects.values())
    return total

student_name = input("Enter student name: ")

python_marks = get_marks("Python")
dsa_marks = get_marks("DSA")
dbms_marks = get_marks("DBMS")
maths_marks = get_marks("Maths")
cn_marks = get_marks("Computer Networks")

subjects = {
    "Python": python_marks,
    "DSA": dsa_marks,
    "DBMS": dbms_marks,
    "Maths": maths_marks,
    "Computer Networks": cn_marks
}

highest_subject = max(subjects, key=subjects.get)
highest_marks = subjects[highest_subject]
lowest_subject = min(subjects, key=subjects.get)
lowest_marks = subjects[lowest_subject]

print("\n----- Subject-wise Analysis -----")

for subject, marks in subjects.items():
    if marks >= 80:
        performance = "Excellent"
    elif marks >= 60:
        performance = "Good"
    elif marks >= 40:
        performance = "Average"
    else:
        performance = "Needs Improvement"

    print(f"{subject}: {marks}/100 - {performance}")
    
total_marks = calculate_total(subjects)

percentage = ( total_marks / 500 )*100



# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
    
    

# PASS or fail    
if percentage >= 40:
    status = "PASS"
else:
    status = "FAIL" 


# C — Result mein Grade + Status show

print()
print("---------- Result ----------")

print("Student:", student_name)
print("Total Marks:", total_marks, "/500")
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
print("Status:", status)
print("Highest Marks:", highest_marks, "-", highest_subject)
print("Lowest Marks:", lowest_marks, "-", lowest_subject)
    
