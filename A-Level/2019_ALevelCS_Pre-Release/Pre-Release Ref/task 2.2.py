fileHandler = open('records.txt','r')  # to open pre-existing text file
id= input("enter the id you want to search")   # string datatype
rec=fileHandler.readline() # reads the firsdt record of file
found=False         # boolean variable
while(len(rec)>0):
    list=rec.split('#')         # split the record and shift in the list
    if (list[0]==id):
        print(list[1])
        found=True
    rec=fileHandler.readline()

if found==False:
    print("Student ID not found")


#Task 3
fileHandler = open('records.txt','r')  # to open pre-existing text file
id= input("enter the first two letters of Id which you want to search")   # string datatype
rec=fileHandler.readline() # reads the firsdt record of file
found=False         # boolean variable
while(len(rec)>0):
    list=rec.split('#')         # split the record and shift in the list
    if (list[0][:2]==id):
        print(list[1])
        found=True
    rec=fileHandler.readline()

if found==False:
    print("Student ID not found")



    
