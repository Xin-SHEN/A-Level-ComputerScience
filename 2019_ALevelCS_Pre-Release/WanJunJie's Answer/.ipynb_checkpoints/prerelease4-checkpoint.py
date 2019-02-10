#Task 2.3
studentfile=open("student.txt","r")
count=len(open("student.txt","r").readlines())
line=studentfile.readlines()
line=[c.strip() for c in line ]
studentsearch=input("Please enter the student id you want to search.")
found=False

for i in range(count):
    if studentsearch in line[i]:
        print("The email address of this student with student id",line[i][0:6], "is:",line[i][7:])
        found=True
        

if found==False:
    print("The id is not found in the file.")
studentfile.close()
