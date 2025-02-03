from Page import *

Username, login_ch = Login_Page()

if login_ch == 1:
    Admin_Page()
else:
    Student_Page(Username)
