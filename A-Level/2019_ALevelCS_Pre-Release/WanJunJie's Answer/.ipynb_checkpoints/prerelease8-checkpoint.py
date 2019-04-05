#Task 2.6 append
studentfile=open("student.txt","a")
numberofstudentsadd=int(input("Please enter the number of students you want to add to the list."))
for i in range(numberofstudentsadd):
    studentid=input("Please enter the student id. Please enter two letters followed by four numbers.")
    while studentid[0:2].isalpha()==False or studentid[2:6].isdigit()==False or len(studentid)!=6:
        studentid=input("Please enter the student id again, you enter the wrong format.")
    studentaddress=input("Please enter the email address of the student")
    homeaddress=input("Please enter the home address of the student.")
    tutor=input("Please enter the tutor of the student")
    studentfile.write(studentid+"\n"+studentaddress+"\n"+homeaddress+"\n"+tutor+"\n")

studentfile.close()
