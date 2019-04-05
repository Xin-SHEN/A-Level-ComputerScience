import random
MyList = []

for x in range(0,100,1):
    MyList.append(random.randint(0,999))
    
print(MyList)

print("-------------")

MaxIndex = 100
n = MaxIndex-1
temp = 0
for i in range(MaxIndex-1):
    for j in range(n):
        if MyList[j]>MyList[j+1]:
            temp = MyList[j]
            MyList[j] = MyList[j+1]
            MyList[j+1] = temp
    n = n-1
    
#for q in range(100):
print(MyList)

