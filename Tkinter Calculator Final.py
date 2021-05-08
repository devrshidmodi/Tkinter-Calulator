#Devrshi Modi
#April 30,2019
#This program will output a fully functional calculator.



from tkinter import *                                         #Importing everything from tkinter module.
from math import *                                            #Importing everything from math module.


calculator= Tk()
calculator.title("Calculator")



class Application(Frame):                                     #The frame is defined  as a class.
 def __init__(self,master):                                   #__init__ initializes the attributes of the class
      Frame.__init__(self,master)                             #Calls Frame to act as an object
      self.Buttons()                                          #The Buttons function created here.

 def Buttons(self):
  #Function that defines the buttons of the calculator.

  self.display=Entry(self,font =("Calibri",20),justify=RIGHT) #Sets the input to the right side of the calculator display.
  self.display.insert(0,"0")                                  #Inserts zero initially to the right side of the calculator display.
  self.display.grid(row=0,column=0,columnspan=100)            #Calculator Display is defined as being at the first row and first column of the application. The columnspan allows the buttons to not be compressed.          

  #Row 1 of Buttons:

  self.sevenButton=Button(self,font=("Calibri",12),bg="#ad1aaa",width =6,height=2,text="7",borderwidth=7,command=lambda:self.showondisplay("7")).grid(row=1,column=0)             #Number 7 Button
  self.eightButton=Button(self,font=("Calibri",12),bg="#ad1aaa",width =6,height=2,text="8",borderwidth=7,command=lambda:self.showondisplay("8")).grid(row=1,column=1)             #Number 8 Button
  self.nine=Button(self,font=("Calibri",12),bg="#ad1aaa",width =6,height=2,text="9",borderwidth=7,command=lambda:self.showondisplay("9")).grid(row=1,column=2)                    #Number 9 Button
  self.multiplyButton=Button(self,font=("Calibri",12),bg="#26c6c9",width =6,height=2,text="*",borderwidth=7,command=lambda:self.showondisplay("*")).grid(row=1,column=3)          #Multiplication Operation Button

  #Row 2 of Buttons:

  self.fourButton=Button(self,font=("Calibri",12),bg="#ad1aaa",width =6,height=2,text="4",borderwidth=7,command=lambda:self.showondisplay("4")).grid(row=2,column=0)              #Number 4 Button
  self.fiveButton=Button(self,font=("Calibri",12),bg="#ad1aaa",width =6,height=2,text="5",borderwidth=7,command=lambda:self.showondisplay("5")).grid(row=2,column=1)              #Number 5 Button
  self.sixButton=Button(self,font=("Calibri",12),bg="#ad1aaa",width =6,height=2,text="6",borderwidth=7,command=lambda:self.showondisplay("6")).grid(row=2,column=2)               #Number 6 Button
  self.subtractButton=Button(self,font=("Calibri",12),bg="#26c6c9",width =6,height=2,text="-",borderwidth=7,command=lambda:self.showondisplay("-")).grid(row=2,column=3)          #Subtraction Operation Button

  #Row 3 of Buttons:

  self.oneButton=Button(self,font=("Calibri",12),bg="#ad1aaa",width =6,height=2,text="1",borderwidth=7,command=lambda:self.showondisplay("1")).grid(row=3,column=0)               #Number 1 Button
  self.twoButton=Button(self,font=("Calibri",12),bg="#ad1aaa",width =6,height=2,text="2",borderwidth=7,command=lambda:self.showondisplay("2")).grid(row=3,column=1)               #Number 2 Button
  self.threeButton=Button(self,font=("Calibri",12),bg="#ad1aaa",width =6,height=2,text="3",borderwidth=7,command=lambda:self.showondisplay("3")).grid(row=3,column=2)             #Number 3 Button
  self.addButton=Button(self,font=("Calibri",12),bg="#26c6c9",width =6,height=2,text="+",borderwidth=7,command=lambda:self.showondisplay("+")).grid(row=3,column=3)               #Addition Operation Button     

  #Row 4 of Buttons:

  self.clearButton=Button(self,font=("Calibri",12),bg="#9fd613",width =6,height=2,text="C",borderwidth=7,command=lambda:self.clearText("C")).grid(row=4,column=0)                 #Clear Button
  self.zeroButton=Button(self,font=("Calibri",12),bg="#ad1aaa",width =6,height=2,text="0",borderwidth=7,command=lambda:self.showondisplay("0")).grid(row=4,column=1)              #Number 0 Button     
  self.equalButton=Button(self,font=("Calibri",12),bg="#d6128e",width =6,height=2,text="=",borderwidth=7,command=lambda:self.calculateInput()).grid(row=4,column=2)          #Equal Sign - SYMBOL FOR CALCULATING EXPRESSION!
  self.divideButton=Button(self,font=("Calibri",12),bg="#26c6c9",width =6,height=2,text="/",borderwidth=7,command=lambda:self.showondisplay("/")).grid(row=4,column=3)            #Division Operation Button

  #Row 5 of Buttons:

  self.bracketoneButton=Button(self,font=("Calibri",12),bg="#c6850b",width =6,height=2,text="(",borderwidth=7,command=lambda:self.showondisplay("(")).grid(row=5,column=0)        #Left Bracket Button 
  self.brackettwoButton= Button(self,font=("Calibri",12),bg="#c6850b",width =6,height=2,text=")",borderwidth=7,command=lambda:self.showondisplay(")")).grid(row=5,column=1)       #Right Bracket Button
  self.sinButton=Button(self,font=("Calibri",12),bg="#22bf6e",width =6,height=2,text=("sin(x)"),borderwidth=7,command=lambda:self.showondisplay("sin")).grid(row=5,column=2)      #Sin Function Button(Takes user input as radians)
  self.cosButton=Button(self,font=("Calibri",12),bg="#22bf6e",width =6,height=2,text=("cos(x)"),borderwidth=7,command=lambda:self.showondisplay("cos")).grid(row=5,column=3)      #Cos Function Button(Takes user input as radians)     

  #Row 6 of Buttons:

  self.tanButton=Button(self,font=("Calibri",12),bg="#22bf6e",width =6,height=2,text=("tan(x)"),borderwidth=7,command=lambda:self.showondisplay("tan")).grid(row=6,column=0)      #Tan Function Button(Takes user input as radians)
  self.asinButton=Button(self,font=("Calibri",12),bg="#d6300e",width =6,height=2,text=("arcsin"),borderwidth=7,command=lambda:self.showondisplay("asin")).grid(row=6,column=1)    #Inverse Sin Function Button(Displays radians on screen)
  self.acosButton=Button(self,font=("Calibri",12),bg="#d6300e",width =6,height=2,text=("arccos"),borderwidth=7,command=lambda:self.showondisplay("acos")).grid(row=6,column=2)    #Inverse Cos Function Button(Displays radians on screen)
  self.atanButton=Button(self,font=("Calibri",12),bg="#d6300e",width =6,height=2,text=("arctan"),borderwidth=7,command=lambda:self.showondisplay("atan")).grid(row=6,column=3)    #Inverse Tan Function Button(Displays radians on screen)
  
  #Row 7 of Buttons:

  self.dotButton=Button(self,font=("Calibri",12),bg="#ad1aaa",width=6,height=2,text=".",borderwidth=7,command=lambda:self.showondisplay(".")).grid(row=7,column=0)                #Decimal Button Operation Button(Mathematical Constant)
  self.exponentButton= Button(self,font=("Calibri",12),bg="#2297c1",width =6,height=2,text=("x^"),borderwidth=7,command=lambda:self.showondisplay("**")).grid(row=7,column=1)     #Exponent Operation Button
  self.squarerootButton= Button(self,font=("Calibri",12),bg="#2297c1",width =6,height=2,text=("√"),borderwidth=7,command=lambda:self.showondisplay("sqrt")).grid(row=7,column=2)  #Square root Operation Button
  self.piButton= Button(self,font=("Calibri",12),bg="#2297c1",width =6,height=2,text=("π"),borderwidth=7,command=lambda:self.showondisplay("pi")).grid(row=7,column=3)  #Log Base 10 Operation Button

 def replaceText(self,text):
     #Function for letting users re-enter values on screen
        self.display.delete(0,END)                            #Allows to replace current text before entering next text.
        self.display.insert(0,text)                           #Allows user to insert new text.                         

 def showondisplay(self,text):
     #Function for showing user input on screen.
        self.entryText=self.display.get()                     #Gets all the text from the user input
        self.textLength=len(self.entryText)                   #Sets textLength equal to the length of the entryText so it can be properly shown on the display.  
        if self.entryText == "0":
            self.replaceText(text)                            #If the entryText is 0, it keeps  0 on the display.
        else:
            self.display.insert(self.textLength,text)         #Inserts the user input onto the screen display

 def calculateInput(self):
     #Function for calculating user input                     #Creates a function to calculate the expression displayeed on the screen
        self.entryText=self.display.get()                     #Assigns the user input to the tkinter command entryText.

        try:                                                  #Tries to execute the instructions below

         self.result=eval(self.entryText)                     #Evaluates the entry text that the user has inputed. CALCULATION ALGORITHM!!
         self.replaceText(self.result)                        #Assigns the user input to the tkinter command entryText.

        except SyntaxError as o:                              #If the instructions cannot be executed, this will display on the screen.
         self.replaceText("Invalid Input")                    #If there is an invalid input by the user,it displays "Invalid Input" on the calculator display.
            

        

 def clearText(self,master):                                  #Clears text when C button is clicked .                   
     #Function for clearing the calculator display when the "C" button is pressed

        self.replaceText("0")                                 #Displays number 0 on screen.





k=Application(calculator).grid()        #Application class is returned, and the tkinter calculator is displayed onto the grid
calculator.mainloop()                   #Execution of code stops here!
        
