name=input("Enter your name:")
n=int(input("Enter number of weights:"))

weight_list=[]
veryLight_list=[]
normalLoad_list=[]
heavyLoad_list=[]
overload_list=[]
invalid_list=[]

for i in range(n):
    value=int(input("Enter weight:"))
    weight_list=weight_list+[value]

print(weight_list)

valid_count=0

for i in weight_list:
    if i<0:
        invalid_list=invalid_list+[i]
    else:
        valid_count=valid_count+1
        if i<=5:
            veryLight_list=veryLight_list+[i]
        elif i<=25:
            normalLoad_list=normalLoad_list+[i]
        elif i<=60:
            heavyLoad_list=heavyLoad_list+[i]
        else:
            overload_list=overload_list+[i]

L=0
for i in name:
    if i!=" ":
        L=L+1

PLI=L%3
print("L=",L)
print("PLI=",PLI)

affected=0

if PLI==0:
    for i in overload_list:
        invalid_list=invalid_list+[i]
        affected=affected+1
    overload_list=[]

elif PLI==1:
    for i in veryLight_list:
        affected=affected+1
    veryLight_list=[]

elif PLI==2:
    for i in veryLight_list:
        affected=affected+1
    for i in overload_list:
        affected=affected+1
    veryLight_list=[]
    overload_list=[]


print("Very Light:",veryLight_list)
print("Normal Load:",normalLoad_list)
print("Heavy Load:",heavyLoad_list)
print("Overload:",overload_list)
print("Invalid:",invalid_list)
print("Valid weights:",valid_count)
print("Affected by PLI:",affected)
