#Task 2.6
studentfile=open("student.txt","r")
count=len(open("student.txt","r").readlines())
line=studentfile.readlines()
line=[c.strip() for c in line ]
studentsearch=input("Please enter the student id you want to search.")
found=False

for i in range(count):
    if studentsearch in line[i]:
        print("The student's student id is:",line[i], "The email address is:",line[i+1],
              "The home address is:",line[i+2],"The tutor of this student is:",line[i+3])
        found=True
        

if found==False:
    print("The student is not in this class.")
studentfile.close()



        
