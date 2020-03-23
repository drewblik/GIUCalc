import tkinter as tk
#buttons, labels entrys for basic widgets
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row = 1, column = 0)

        #quit button
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row = 0, column = 1)

        #test button
        self.newButton = tk.Button(self)
        self.newButton["text"] = "Deez Nuts"
        self.newButton["command"] = self.nuts
        self.newButton.grid(row = 0, column = 2)

        #clickable button that stores info
        self.times_clicked = tk.Button(self, text = "click counter", command=self.store_info)
        self.times_clicked.grid(row = 1, column = 1)
        self.times_clicked.counter = 0




    def say_hi(self):
        print("hi there, everyone!")

    def nuts(self):
        print("Deez Nuts")
        self.times_clicked.counter += 1

    def store_info(self):
        print(self.times_clicked.counter)
        self.times_clicked.configure(text = "Clicked " + str(self.times_clicked.counter) + " times")
        self.times_clicked.update()
        self.times_clicked.counter += 1

root = tk.Tk()
app = Application(master=root)
app.mainloop()