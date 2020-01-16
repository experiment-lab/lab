# importing modules
import tkinter as tk
from tkinter import ttk,colorchooser,filedialog,messagebox,font
import os
# notpad window
def action():
    pass
root = tk.Tk()
root.title('Notebook')
root.geometry('800x600')
####################### main menu ####################### 
main_menu = tk.Menu(root)

##### creating menubars for main menu
file = tk.Menu(main_menu,tearoff = False)
edit = tk.Menu(main_menu,tearoff = False)
tools = tk.Menu(main_menu,tearoff = False)
helper = tk.Menu(main_menu,tearoff = False)

##### cascade file, edir, views onto main menu
main_menu.add_cascade(label = 'Files', menu = file)
main_menu.add_cascade(label = 'Edit', menu = edit)
main_menu.add_cascade(label = 'Views', menu = tools)
main_menu.add_cascade(label = 'Help', menu = helper)


#----------------------main menu end ------------------------

######################## tool bar #########################
tool_bar = ttk.Label(root)
tool_bar.pack(side = tk.TOP, fill = tk.X)

##### font box by default arial
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width = 30, textvariable = font_family, state = 'readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row = 0 ,column =0 , padx = 7)

##### font size 
font_size = tk.IntVar()
fontsize_box = ttk.Combobox(tool_bar, width = 10 ,textvariable = font_size, state ='readonly')
fontsize_box['values'] = tuple(range(1,81))
fontsize_box.grid(row = 0, column =1, padx = 2)
fontsize_box.current(11)

##### bolt button
#bold_icon = tk.PhotoImage(file = r'C:\icons2\bold.png')
bold_btn = ttk.Button(tool_bar, text = 'B',width = 2)
bold_btn.grid(row=0, column=2, padx=2)

##### italic button
#italic_icon = tk.PhotoImage(file = r'C:\icons2\italic.png')
italic_btn = ttk.Button(tool_bar, text = 'I',width = 2)
italic_btn.grid(row=0, column=3, padx=2)

##### underline button
#underline_icon = tk.PhotoImage(file = r'C:\Users\jaydeep\Desktop\py_project\icons2\underline.png')
underline_btn = ttk.Button(tool_bar, text = 'U',width = 2 )
underline_btn.grid(row=0, column=4, padx=2)
 
##### font color chooser
#color_icons = tk.PhotoImage(file = r'C:\Users\jaydeep\Desktop\py_project\icons2\font_color.png')
color_btn = ttk.Button(tool_bar, text = 'color',width = 5 )
color_btn.grid(row=0, column=5 , padx = 2)

##### alignment left
#Ralign_icon = tk.PhotoImage(file = r'C:\icons2\italic.png')
r_align_btn = ttk.Button(tool_bar, text = 'R align',width = 7)
r_align_btn.grid(row=0, column=6, padx=2)

#Ralign_icon = tk.PhotoImage(file = r'C:\icons2\italic.png')
c_align_btn = ttk.Button(tool_bar, text = 'C align',width = 7)
c_align_btn.grid(row=0, column=7, padx=2)
#Ralign_icon = tk.PhotoImage(file = r'C:\icons2\italic.png')
l_align_btn = ttk.Button(tool_bar, text = 'L align',width = 7)
l_align_btn.grid(row=0, column=8, padx=2)

#------------------------tool bar end ---------------------

######################## text editor #######################
text_editor = tk.Text(root)
text_editor.config(wrap = 'word', relief = tk.GROOVE )

text_editor.configure(font = ('Arial',12))
scroll_bar = tk.Scrollbar(root)
scroll_bar.pack(fill = tk.Y , side =tk.RIGHT)
text_editor.pack(fill = tk.BOTH ,expand =True)
text_editor.focus_set()

##### scroll_bar,text bar configure

scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

##### font family and font size funtinality
current_font_fmly = 'Arial'
current_font_size = 12

def change_font(root):
    global current_font_fmly
    current_font_fmly = font_family.get()
    text_editor.configure(font = (current_font_fmly,current_font_size))
 

def change_fontsize(root):
    global current_font_size
    current_font_size = font_size.get()
    text_editor.configure(font = (current_font_fmly,current_font_size))
  
font_box.bind("<<ComboboxSelected>>",change_font)  
fontsize_box.bind("<<ComboboxSelected>>",change_fontsize) 

##### bold,italic,underline button functinality

def change_bold():
    current_state = tk.font.Font(font = text_editor['font'])
    if current_state.actual()['weight'] == 'normal':
        text_editor.configure(font = (current_font_fmly,current_font_size,'bold'))
    else:
        text_editor.configure(font = (current_font_fmly,current_font_size,'normal'))

bold_btn.configure(command = change_bold)

def change_italic():
    current_state = tk.font.Font(font = text_editor['font'])
    if current_state.actual()['slant'] == 'roman':
        text_editor.configure(font = (current_font_fmly,current_font_size,'italic'))
    else:
        text_editor.configure(font = (current_font_fmly,current_font_size,'roman'))

italic_btn.configure(command = change_italic)

def change_underline():
    current_state = tk.font.Font(font = text_editor['font'])
    if current_state.actual()['underline'] == 0:
        text_editor.configure(font = (current_font_fmly,current_font_size,'underline'))
    else:
        text_editor.configure(font = (current_font_fmly,current_font_size,'normal'))

underline_btn.configure(command = change_underline)

def font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg = color_var[1])

color_btn.configure(command = font_color)

def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left' , justify =tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,tk.LEFT)

l_align_btn.configure(command = align_left)

def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,tk.RIGHT)

r_align_btn.configure(command = align_right)

def align_center():
    text_content =text_editor.get(1.0,'end')
    text_editor.tag_config('center', justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,tk.CENTER)
    
c_align_btn.configure(command = align_center)
#-----------------------text editor end ---------------------


######################### status bar#########################

status_bar =tk.Label(root , text = 'Status Bar')
status_bar.pack(side = tk.BOTTOM, fill =tk.X)

status_change = False
def statusbar(root):
    global status_change
    if text_editor.edit_modified():
        status_change = True
        characters = len(text_editor.get(1.0,'end-1c'))
        words = len(text_editor.get(1.0,'end-1c').split())
        status_bar.configure(text = f'Characters : {characters}  Words : {words}')
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",statusbar)

#------------------------ end status bar-------------------- 


######################### menu functinality ##################
##### path variable
address = ''

##### new file functionality
def new_file(event=None):
    global address
    address = ''
    text_editor.delete(1.0,tk.END)

##### open file functinality
def open_file(event=None):
     global address
     address = tk.filedialog.askopenfilename(initialdir = os.getcwd(),title = 'Select File', filetypes = (('Text file','*.txt'),('All files','*.*')))
     try:
         text_editor.delete(1.0,tk.END)
         with open(address,'r') as fr:
             text_editor.insert(tk.INSERT,fr.read())
         root.title(os.path.basename(address))
     except FileNotFoundError:
         return
     except:
         return

#####  Save functinality
def save_file(event=None):
    global address
    try:
        if address:
            content = str(text_editor.get(1.0,tk.END))
            with open(address,'w',encoding = 'utf-8') as fw:
                fw.write(content)
        else:
            address = tk.filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes = (('Text file','*.txt'),('All files','*.*')))
            content2 = str(text_editor.get(1.0,tk.END))
            address.write(content2)
            address.close()
    except:
        return

##### save as file functianlity
def save_as_file(event=None):
    global address
    try:
        address = tk.filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes = (('Text file','*.txt'),('All files','*.*')))
        content = str(text_editor.get(1.0,tk.END))
        address.write(content)
        address.close()
    except:
        return

##### exit functianlity  
def Exit(event=None):
    global address
    try:
        mbox = messagebox.askyesnocancel('warning','Do you want to save file?')
        if mbox == True:
            if address:
                content = str(text_editor.get(1.0,tk.END))
                with open(address,'w',encoding='uft-8') as fw:
                    fw.write(content)
                root.destroy()
            else:
                address = filedialog.asksaveasfile(mode='w',defaultextension = '.txt',filetypes= (('Text file','*.txt'),('All file','*.*')))
                content = str(text_editor.get(1.0,tk.END))
                address.write(content2)
                address.close()
                root.destroy()
        if mbox == False:
             root.destroy()
    except:
        return
    
##### find functinality
def find_func(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red', background = 'yellow')
    def replace():
        word = find_input.get()
        replace =  replace_input.get()
        content = str(text_editor.get(1.0,tk.END))
        new_content = content.replace(word,replace)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(tk.INSERT,new_content)
    
    find_box = tk.Toplevel()
    find_box.title('find replace box')
    find_box.geometry('450x250+500+200')
    find_box.resizable(0,0)
    
    ##### find frame
    find_frame = ttk.LabelFrame(find_box,text ='Find/Repalce',width=70)
    find_frame.pack(pady = 40)
    
    ######  find label
    find_input_label =  ttk.Label(find_frame,text = 'Find : ')
    find_input_label.grid(row= 0,column=0,padx =4,pady=4)
    
    ##### find entry
    find_input = ttk.Entry(find_frame,width = 30)
    find_input.grid(row= 0,column=1,padx =4,pady=4)
    
    ##### find button
    find_input_btn = ttk.Button(find_frame,width = 10,text = 'Find',command = find)
    find_input_btn.grid(row= 1,column=1,padx =4,pady=4)
    
    ##### replace label
    replace_label =  ttk.Label(find_frame,text = 'replace : ')
    replace_label.grid(row= 2,column=0,padx =4,pady=4)
    
    #### replace input
    replace_input = ttk.Entry(find_frame,width = 30)
    replace_input.grid(row= 2,column=1,padx =4,pady=4)
    
    ##### find button
    replace_input_btn = ttk.Button(find_frame,width = 10,text ='Repalce',command = replace)
    replace_input_btn.grid(row= 3,column=1,padx =4,pady=4)
    
    find_box.mainloop()    
        
        
        


#####  cascade file drop list
file.add_command(label = 'New Files', accelerator = 'Ctrl+N', command = new_file)
file.add_command(label = 'Open File' , accelerator = 'Ctrl+O', command = open_file)
file.add_command(label = 'Save' ,  accelerator = 'Ctrl+S',command = save_file )
file.add_command(label = 'Save as' , accelerator = 'Ctrl+Shift+S',command = save_as_file)
file.add_command(label = 'Exit' , accelerator = 'Alt+F4',command = Exit)

#####  cascade edit drop list

#edit.add_command(label = 'Undo' , accelerator = 'Ctrl+Z',  command = lambda:text_editor.event_generate("<Control-z>"))
#edit.add_command(label = 'Redo' , accelerator = 'Ctrl+D', command = lambda:text_editor.event_generate("<Control-Shift-z>"))
edit.add_command(label = 'Copy' , accelerator = 'Ctrl+c', command = lambda:text_editor.event_generate("<Control-c>"))
edit.add_command(label = 'Paste' , accelerator = 'Ctrl+v', command = lambda:text_editor.event_generate("Control-v"))
edit.add_command(label = 'Find' , accelerator = 'Ctrl+R', command = find_func)

#####  cascade views drop list
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar =tk.BooleanVar()
show_statusbar.set(True)
###### hide toolbar functinality
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill = tk.X)
        text_editor.pack(fill=tk.BOTH,expand = True)
        status_bar.pack(side = th.BOTTOM,fill = tk.X )
        show_toolbar = True
        
##### hide status bar functinality
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side = tk.BOTTOM , fill =tk.X)
        show_statusbar = True

tools.add_checkbutton(label = 'status bar',onvalue=True,offvalue=False,variable = show_toolbar,command=hide_toolbar)
tools.add_checkbutton(label = 'tool bar',onvalue=True,offvalue=False,variable=show_statusbar,command=hide_statusbar)


#------------------------menu functinality end---------------

root.config(menu = main_menu)

###### bind shortcut key
root.bind("<Control-o>",open_file)
root.bind("<Control-n>",new_file)
root.bind("<Control-s>",save_file)
root.bind("<Control-Shift-s>",save_as_file)
root.bind("<Alt-F4>",Exit)
root.bind("Control-r",find_func)
root.mainloop()

