name=input("Enter student name:")
n=int(input("Enter number of subjects:"))
total=0
for i in range(1,n+1):
    mark=float(input(f"Enter mark for subject {i}:"))
    total+=mark
    percentage=total/n
    if percentage>=90:
        grade="A+"
        percentage="outstanding"
    elif percentage>=80:
        grade="A"
        percentage="Excellent"
    elif percentage>=70:
        grade="B"
        percentage="Very Good"
    elif percentage>=60:
        grade="C"
        percentage="Good"
    elif percentage>=50:
        grade="D"
        percentage="Average"
    else:
        grade="F"
        performance="Needs Improvement"
percentage = (total / 500) * 100
print("\n---Academic Performance---")
print("Student Name:",name)
print("Total marks:",total)
print("Percentage:",round(percentage,2),"%")
print("Grade:",grade)
print("Performance:",performance)