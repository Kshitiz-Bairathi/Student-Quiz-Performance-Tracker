from Menu import *
from Access import *
from Admin import *
from Student import *
import time

def Login_Page():
    print("Login Page")
    print(" ")

    print("1) Admin")
    print("2) Student")

    status = True
    while status:
        login_ch = int(input("Enter the designation from above (1 or 2): "))
        if login_ch in [1,2]:
            status = False
        else:
            print("Enter correct option")

    status = True

    while status:
        Username = input("Enter Username : ")
        Password = input("Enter Password : ")

        if login_ch == 1:
            Adm_access = Admin_Access(Username, Password)

            if Adm_access.Validation():
                status = False
            else:
                print("Incorrect Username or Password")

        else:
            Std_access = Student_Access(Username, Password)

            if Std_access.Validation():
                status = False
            else:
                print("Incorrect Username or Password")

    return Username,login_ch

def Admin_Page():
    Adm = Admin()
    status = True
    while status:
        ch = menu_Admin()

        if ch == 1:
            subject = menu_Subject()
            print(" ")
            print(f"The no. of Questions for Subject - {subject} is {Adm.GetTotalQA(subject)}")
            time.sleep(2)
            print(" ")
        
        elif ch == 2:
            subject = menu_Subject()
            print(" ")
            Adm.AddQA(subject)
            time.sleep(2)
            print(" ")
        
        elif ch == 3:
            subject = menu_Subject()
            print(" ")
            Adm.Result_Admin(subject)
            time.sleep(2)
            print(" ")
        
        elif ch == 4:
            subject = menu_Subject()
            print(" ")
            Adm.Delete_QA(subject)
            time.sleep(2)
            print(" ")
        
        elif ch == 5:
            status = False
        
        else:
            print("Enter Valid Choice")
            time.sleep(2)
    
    return

def Student_Page(Username):
    Std = Student(Username)
    status = True
    while status:
        ch = menu_Student()

        if ch == 1:
            subject = menu_Subject()
            print(" ")
            Std.GiveExam(subject)
            time.sleep(2)
            print(" ")
        
        elif ch == 2:
            subject = menu_Subject()
            print(" ")
            Std.Result_Student(subject)
            time.sleep(2)
            print(" ")
        
        elif ch == 3:
            status = False
        
        else:
            print("Enter Valid Choice")
            time.sleep(2)
    
    return