
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox

current_file = ''

def open_file(value=None):
    global current_file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, END)
            text.insert(END, file.read())
    current_file=file_path
    
    if current_file:
        file_title = current_file.split('/')[-1]
    window.title(file_title + ' - Notpad ')

def save_file(value=None):
    global current_file
    print("saved")
    if current_file:
        with open(current_file, 'w') as file:
            file.write(text.get(1.0, END))

    else:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        print(file_path)

        if file_path:
            with open(file_path, 'w') as file:
                file.write(text.get(1.0, END))
            print('file saved')
        current_file = file_path

        if current_file:
            file_content = current_file.split('/')[-1]
            window.title(file_content)


def new_file(event=None):
    global current_file
    print('opened')
    file_path = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    print(file_path.name)
    if file_path:
        with open(file_path.name, 'w') as file:
            text.delete(1.0, END)
            content = file_path.name
    current_file = file_path.name
    
    if current_file:
        file_content = current_file.split('/')[-1]
    window.title(file_content + ' - Notepad')

window = Tk()

window.title(f"Untitled-Notepad")

menu_bar = Menu()
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0) #tearoff - remove line

menu_bar.add_cascade(label="File", menu=file_menu)   # cascade - add sub menu
file_menu.add_command(label="New", accelerator='Ctrl+N', command=new_file)
file_menu.add_command(label='Open', accelerator='Ctrl+O', command=open_file)
file_menu.add_command(label='Save', accelerator='Ctrl+S', command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=file_menu.quit)

edit_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator='Ctrl+X')
edit_menu.add_command(label="Copy", accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", accelerator='Ctrl+V')
edit_menu.add_command(label="Select All", accelerator='Ctrl+A')

text = scrolledtext.ScrolledText(window, selectbackground='yellow', selectforeground='black')
text.pack(pady=1, expand=True, fill=BOTH)

window.bind('<Control-n>', new_file)
window.bind('<Control-s>', save_file)
window.bind('<Control-o>', open_file)

window.mainloop()
