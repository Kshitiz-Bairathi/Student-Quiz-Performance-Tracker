import pandas as pd
import matplotlib.pyplot as plt
import random

class Student:
    def __init__(self, name):
        data=pd.read_csv('Questionbank.csv')
        self.df=pd.DataFrame(data)

        self.name = name
    
    def GetTotalQA(self,subject):
        column = subject + 'que'
        return self.df[column].count()
    
    def GiveExam(self, subject):
        self.name=self.name.upper()

        nameSubject = self.name+subject
        if (nameSubject not in self.df.columns):
            self.df[nameSubject] = pd.Series([None] * len(self.df))
        
        dicSubject={'correct':0, 'wrong':0}
        status=True
        while status:
            print("No. of Questions Available = ", self.GetTotalQA(subject))
            noq=int(input('How many QA you want in your online exam ? '))
            if noq>=0 and noq<=self.df[subject+"que"].count():
                status=False
            else:
                print('Sorry! not enough QA available in database . . . Choose less QA')
        
        question_no_list = random.sample(range(self.df[subject + "que"].count()), noq)
        
        for i in question_no_list:
            print('Question:', self.df.loc[i, subject + "que"])
            print('A.', self.df.loc[i, subject + "1"],
              '\nB.', self.df.loc[i, subject + "2"],
              '\nC.', self.df.loc[i, subject + "3"],
              '\nD.', self.df.loc[i, subject + "4"])
            status=True
            while status:
                choice=input('Enter your answer : ')
                choice=choice.upper()
                if choice in 'ABCD':
                    status=False
                else:
                    print('Please enter only given options (A,B,C,D) ')

            if choice=='A':
                ans=self.df.loc[i,subject+"1"]
            elif choice=='B':
                ans=self.df.loc[i,subject+"2"]
            elif choice=='C':
                ans=self.df.loc[i,subject+"3"]
            elif choice=='D':
                ans=self.df.loc[i,subject+"4"]

            if ans==self.df.loc[i,subject+"ans"]:
                print('>>>>>>>> Correct Answer <<<<<<<<<<')
                print('')
                dicSubject['correct']+=1
            else:
                print('>>>>>>>> Wrong Answer <<<<<<<<<<')
                print('Correct Answer is :',self.df.loc[i,subject+"ans"])
                print('')
                dicSubject['wrong']+=1

        print('Result Analysis : ',dicSubject)
        plt.bar(['correct','wrong'],[dicSubject['correct'], dicSubject['wrong']],width=0.6)
        plt.title('Result Analysis')
        plt.xlabel('Particulars')
        plt.ylabel('No of answers')
        plt.show()
        
        self.df.loc[self.df[nameSubject].count(), nameSubject] = (dicSubject['correct']/noq)*100

        self.Data_Frame = self.df.loc[:,'Physicsque':]
        self.Data_Frame.to_csv('Questionbank.csv')

        return
    
    def Result_Student(self,subject):
        name_result=self.name+subject
        if name_result in self.df.columns:
            scores = self.df[name_result].dropna()
            Exam_count = self.df[name_result].count()
            x_index = list(range(1,Exam_count+1))
            plt.plot(x_index,scores,marker='o',markersize=5,linewidth=2)
            plt.ylabel('Percentage scored')
            plt.title('Performance Report')
            plt.show()
        else :
            print('No data')
        
        return