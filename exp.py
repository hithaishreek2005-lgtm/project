print("************ GMIT ENGINEERING COLLEGE *************")
print("Welcome to college Admission System")
print("Available Departments:")
print("1.CSE")
print("2.AIML")
print("3.ECE")
print("4.EEE")
print("5.MECH")
print("6.CIVIL")
name = input("enter student name:")
department = input("enter your department")
if department == "CSE" or department == "AIML" or department =="ECE" or department =="MECH":
    print("welcome to GMIT college")
    marks = int(input("enter your 12 th marks:"))
    if marks>=85:
        print("Admission confirmed")
        print("you are eligible for scholarship")
    elif marks >=60:
        print("Admission confirmed")
        print("No scholorship")
    elif marks >=40:
        print("you are eligible for management quota")
    else:
        print("sorry,you are not eligible for admission")
else:
    print("sorry,this department is not avilable")