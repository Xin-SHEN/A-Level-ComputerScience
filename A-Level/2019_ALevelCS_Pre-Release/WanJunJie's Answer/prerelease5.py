#Task 2.4
studentfile=open("student.txt","a")
numberofstudentsadd=int(input("Please enter the number of students you want to add to the list."))
for i in range(numberofstudentsadd):
    studentid=input("Please enter the student id. Please enter two letters followed by four numbers.")
    while studentid[0:2].isalpha()==False or studentid[2:6].isdigit()==False or len(studentid)!=6:
        studentid=input("Please enter the student id again, you enter the wrong format.")
    studentaddress=input("Please enter the email address")
    studentfile.write(studentid+"#"+studentaddress+"\n")
studentfile.close()

