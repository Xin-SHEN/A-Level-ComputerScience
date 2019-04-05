#Task 2.1
studentfile=open("student.txt","a")
numberofstudents=int(input("Please enter the number of students in the class"))
for i in range(numberofstudents):
    studentid=input("Please enter the student id. Please enter two letters followed by four numbers.")
    while studentid[0:2].isalpha()==False or studentid[2:6].isdigit()==False or len(studentid)!=6:
        studentid=input("Please enter the student id again, you enter the wrong format.")
    studentaddress=input("Please enter the email address")
    studentfile.write(studentid+"#"+studentaddress+"\n")
studentfile.close()
    
#Task 2.2
studentfile=open("student.txt","r")
count=len(open("student.txt","r").readlines())
line=studentfile.readlines()
line=[c.strip() for c in line ]
studentsearch=input("Please enter the student id you want to search.")
found=False

for i in range(count):
    if studentsearch in line[i]:
        index=i
        found=True
        break

if found==True:
    print("The email address of this student is:",line[index][7:])
else:
    print("The id is not found in the file.")
studentfile.close()

        
