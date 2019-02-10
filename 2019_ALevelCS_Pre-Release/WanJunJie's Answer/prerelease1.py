
#Task1.1
numberofstudents=int(input("Please enter the number of students"))
student=[]
for i in range(numberofstudents):
    studentname=input("Please enter the student name")
    studentaddress=input("Please enter the email address")
    student.append(studentname+"#"+studentaddress)

print("name | email")
for i in range(numberofstudents):
    index = student[i].find("#")
    print(student[i][:index]," | ",student[i][index+1:])



#Task1.2
studentdelete=input("Please enter the student who leave the school.")
print("name | email")
for i in range(numberofstudents):
    if studentdelete in student[i]:
        index=i
        print(student[index][:student[index].find("#")]," | ",student[index][student[index].find("#")+1:])
        break
del student[index]



#Task1.3   Task1.4
studentsearch=input("Please enter the student you want search for.")
found=False
print("name | email")
for i in range(numberofstudents-1):
    if studentsearch in student[i]:
        print(student[i][:student[i].find("#")]," | ",student[i][student[i].find("#")+1:])
        found=True
if found==False:
    print("The student you search is not in class.")



