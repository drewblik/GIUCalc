import tkinter as tk
import time
#buttons, labels entrys for basic widgets
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # = button
        self.equals = tk.Button(self,text = "=",command=self.answer)
        self.equals.num = ""
        self.equals.grid(row = 0, column = 3)
        self.equals.first_or_second = 0
        self.equals.operator = 0
        self.equals.first = ""
        self.equals.second = ""

        def numberButtons(self):
            # 0 button
            self.one = tk.Button(self, text="0", command=lambda: self.number(0))
            self.one.grid(row=4, column=1)

            # 1 button
            self.one = tk.Button(self, text = "1", command = lambda: self.number(1))
            self.one.grid(row = 3, column = 0)

            # 2 button
            self.one = tk.Button(self, text="2", command=lambda: self.number(2))
            self.one.grid(row=3, column=1)

            # 3 button
            self.one = tk.Button(self, text="3", command=lambda: self.number(3))
            self.one.grid(row=3, column=2)

            # 4 button
            self.one = tk.Button(self, text="4", command=lambda: self.number(4))
            self.one.grid(row=2, column=0)

            # 5 button
            self.one = tk.Button(self, text="5", command=lambda: self.number(5))
            self.one.grid(row=2, column=1)

            # 6 button
            self.one = tk.Button(self, text="6", command=lambda: self.number(6))
            self.one.grid(row=2, column=2)

            # 7 button
            self.one = tk.Button(self, text="7", command=lambda: self.number(7))
            self.one.grid(row=1, column=0)

            # 8 button
            self.one = tk.Button(self, text="8", command=lambda: self.number(8))
            self.one.grid(row=1, column=1)

            # 9 button
            self.one = tk.Button(self, text="9", command=lambda: self.number(9))
            self.one.grid(row=1, column=2)
        numberButtons(self)

        def operatorButtons(self):
            # + button
            self.operator = tk.Button(self, text="+", command=lambda: self.operation(0))
            self.operator.grid(row=1, column=3)

            # - button
            self.operator = tk.Button(self, text="-", command=lambda: self.operation(1))
            self.operator.grid(row=2, column=3)

            # * button
            self.operator = tk.Button(self, text="*", command=lambda: self.operation(2))
            self.operator.grid(row=3, column=3)

            # / button
            self.operator = tk.Button(self, text="/", command=lambda: self.operation(3))
            self.operator.grid(row=4, column=3)
        operatorButtons(self)


        # display button
        self.display = tk.Label(self,text = "0")
        self.display.grid(row = 0, column = 0, columnspan = 3)


        # clear button
        self.clear = tk.Button(self,text="C",command=self.clear_answer)
        self.clear.grid(row= 4, column = 2)

        # dot button
        self.dot = tk.Button(self, text=".", command=lambda: self.number("."))
        self.dot.grid(row=4, column=0)

    def clear_answer(self):
        self.equals.first_or_second = 0
        self.equals.operator = 0
        self.equals.first = ""
        self.equals.second = ""
        self.display.configure(text="")
        self.display.update()
    def dot_check(self,n):
        i = list(str(n))
        if "." in i:
            return True
        else:
            return False
    def number(self,n):
        if self.dot_check(n):
            self.display.configure(text="ERROR")
            self.display.update()
            time.sleep(2)

            if self.equals.first_or_second == 0:

                print(self.equals.first)
                self.display.configure(text=self.equals.first)
                self.display.update()
            if self.equals.first_or_second == 1:

                print(self.equals.second)
                self.display.configure(text= self.equals.second)
                self.display.update()

        else:
            if self.equals.first_or_second == 0:
                self.equals.first += str(n)
                print(self.equals.first)
                self.display.configure(text=self.equals.first)
                self.display.update()
            if self.equals.first_or_second == 1:
                self.equals.second += str(n)
                print(self.equals.second)
                self.display.configure(text= self.equals.second)
                self.display.update()


    def operation(self,n):
        self.equals.operator = n
        self.equals.first_or_second = 1

        print(self.equals.operator)
        print(self.equals.first)

    def answer(self):

        if self.equals.operator == 0:

            self.display.configure(text=float(self.equals.first) + float(self.equals.second))
            self.display.update()
            self.answer_is_first(float(self.equals.first) + float(self.equals.second))
        if self.equals.operator == 1:

            self.display.configure(text=float(self.equals.first) - float(self.equals.second))
            self.display.update()
            self.answer_is_first(float(self.equals.first) - float(self.equals.second))
        if self.equals.operator == 2:

            self.display.configure(text=float(self.equals.first) * float(self.equals.second))
            self.display.update()
            self.answer_is_first(float(self.equals.first) * float(self.equals.second))
        if self.equals.operator == 3:

            self.display.configure(text=float(self.equals.first) / float(self.equals.second))
            self.display.update()
            self.answer_is_first(float(self.equals.first) / float(self.equals.second))
    def answer_is_first(self,n):
        self.equals.first_or_second = 0
        self.equals.operator = 0
        self.equals.first = str(n)
        self.equals.second = ""


root = tk.Tk()
app = Application(master=root)
app.mainloop()