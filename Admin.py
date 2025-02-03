import pandas as pd
import numpy
import matplotlib.pyplot as plt

class Admin:
    def __init__(self):
        data=pd.read_csv('Questionbank.csv')
        self.df=pd.DataFrame(data)

    def GetTotalQA(self,subject):
        column = subject + 'que'
        return self.df[column].count()
    
    def swap(s1, s2):
        return s2, s1

    def AddQA(self,subject):
        que=input('Enter question : ')
        op1=input('Enter option 1 : ')
        op2=input('Enter option 2 : ')
        op3=input('Enter option 3 : ')
        op4=input('Enter option 4 : ')
        status=True
        while status:
            ch=input('Which option is correct answer (Enter only 1 or 2 or 3 or 4) : ')
            if ch>='1' and ch<='4':
                status=False
            else:
                print('Enter only 1 or 2 or 3 or 4 . . . :')
                
        if ch=='1':
            ans=op1
        elif ch=='2':
            ans=op2
        elif ch=='3':
            ans=op3
        elif ch=='4':
            ans=op4
        self.df.loc[self.GetTotalQA(subject),[(subject+'que'),(subject+'1'),(subject+'2'),(subject+'3'),(subject+'4'),(subject+'ans')]]=[que,op1,op2,op3,op4,ans]
        self.Data_Frame = self.df.loc[:,'Physicsque':]
        self.Data_Frame.to_csv('Questionbank.csv')

        print("Question added successfully")

        return
    
    def Result_Admin(self,subject):
        name=input('Enter the name of student to check the progress: ')
        name=name.upper()
        name_result=name+subject
        if name_result in self.df.columns:
            scores = self.df[name_result].dropna()
            Exam_count = self.df[name_result].count()
            x_index = list(range(1,Exam_count+1))
            plt.plot(x_index,scores,marker='o',markersize=5,linewidth=2)
            plt.ylabel('Percentage scored')
            plt.title('Performance Report')
            plt.xticks(x_index)
            plt.show()
        else :
            print('No data')
        
        return
    
    def swap(self,df,row1,row2):
        df.iloc[row1], df.iloc[row2] = df.iloc[row2].copy(), df.iloc[row1].copy()
        return df
    
    def Delete_QA(self, subject):
        print(self.df[subject+'que'])

        que_ID = int(input("Enter the ID of the Question to be Deleted: "))
        total_que = self.df[subject+'que'].count()

        status = True
        while status:
            if(que_ID >=0 and que_ID < self.df[subject+'que'].count()):
                self.df.loc[:,(subject+'que'):(subject+'ans')] = self.swap(self.df.loc[:,(subject+'que'):(subject+'ans')], total_que-1, que_ID)
                status = False
            else:
                print("Invalid Question ID")
        
        self.df.loc[total_que-1, 'Physicsque':'Physicsans'] = numpy.nan

        self.Data_Frame = self.df.loc[:,'Physicsque':]
        self.Data_Frame.to_csv('Questionbank.csv')
        
        print("The Question has been Successfully Deleted")

        return
    
    