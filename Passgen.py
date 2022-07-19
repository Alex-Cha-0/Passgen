import random
from tkinter import *
from gui import *


root = Tk()
setwindow(root)
top = Label(root, text='Генератор паролей', font='Tahoma 13')
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
       'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
       '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
spec = ['!', '#', '$', '%', '&', '*', '+', '-', '?', '~']


def passgen(event=False):
    global len_entry, data
    global result
    global error
    global result_entry
    global tex1
    start = 0
    result_lst = []

    try:
        if 64 >= int(len_entry.get()) > 0:
            while start != int(len_entry.get()):
                error.config(text='')
                if spec_btnOn.get() == 0:
                    data = random.choice(lst)
                if spec_btnOn.get() == 1:
                    data = random.choice(lst + spec)
                result_lst.append(data)
                start += 1
                result_entry.delete(0, END)
                label_copy = Label(root, text="Ваш пароль скопирован в буфер обмена!", fg='#32CD32')
                label_copy.grid(row=2, column=1, sticky=W, columnspan=2)

    except ValueError:
        error.config(text='Вы ввели не числа')

    result_str = ''.join(result_lst)
    result_entry.insert(0, result_str)
    copy()


# def popup(event):
# try:
# menu.tk_popup(event.x_root, event.y_root)  # Pop the menu up in the given coordinates
# finally:
# menu.grab_release()  # Release it once an option is selected
def copy():
    inp = result_entry.get()  # Get the text inside entry widget
    root.clipboard_clear()  # Clear the tkinter clipboard
    root.clipboard_append(inp)  # Append to system clipboard


create_btn = Button(root, text="Создать пароль", font='Tahoma 10', command=passgen)
tex = Label(root, text='Длина пароля:', font='Tahoma 10')
len_entry = Entry(root, font='Tahoma 10', width=5, bd=2)
result = Label(root, font='Tahoma 10')
error = Label(root, fg='red')
result_entry = Entry(root, font='Tahoma 10', width=64, bd=2)
# menu = Menu(root, tearoff=0)
# menu.add_command(label='Copy', command=copy)
len_entry.bind('<Return>', passgen)  # Действие при нажатии Enter
tex1 = Label(root, text='Ваш пароль:', font='Tahoma 10')

spec_btnOn = IntVar()
spec_btn = Checkbutton(root, text='Спецсимволы', variable=spec_btnOn)
spec_btn.grid(row=1, column=2)

tex1.grid(row=2, column=0, sticky=W)
top.grid(row=0, column=1)
tex.grid(row=1, column=0, sticky=W)
len_entry.grid(row=1, column=1, sticky=W)
create_btn.grid(row=4, column=2, sticky=E)
tex1.grid(row=2, column=0)
result_entry.grid(row=3, column=0, columnspan=3)
error.grid(row=5, column=1)
# result_entry.bind('<Button-3>', popup)  # Bind a func to right click
root.mainloop()
