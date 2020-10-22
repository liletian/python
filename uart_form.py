#this is a simple python form to read the uart
import tkinter as tk
import serial.tools.list_ports as port_list
import serial

def say_hi():
    ser = serial.Serial('COM4', 115200, timeout=1)
    ser.write(str.encode('w0103'))
    ser.write(str.encode('w027c'))
    ser.write(str.encode('w0080'))
    ser.write(str.encode('r'))
    ser.write(str.encode('06'))
    a=ser.read(2)
    print(a)
    ser.close()




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
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        ser = serial.Serial('COM4', 115200, timeout=1)
        ser.write(str.encode('w0103'))
        ser.write(str.encode('w027c'))
        ser.write(str.encode('w0080'))
        ser.write(str.encode('r'))
        ser.write(str.encode('06'))
        a=ser.read(2)
        print(a)
        ser.close()
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

