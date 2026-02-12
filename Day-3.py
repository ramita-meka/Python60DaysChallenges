num=int(input("Enter the no.of students : "))
marks=[]
valid_count=0
failed_count=0
section=input("Enter a section(A/B) : ")
for i in range(num):
    N=int(input("Enter the student marks :"))
    if section == "A":
        N=N+5
        if N>100 and N<106:
            N=100
        print("Incremented marks for Section-A are: ", N)
    else:
        print("No marks are Incremented for Section-B")
    marks.append(N)

for i in marks:
       if i>=90 and i<=100:
        valid_count=valid_count+1
        print(f"{i} -> Excellent")
       elif i>=75 and i<=89:
        valid_count=valid_count+1
        print(f"{i} -> Very Good")
       elif i>=60 and i<=74:
        valid_count=valid_count+1
        print(f"{i} -> Good")
       elif i>=40 and i<=59:
        valid_count=valid_count+1
        print(f"{i} -> Average")
       elif i>=0 and i<=39:
        failed_count=failed_count+1
        valid_count=valid_count+1
        print(f"{i} -> Fail")
       else:
        print(f"{i} -> Invalid")
print("Total Valid Students: ",valid_count)
print("Total Failed Students: ",failed_count)