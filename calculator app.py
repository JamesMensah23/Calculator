from tkinter import *     # to import the tkinter gui module
import math
def click(value):           # the click effect
    ex = entry_field.get()
    answer=''
    try:
        if value=='C':
            ex = ex[:-1]     # to delete the last character entered in the entry field for the C function
            entry_field.delete(0, END)
            entry_field.insert(0, ex)
            return
        elif value=='CE'  :        # to delete the whole text in the entry field for CE function
            entry_field.delete(0, END)
        elif value=='AC' :
            entry_field.delete(0, END)
        elif value=='COS' :
            answer = math.cos(math.radians(eval(ex)))
        elif value=='TAN':
            answer = math.tan(math.radians(eval(ex)))
        elif value== 'SIN':
            answer = math.sin(math.radians(eval(ex)))
        elif value== '=':
            answer= eval(ex)

        else:
            entry_field.insert(END, value)
            return

        entry_field.delete(0, END)
        entry_field.insert(0, answer)
    except SyntaxError:
        pass


root = Tk()              # this to create a window for our app
root.title("smart calculus")     # title
root.config(bg='misty rose')      # background color(bg)
root.geometry('680x400+100+100')     # width and height coordinates

entry_field = Entry(root, font= ('arial', 20, 'bold'),bg='misty rose',fg='black', bd=5, relief=SUNKEN, width=15)    # we set the entry field as a class and name it entry_field so we can call it.
entry_field.grid(row=0, column=0, columnspan=8)         # we call the class sort of with the grid method. we also use columnspan to indent the entry field appropriately
# premier statement. button = Button(root)  We create a class Button and beacuse its in our window, we call root,then we name it button
# buttons
button_list = [
    'C', 'CE', 'AC','SIN','COS', 'TAN','RAD','HEX',
    '9','8','7','OCT','+','*','-','/',
    '6','5','4','X!','%','?','.','EXP',
    '3','2','1','0','%','log','In','=']
rowvalue =1
columnvalue =0
for i in button_list:
    button = Button(root,width=5,height=2, bd=2, relief=SUNKEN,text=i, bg='white', fg='black', font=('arial', 19, 'bold'), activebackground ='misty rose',command=lambda button=i: click(button))
    # text=i cos we want to create several other buttons with the same specs. so we make it a variable so we can implement as we go
    button.grid(row=rowvalue, column=columnvalue, pady=2)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0


root.mainloop()         # this to keep our window on a loop so it keeps on our screen
