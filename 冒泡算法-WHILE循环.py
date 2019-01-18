import random
MyList = []

for x in range(0,100,1):
    MyList.append(random.randint(0,999))
    
print(MyList)

print("-------------")
MaxIndex = 100
n = MaxIndex-1
temp = 0
MoreSwap = True
while MoreSwap == True:
    #MoreSwap = False
    for j in range(n):
        if MyList[j]>MyList[j+1]:
            temp = MyList[j]
            MyList[j] = MyList[j+1]
            MyList[j+1] = temp
            MoreSwap = True
        else:
            MoreSwap = False
    n = n-1
    
print(MyList)
print(100-n)
        