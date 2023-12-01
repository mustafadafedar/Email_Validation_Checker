
def Email():

 k,j,d = 0,0,0
 email = input("Enter Your Email : ")
 if len(email) >= 6:
     if email[0].isalpha():
         if ("@" in email) and (email.count("@") == 1):
             if (email[-4] == ".") ^ (email[-3] == "."):
                 for i in email:
                     if i==i.isspace():
                         k=1
                     elif i.isalpha():
                         if i==i.upper():
                             j=1
                     elif i.isdigit():
                         continue
                     elif i=="_" or i=="." or i=="@":
                         continue
                     else:
                         d=1
                 if k==1 or j==1 or d==1:
                     print("please remove the space and uppercase")
             else:
                 print("'.' is missing or in wrong position")
         else:
             print("'@' is missing")
     else:
        print("first letter must be alphabet")
 else:
     print("Email characters must be greater than 6")

op = Email()
print(op)