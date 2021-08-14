from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def cut():
    TextArea.event_generate(('<<Cut>>'))

def copy():
    TextArea.event_generate(('<<Copy>>'))

def paste():
    TextArea.event_generate(('<<Paste>>'))

def about():
    messagebox.showinfo('Notepad', 'Notepad made by Code Monk')

def new():
    global file
    root.title('Untitled - Notepad')
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + ' - Notepad')
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])

        if file == "":
            file = None
        else:
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file + ' - Notepad'))
            print('File Saved')

    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.iconbitmap(r'icons/notes.ico')
    root.geometry('788x644')

    TextArea = Text(root, font=('Consolas', 11))
    TextArea.pack(fill=BOTH, expand=True)
    file = None

    MenuBar = Menu(root)

    ################################# FILE MENU #################################
    FileMenu = Menu(MenuBar, tearoff=0)
    # Open New File
    FileMenu.add_command(label='New', command=new)
    # Open Existing File
    FileMenu.add_command(label='Open', command=openFile)
    # Save Current File
    FileMenu.add_command(label='Save as', command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=root.destroy)
    MenuBar.add_cascade(label="File", menu=FileMenu)

    ################################# EDIT MENU #################################
    EditMenu = Menu(MenuBar, tearoff=0)
    # Cut Option
    EditMenu.add_command(label="Cut", command=cut)
    # Copy Option
    EditMenu.add_command(label="Copy", command=copy)
    # Paste Option
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    ################################# HELP MENU #################################
    HelpMenu = Menu(MenuBar, tearoff=0)
    # About Notepad
    HelpMenu.add_command(label='About', command=about)
    MenuBar.add_cascade(label='Help', menu=HelpMenu)

    root.config(menu=MenuBar)

    # Adding ScrollBar
    Scrollbar = Scrollbar(TextArea, orient=VERTICAL)
    Scrollbar.pack(side=RIGHT, fill=Y)
    Scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scrollbar.set)

    root.mainloop()