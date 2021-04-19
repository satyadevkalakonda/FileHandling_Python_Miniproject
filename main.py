import os
z=1
while(True):
    print("\n 1. Add Record")
    print("\n 2. Display ALL Records")
    print("\n 3. Search student record by name")
    print("\n 4. Search student record by Rollno")
    print("\n 5. Delete Student Record by Name")
    print("\n 6. Exit")

    n=int(input("Enter Your Choice"))
    if(n==7):
        break
    elif(n==1):
        print("\n Enter students details\n")
        n=input("Enter Name= ")
        r=input("Enter Rollno= ")
        cl=input("Enter class")
        f=open("student.txt","a")
        f.write(n+"-"+r+"-"+cl+"-")
        f.close()