name=str(input("Enter Full Name: "))
email_id=str(input("Enter Email ID: "))
number=str(input("Enter Mobile Number: "))
age=str(input("Enter a Age: "))
n=len(name)
if name.count(' ')>=1 and (name[0]!='_' and name[n-1]!='_'):
    if (email_id.count('@')==1 and email_id.count('.')==1) and email_id[0]!='@':
        if len(number)==10 and (number>='0000000000' and number<='9999999999') and number[0]!='0':
            if age>='18' and age<='60':
              print("User Profile is VALID")
            else:
              print("User Profile is INVALID")
        else:
            print("User Profile is INVALID")
    else:
        print("User Profile is INVALID")
else:
    print("User Profile is INVALID")