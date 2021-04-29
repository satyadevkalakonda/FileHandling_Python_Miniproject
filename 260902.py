import os


class Add:

    # Class for Adding the student Record

    def addrecord(self):
        print("\n Enter students details\n")
        f = open("student.txt", "r")
        n = input("Enter Name= \n")
        r = input("Enter Rollno= \n")
        flag=0
        while (True):
            t = f.readline()
            l = len(t)
            if (l == 0):
                break
            g = t.split('-')
            if (g[1] == r):
                print("Roll no already exists")
                flag=1
        if(flag==1):
            quit()
        f.close()
        cl = input("Enter class= \n")
        fn = input("Enter Father name= \n")
        mn = input("Enter the Mother Name= \n")
        f = open("student.txt", "a")
        f.write(n + "-" + r + "-" + cl + "-" + fn + "-" + mn + "\n")
        print("Successfully added the record")
        f.close()



class Print_R:
    # Class for Printing the Student Records
    def printrecord(self):
        print("\n --- Displaying ALL Records----\n")
        f = open("student.txt", "r")
        while (True):
            d = f.readline()
            l = len(d)
            if (l == 0):
                break
            print(d.strip())



class Search_n:
    # Class For Searching Student Record with name
    def searchname(self):
        print("\n 3. Enter student name to search")
        search = input()
        f = open("student.txt", "r")
        flag=0
        while(True):
            t = f.readline()
            l = len(t)
            if (l == 0):
                break
            g = t.split('-')
            if (g[0] == search):
                print("\n --- Record Found----\n")
                print("Name is", g[0])
                print("Roll no is", g[1])
                print("class is ", g[2])
                print("Father name is", g[3])
                print("Mother name is", g[4])
                flag=1
                break

        if(flag==0):
            print("Record Not Found")
        f.close()

class Search_r:
    #  class for searching the student record using rollno
    def searchrollno(self):
        print("Enter Student Roll No To Search : \n")
        search = input()
        f = open("student.txt", "r")
        flag = 0
        while(True):
            t = f.readline()
            l = len(t)
            if (l == 0):
                break
            g = t.split('-')
            if (g[1] == search):
                print("\n --- Record Found---\n")
                print("Name is", g[0])
                print("Roll no is", g[1])
                print("class is ", g[2])
                print("Father name is", g[3])
                print("Mother name is", g[4])
                flag=1
                break
        if(flag==0):
            print("Record Not Found")


class Delete_r:
    # Class for Deleting the student Record

    def deleterecord(self):
        search = input("Enter Student name to delete=\n")
        f = open("student.txt", "r")
        tt = open("temp.txt", "w+")
        h = 0
        flag = 0
        while (True):
            t = f.readline()
            l = len(t)
            if (l == 0):
                break
            g = t.split('-')
            if (g[0] != search):
                tt.write(t)
            if (g[0] == search):
                h = 1
        f.close()
        tt.close()
        if (h == 1):
            print("Record Deleted Successfully")
            os.remove("student.txt")
            os.rename("temp.txt", "student.txt")
        elif (h == 0):
            print("Record Not Found!! Deletion unsuccessful")

class Update_r:
    # Class for updating the student Record
    def updaterecord(self):
        h = 0
        search = input("Enter Student Name to update record=\n")
        f = open("student.txt", "r")
        tt = open("temp.txt", "w+")
        flag = 0
        while (True):
            t = f.readline()
            l = len(t)
            if (l == 0):
                break
            g = t.split('-')
            if (g[0] == search):
                print("Current Details is : \n", t)
                print("Format : Name-Rollno-Class-Fathername-Mothername\n")
                print("-----------------------")
                newroll = input("Update the Roll no / Press Enter to Continue=\n")
                newclass = input("Update the Class / Press Enter to Continue=\n")
                fathername = input("Update the Father Name / Press Enter to Continue=\n")
                mothername = input("Update the Mother Name / Press Enter to Continue=\n")
                if (len(newroll) == 0):
                    newroll = g[1]
                if (len(newclass) == 0):
                    newclass = g[2]
                if (len(fathername) == 0):
                    fathername = g[3]
                if (len(mothername) == 0):
                    mothername = g[4]
                tt.write("\n" + g[0] + "-" + newroll + "-" + newclass + "-" + fathername + "-" + mothername)
                h = 1
            else:
                tt.write(t)
        f.close()
        tt.close()
        if (h == 1):
            print("Record Updated Successfully")
            os.remove("student.txt")
            os.rename("temp.txt", "student.txt")
        elif (h == 0):
            print("No Record Exist: for updation process")

def exitt():
    print("Thank you For using the application Bye!...")
    quit()

def main():
    while(True):
        print("\n--------- Welcome to Student Managment System-----------\n")
        print("1. Add Student Record\n")
        print("2. Display Record\n")
        print("3. Search Record Using Name\n")
        print("4. Search Record Using Rollno\n")
        print("5. Update The Record\n")
        print("6. Delete The Record\n")
        print("7. Exit")
        print("\n----------------------------------------------------------\n")
        n=int(input("Enter the choice:\n"))
        if(n==1):
            a1=Add()
            a1.addrecord()
        elif(n==2):
           p1=Print_R()
           p1.printrecord()
        elif(n==3):
            s1=Search_n()
            s1.searchname()
        elif(n==4):
            s2=Search_r()
            s2.searchrollno()
        elif(n==5):
            u1=Update_r()
            u1.updaterecord()
        elif(n==6):
            d1=Delete_r()
            d1.deleterecord()
        elif(n==7):
            exitt()
        else:
            print("Wrong choice")
            exitt()



if __name__ == "__main__":
        main()