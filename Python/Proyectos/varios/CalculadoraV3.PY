from tkinter import *
from tkinter import messagebox

 
class Pycalc(Frame):
 
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()
 
    def deleteLastCharacter(self):
        textLength = len(self.display.get())
 
        if textLength >= 1:
            self.display.delete(textLength - 1, END)
        if textLength == 1:
            self.replaceText("0")
 
    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)
 
    def append(self, text):
        actualText = self.display.get()
        textLength = len(actualText)
        if actualText == "0":
            self.replaceText(text)
        else:
            self.display.insert(textLength, text)
 
    def evaluate(self):
        try:
            self.replaceText(eval(self.display.get()))
        except (SyntaxError, AttributeError):
            messagebox.showerror("Error", "Syntax Error")
            self.replaceText("0")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot Divide by 0")
            self.replaceText("0")
 
    def containsSigns(self):
        operatorList = ["*", "/", "+", "-"]
        display = self.display.get()
        for c in display:
            if c in operatorList:
                 return True
        return False
 
    def changeSign(self):
        if self.containsSigns():
            self.evaluate()
        firstChar = self.display.get()[0]
        if firstChar == "0":
            pass
        elif firstChar == "-":
            self.display.delete(0)
        else:
            self.display.insert(0, "-")
 
    def inverse(self):
        self.display.insert(0, "1/(")
        self.append(")")
        self.evaluate()
 
    def createWidgets(self):
        self.display = Entry(self, font=("Arial", 24), relief=RAISED, justify=RIGHT, bg='#515151', fg='white', borderwidth=0)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew" , padx=5,pady=5)
 
        self.ceButton = Button(self, font=("Arial", 15), fg='black', bg='#9B9A9A', text="CE", highlightbackground='grey', command=lambda: self.replaceText("0"),width=6,height=2)
        self.ceButton.grid(row=1, column=0, sticky="nsew" ,padx=5,pady=5)
        self.inverseButton = Button(self, font=("Arial", 15), fg='black', bg='#9B9A9A', text="1/x", highlightbackground='grey', command=lambda: self.inverse(),width=6,height=2)
        self.inverseButton.grid(row=1, column=2, sticky="nsew" ,padx=5,pady=5)
        self.delButton = Button(self, font=("Arial", 15), fg='black', bg='#9B9A9A', text="Del", highlightbackground='grey', command=lambda: self.deleteLastCharacter(),width=6,height=2)
        self.delButton.grid(row=1, column=1, sticky="nsew" ,padx=5,pady=5)
        self.divButton = Button(self, font=("Arial", 15), fg='white', bg='#FFC300', text="/", highlightbackground='grey', command=lambda: self.append("/"),width=6,height=2)
        self.divButton.grid(row=1, column=3, sticky="nsew" ,padx=5,pady=5)
 
        self.sevenButton = Button(self, font=("Arial", 15), fg='white', bg='#515151', text="7", highlightbackground='grey', command=lambda: self.append("7"),width=6,height=2)
        self.sevenButton.grid(row=2, column=0, sticky="nsew" ,padx=5,pady=5)
        self.eightButton = Button(self, font=("Arial", 15), fg='white', bg='#515151', text="8", highlightbackground='grey', command=lambda: self.append("8"),width=6,height=2)
        self.eightButton.grid(row=2, column=1, sticky="nsew" ,padx=5,pady=5)
        self.nineButton = Button(self, font=("Arial", 15), fg='white', bg='#515151', text="9", highlightbackground='grey', command=lambda: self.append("9"),width=6,height=2)
        self.nineButton.grid(row=2, column=2, sticky="nsew",padx=5,pady=5)
        self.multButton = Button(self, font=("Arial", 15), fg='white', bg='#FFC300', text="*", highlightbackground='grey', command=lambda: self.append("*"),width=6,height=2)
        self.multButton.grid(row=2, column=3, sticky="nsew",padx=5,pady=5)
 
        self.fourButton = Button(self, font=("Arial", 15), fg='white', bg='#515151',text="4", highlightbackground='grey', command=lambda: self.append("4"),width=6,height=2)
        self.fourButton.grid(row=3, column=0, sticky="nsew",padx=5,pady=5)
        self.fiveButton = Button(self, font=("Arial", 15), fg='white', bg='#515151', text="5", highlightbackground='grey', command=lambda: self.append("5"),width=6,height=2)
        self.fiveButton.grid(row=3, column=1, sticky="nsew",padx=5,pady=5)
        self.sixButton = Button(self, font=("Arial", 15), fg='white', bg='#515151', text="6", highlightbackground='grey', command=lambda: self.append("6"),width=6,height=2)
        self.sixButton.grid(row=3, column=2, sticky="nsew",padx=5,pady=5)
        self.minusButton = Button(self, font=("Arial", 15), fg='white', bg='#FFC300', text="-", highlightbackground='grey', command=lambda: self.append("-"),width=6,height=2)
        self.minusButton.grid(row=3, column=3, sticky="nsew",padx=5,pady=5)
 
        self.oneButton = Button(self, font=("Arial", 15), fg='white', bg='#515151', text="1", highlightbackground='grey', command=lambda: self.append("1"),width=6,height=2)
        self.oneButton.grid(row=4, column=0, sticky="nsew",padx=5,pady=5)
        self.twoButton = Button(self, font=("Arial", 15), fg='white', bg='#515151',  text="2", highlightbackground='grey', command=lambda: self.append("2"),width=6,height=2)
        self.twoButton.grid(row=4, column=1, sticky="nsew",padx=5,pady=5)
        self.threeButton = Button(self, font=("Arial", 15), fg='white', bg='#515151', text="3", highlightbackground='grey', command=lambda: self.append("3"),width=6,height=2)
        self.threeButton.grid(row=4, column=2, sticky="nsew",padx=5,pady=5)
        self.plusButton = Button(self, font=("Arial", 15), fg='white', bg='#FFC300', text="+", highlightbackground='grey', command=lambda: self.append("+"),width=6,height=2)
        self.plusButton.grid(row=4, column=3, sticky="nsew",padx=5,pady=5)
 
        self.negToggleButton = Button(self, font=("Arial", 15), fg='black', bg='#9B9A9A', text="+/-", highlightbackground='grey', command=lambda: self.changeSign(),width=6,height=2)
        self.negToggleButton.grid(row=5, column=0, sticky="nsew",padx=5,pady=5)
        self.zeroButton = Button(self, font=("Arial", 15), fg='white',bg='#515151', text="0", highlightbackground='grey', command=lambda: self.append("0"),width=6,height=2)
        self.zeroButton.grid(row=5, column=1, sticky="nsew",padx=5,pady=5)
        self.decimalButton = Button(self, font=("Arial", 15), fg='white', bg='#515151', text=".", highlightbackground='grey', command=lambda: self.append("."),width=6,height=2)
        self.decimalButton.grid(row=5, column=2, sticky="nsew",padx=5,pady=5)
        self.equalsButton = Button(self, font=("Arial", 15), fg='white', bg='#FFC300', text="=", highlightbackground='grey', command=lambda: self.evaluate(),width=6,height=2)
        self.equalsButton.grid(row=5, column=3, sticky="nsew",padx=5,pady=5)
 

Calculator = Tk()
Calculator.title("Calculadora")
Calculator.resizable(0,0)

Calculator.config(cursor="hand2")
root = Pycalc(Calculator).grid(padx=5,pady=5)
Calculator.mainloop()