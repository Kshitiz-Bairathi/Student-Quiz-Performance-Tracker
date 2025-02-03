from abc import ABC,abstractmethod
import pandas as pd
import numpy as np

class Access(ABC):
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password
    
    @abstractmethod
    def Validation(self):
        pass

class Admin_Access(Access):
    __Admin_Username = "Kshitiz"
    __Admin_Password = "Bairathi"

    def __init__(self, Username, Password):
        super().__init__(Username, Password)
    
    def Validation(self):
        if self.Username == self.__Admin_Username and self.Password == self.__Admin_Password:
            return True
        else:
            return False
        
class Student_Access(Access):
    Data = pd.read_csv('Student_Login_Data.csv')
    Student_Login_Data = np.array(Data)

    def __init__(self, Username, Password):
        super().__init__(Username, Password)
    
    def Validation(self):
        key = self.Username +'_'+ self.Password
            
        if key in self.Student_Login_Data:
            return True
        else:
            return False