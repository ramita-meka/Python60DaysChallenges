student_id=(input("Enter student id: "))
email_id=input("Enter email id: ")
password=input("Enter password: ")
referral_code=input("Enter referral code: ")
n=len(email_id)
if (len(student_id)==7 and student_id.find('CSE-')==0 and
     ('0'<=student_id[4]<='9' and '0'<=student_id[5]<='9' and '0'<=student_id[6]<='9')):
         if (email_id.count('@')==1 and (email_id[0]!='@' and email_id[n-1]!='@') and
              (email_id[n-4]=='.' and email_id[n-3]=='e' and email_id[n-2]=='d' and email_id[n-1]=='u')):
                   if (len(password)>=8 and 'A'<=password[0]<='Z' and
                        (('0'<=password[0]<='9') or
                        ('0'<=password[1]<='9') or
                        ('0'<=password[2]<='9') or
                        ('0'<=password[3]<='9') or
                        ('0'<=password[4]<='9') or
                        ('0'<=password[5]<='9') or
                        ('0'<=password[6]<='9') or
                        ('0'<=password[7]<='9'))):
                          if referral_code.find('REF')==0 and ('0'<=referral_code[3]<='9' and '0'<=referral_code[4]<='9') and referral_code[5]=='@':
                              print("APPROVED")
                          else:
                              print("REJECTED")
                   else:
                       print("REJECTED")
         else:
               print("REJECTED")
else:
        print("REJECTED")