# -*- coding: utf-8 -*-
import tkinter as tk
import random

windowX = 800
windowY = 800

class Question:
    def __init__(self,questionText,trueOption,option2,option3,option4,answer=None):
        self.questionText = questionText
        self.optionTexts = [trueOption,option2,option3,option4]
        self.answer = answer
        self.trueOption = trueOption
    def checkIfTrue(self):
        if(self.answer == self.trueOption):
            return True
        else:
            return False
        
    def clearAnswer(self):
        self.answer = None


QuestionArray = []#

class ui:
    def __init__(self):
        self.quizStarted = False
        self.mainwindow = tk.Tk()
        self.mainwindow.geometry("{}x{}+{}+{}".format(windowX,windowY,
                                 int((self.mainwindow.winfo_screenwidth()/2)-(windowX/2)),
                                 int(self.mainwindow.winfo_screenheight()/2-(windowY/2))))
        
        self.leftFrame = tk.Frame(self.mainwindow)
        self.leftFrame.place(x=0,y=0,height=800,width=600)
        
        self.v = tk.StringVar(self.leftFrame,"1")
        
        self.rightFrame = tk.Frame(self.mainwindow)
        self.rightFrame.place(x=600,y=0,height=800,width=200)
        
        self.QuestList = tk.Listbox(self.rightFrame)
        self.QuestList.bind('<<ListboxSelect>>', self.questListSelected)
        self.QuestList.place(x=0,y=0,width=200,height=800)
        
        
        self.loginScreen()
        
        self.mainwindow.mainloop()        
        
    def clearLeftFrame(self):
        for widget in self.leftFrame.winfo_children():
            widget.destroy()
            
            
    def clearRightFrame(self):
        self.QuestList.delete(0, "end")
        
    def removeQuestion(self,idx):
        QuestionArray.pop(idx)
        
    def questListSelected(self,evt):
        
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        
        if(not self.quizStarted):
            self.previewQuestion(index)
        else:
            self.answerQuestionScreen(index)
            
            
    def previewQuestion(self,index):
        self.clearLeftFrame()
        tk.Label(self.leftFrame,text=QuestionArray[index].questionText).place(x=100,y=50,width = 400, height = 300)
        tk.Label(self.leftFrame,text="Doğru cevap:"+QuestionArray[index].optionTexts[0]).place(x=100,y=400,width=400,height=50)
        tk.Label(self.leftFrame,text=QuestionArray[index].optionTexts[1]).place(x=100,y=480,width=400,height=50)
        tk.Label(self.leftFrame,text=QuestionArray[index].optionTexts[2]).place(x=100,y=550,width=400,height=50)
        tk.Label(self.leftFrame,text=QuestionArray[index].optionTexts[3]).place(x=100,y=630,width=400,height=50)
        
        btn = tk.Button(self.leftFrame,text="Soruyu sil",command = lambda:[self.removeQuestion(index),self.updateRightBuffer(),self.clearLeftFrame(),self.loginScreen()])
        btn.place(x=170,y=700,width=100,height=50)
        
        btn2 = tk.Button(self.leftFrame,text="Geri",command = lambda:[self.clearLeftFrame(),self.loginScreen()])
        btn2.place(x=320,y=700,width=100,height=50)
        
    def loginScreen(self):
        lecturerButton = tk.Button(self.leftFrame,text="Öğretmen Olarak Giriş Yap",command = self.questingAddScreen)
        lecturerButton.place(x=200,y=300,width=200,height=50)
                
        studentButton = tk.Button(self.leftFrame,text="Öğrenci Olarak Giriş Yap",command=self.studentScreen)
        studentButton.place(x=200,y=400,width=200,height=50)


    def questingAddScreen(self):
        self.clearLeftFrame()
        self.questionTextBox = tk.Text(self.leftFrame)
        self.questionTextBox.place(x=100,y=50,width = 400, height = 300)
        
        
        self.correctAnswerBox = tk.Text(self.leftFrame)
        self.correctAnswerBox.place(x=100,y=400,width=400,height=50)
        
        self.optionB = tk.Text(self.leftFrame)
        self.optionB.place(x=100,y=480,width=400,height=50)
        
        self.optionC = tk.Text(self.leftFrame)
        self.optionC.place(x=100,y=550,width=400,height=50)
        
        self.optionD = tk.Text(self.leftFrame)
        self.optionD.place(x=100,y=630,width=400,height=50)
        
        
        tk.Label(self.leftFrame,text="Soru metnini giriniz.",justify="center").place(x=0,y=20,width=600,height=25)
        tk.Label(self.leftFrame,text="A şıkkını giriniz.",justify="center").place(x=0,y=377,width=600,height=25)
        tk.Label(self.leftFrame,text="B şıkkını giriniz.",justify="center").place(x=0,y=457,width=600,height=25)
        tk.Label(self.leftFrame,text="C şıkkını giriniz.",justify="center").place(x=0,y=527,width=600,height=25)
        tk.Label(self.leftFrame,text="D şıkkını giriniz.",justify="center").place(x=0,y=607,width=600,height=25)
        
        self.addButton = tk.Button(self.leftFrame,text="Soruyu ekle",command=self.addQ)
        self.addButton.place(x=170,y=700,width=100,height=50)
        
        self.backButton = tk.Button(self.leftFrame,text="Geri",command= lambda:[self.clearLeftFrame(),self.loginScreen()])
        self.backButton.place(x=320,y=700,width=100,height=50)
        
    def updateRightBuffer(self):
        self.clearRightFrame()
        for i in range(len(QuestionArray),0,-1):
            self.QuestList.insert(0,"Soru "+str(i))
        
        if(self.quizStarted):
            for i in range(len(QuestionArray)):
                if(QuestionArray[i].answer != None):
                    self.QuestList.itemconfig(i,{"bg":"yellow"})
        
            
    def addQ(self):
        
        text = self.questionTextBox.get("1.0","end")
        correctAnswer = self.correctAnswerBox.get("1.0","end")
        optionB = self.optionB.get("1.0","end")
        optionC = self.optionC.get("1.0","end")
        optionD = self.optionD.get("1.0","end")

        if(len(text) < 2 or len(correctAnswer) < 2 or len(optionB) < 2 or len(optionC) < 2 or len(optionD) < 2 ):
            
            tk.messagebox.showerror(title="Eksik form", message="Lütfen bütün boşlukları doldurunuz")
            return
        
        QuestionArray.append(Question(text,correctAnswer,optionB,optionC,optionD))
        
        self.updateRightBuffer()
        
        self.questionTextBox.delete("1.0","end")
        self.correctAnswerBox.delete("1.0","end")
        self.optionB.delete("1.0","end")
        self.optionC.delete("1.0","end")
        self.optionD.delete("1.0","end")
        
    def studentScreen(self):
        self.clearLeftFrame()
        tk.Button(self.leftFrame,text="Quizi Başlat",command=self.startQuiz).place(x=200,y=300,width=200,height=50)
        tk.Button(self.leftFrame,text="Geri",command=lambda:[self.clearLeftFrame(),self.loginScreen()]).place(x=200,y=400,width=200,height=50)
        
    def startQuiz(self):
        self.clearLeftFrame()
        self.quizStarted = True
        self.answerQuestionScreen(0)
    
    
    
    def answerQuestionScreen(self,idx):
        self.clearLeftFrame()
        
        
        
        tk.Label(self.leftFrame,text=QuestionArray[idx].questionText).place(x=100,y=50,width = 400, height = 300)
        
        values = {QuestionArray[idx].optionTexts[0]:QuestionArray[idx].optionTexts[0],
                  QuestionArray[idx].optionTexts[1]:QuestionArray[idx].optionTexts[1],
                  QuestionArray[idx].optionTexts[2]:QuestionArray[idx].optionTexts[2],
                  QuestionArray[idx].optionTexts[3]:QuestionArray[idx].optionTexts[3]}
        
        
        l = list(values.items())
        random.shuffle(l)
        values = dict(l)
        
        cnt = 0
        for (text, value) in values.items():
            btn = tk.Radiobutton(self.leftFrame, text = text, variable = self.v,
                value = value)
            btn.place(x=100,y=400+(cnt*80),width=400,height=50)
            cnt += 1
        
        btn = tk.Button(self.leftFrame,text="Cevabı kaydet",command=lambda:self.saveAnswer(idx))
        btn.place(x=250,y=700,width=100,height=50)
        
        btn2 = tk.Button(self.leftFrame,text="Sıradaki soru",command=lambda:self.answerQuestionScreen(idx+1))
        btn2.place(x=400,y=700,width=100,height=50)
        
        btn3 = tk.Button(self.leftFrame,text="Sınavı bitir",command=lambda:self.finishExam())
        btn3.place(x=100,y=700,width=100,height=50)
    
    def finishExam(self):
        self.clearRightFrame()
        for i in range(len(QuestionArray),0,-1):
            self.QuestList.insert(0,"Soru "+str(i))
        
        correctCount = 0
        wrongCount = 0
        emptyCount = 0
        for i in range(len(QuestionArray)):
            if(QuestionArray[i].answer == None):
                self.QuestList.itemconfig(i,{"bg":"yellow"})
                emptyCount += 1
            elif(QuestionArray[i].checkIfTrue()):
                self.QuestList.itemconfig(i,{"bg":"green"})
                correctCount += 1
            else:
                self.QuestList.itemconfig(i,{"bg":"red"})
                wrongCount += 1
        
        self.clearLeftFrame()
        tk.Label(self.leftFrame,text="Doğru cevap sayısı:"+str(correctCount),justify="center").place(x=0,y=100,width=600,height=25)
        tk.Label(self.leftFrame,text="Yanlış cevap sayısı:"+str(wrongCount),justify="center").place(x=0,y=200,width=600,height=25)
        tk.Label(self.leftFrame,text="Boş soru sayısı:"+str(emptyCount),justify="center").place(x=0,y=300,width=600,height=25)
        
        btn2 = tk.Button(self.leftFrame,text="Ana Ekrana Dön",command=lambda:self.resetQuiz())
        btn2.place(x=250,y=500,width=100,height=50)
    
    def resetQuiz(self):
        [i.clearAnswer() for i in QuestionArray]
        self.clearLeftFrame()
        self.quizStarted = False
        self.loginScreen()
        self.updateRightBuffer()
        
        
    def saveAnswer(self,idx):
        QuestionArray[idx].answer = self.v.get()
        self.updateRightBuffer()
        
    
        
        
        
        
ui()