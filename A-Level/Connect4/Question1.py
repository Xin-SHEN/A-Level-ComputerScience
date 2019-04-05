def DisplayMenu():
    print("DisplayMenu")
    
def ReadFile():
    print("ReadFile")
    
NoOfAttempt = 0
while NoOfAttempt<3:
    DisplayMenu()
    choice = int(input("Make your choice:"))
    if choice == 1:
        ReadFile()
    elif choice == 2:
        print("Add customer code")
    elif choice == 3:
        print("Search customer code")
    elif choice == 4:
        NoOfAttempt = 3
    NoOfAttempt+=1
    print("NoOfAttempt",NoOfAttempt)