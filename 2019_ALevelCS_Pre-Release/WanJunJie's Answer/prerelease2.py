#Task1.6

numberofstudents=int(input("Please enter the number of students."))
student=[[0 for x in range(4)]for i in range(numberofstudents)]
for i in range(numberofstudents):
        studentname=input("Please enter the student name.")
        studentaddress=input("Please enter the email address.")
        dateofbirth=input("Please enter the date of birth.")
        studentid=input("Please enter the student id.")
        student[i][0]=studentname
        student[i][1]=studentaddress
        student[i][2]=dateofbirth
        student[i][3]=studentid

print("name | email | date of birth | id")
for i in range(numberofstudents):
        print(student[i][0]," | ",student[i][1]," | ",student[i][2]," | ",student[i][3])
              

studentdelete=input("Please enter the student who leave the school.")
print("name | email | date of birth | id")
for i in range(numberofstudents):
    if studentdelete in student[i]:
        index=i
        print(student[i][0]," | ",student[i][1]," | ",student[i][2]," | ",student[i][3])
        break


del student[index]



found=False
studentsearch=input("Please enter the student you want search for.")
print("name | email | date of birth | id")
for i in range(numberofstudents-1):
    if studentsearch in student[i][0]:
        print(student[i][0]," | ",student[i][1]," | ",student[i][2]," | ",student[i][3])
        found=True


if found==False:
    print("The student is not in the class.")




