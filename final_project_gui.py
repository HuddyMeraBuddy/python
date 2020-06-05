
import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os


main_application=tk.Tk()
main_application.geometry('1200x600')
main_application.title('Paradox Pad')





#***********************************************main menu***************************************************************************


main_menu=tk.Menu()

newfile_icon=tk.PhotoImage(file=r'icon\add-filesatyam.png')
newwindow_icon=tk.PhotoImage(file=r'icon\addsatyam.png')
replace_icon=tk.PhotoImage(file=r'icon\open-filesatyam.png')
save_icon=tk.PhotoImage(file=r'icon\pursesatyam.png')
saveas_icon=tk.PhotoImage(file=r'icon\save-assatyam.png')
exit_icon=tk.PhotoImage(file=r'icon\exitsatyam.png')
undo_icon=tk.PhotoImage(file=r'icon\undosatyam.png')
redo_icon=tk.PhotoImage(file=r'icon\redosatyam.png')
cut_icon=tk.PhotoImage(file=r'icon\scissorssatyam.png')
copy_icon=tk.PhotoImage(file=r'icon\examsatyam.png')
paste_icon=tk.PhotoImage(file=r'icon\documentsatyam.png')
find_icon=tk.PhotoImage(file=r'icon\destinationsatyam.png')
openfile_icon=tk.PhotoImage(file=r'icon\historysatyam.png')
toolbar_icon=tk.PhotoImage(file=r'New folder\toolbars.png')
statusbar_icon=tk.PhotoImage(file=r'New folder\graphs.png')



file_menu=tk.Menu(main_menu,tearoff=0)
edit_menu=tk.Menu(main_menu,tearoff=0)
veiw_menu=tk.Menu(main_menu,tearoff=0)


#******************COLOUR THEME********************


default_theme=tk.PhotoImage(file=r'New folder\icons2_light_default.png')
light_plus_theme=tk.PhotoImage(file=r'New folder\icons2_light_plus.png')
dark_theme=tk.PhotoImage(file=r'New folder\icons2_dark.png')
red_theme=tk.PhotoImage(file=r'New folder\icons2_red.png')
monokai_theme=tk.PhotoImage(file=r'New folder\icons2_red.png')
night_blue_theme=tk.PhotoImage(file=r'New folder\icons2_night_blue.png')
colour_theme=tk.PhotoImage(file=r'New folder\icons2_font_color.png')
colour_theme=tk.Menu(main_menu,tearoff=0)

theme_choice=tk.StringVar()
color_icon=(default_theme,light_plus_theme,dark_theme,red_theme,monokai_theme,night_blue_theme)

dict_color={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}

main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_cascade(label='Veiw',menu=veiw_menu)
main_menu.add_cascade(label='Color Theme',menu=colour_theme)




###############################################end main menu########################################################################








#***********************************************toolbar*****************************************************************************

#*******font type***********
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#*******font size***********
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(1,140))
font_size.current(11)
font_size.grid(row=0,column=1,padx=5)

#*********buttons***********
bold_icon=tk.PhotoImage(file=r'New folder\icons2_bold.png')
itallic_icon=tk.PhotoImage(file=r'New folder\icons2_italic.png')
underline_icon=tk.PhotoImage(file=r'New folder\icons2_underline.png')
color_theme_icon=tk.PhotoImage(file=r'New folder\icons2_font_color.png')
align_left_icon=tk.PhotoImage(file=r'New folder\icons2_align_left.png')
align_right_icon=tk.PhotoImage(file=r'New folder\icons2_align_right.png')
align_center_icon=tk.PhotoImage(file=r'New folder\icons2_align_center.png')

bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
itallic_btn=ttk.Button(tool_bar,image=itallic_icon)
itallic_btn.grid(row=0,column=3,padx=5)
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)
color_theme_btn=ttk.Button(tool_bar,image=color_theme_icon)
color_theme_btn.grid(row=0,column=5,padx=5)
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

#******Buttons functionalities*******

def bold_button():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.config(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.config(font=(current_font_family,current_font_size,'normal'))

bold_btn.config(command=bold_button)

def itallic_button():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.config(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.config(font=(current_font_family,current_font_size,'roman'))

itallic_btn.config(command=itallic_button)

def underline_button():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.config(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.config(font=(current_font_family,current_font_size,'normal'))

underline_btn.config(command=underline_button)

def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

color_theme_btn.config(command=change_font_color)

def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=align_left)

def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=align_center)

def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command=align_right)


################################################end toolbar#########################################################################







#***********************************************text editor*************************************************************************

text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scrollbar=tk.Scrollbar(main_application)
text_editor.focus_set()
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scrollbar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrollbar.set)

#******font family and font size functionality******
current_font_family='Arial'
current_font_size=12

def change_font(main_application):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.config(font=(current_font_family,current_font_size))

def change_font_size(main_application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.config(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_font_size)





##############################################end text editor#######################################################################








#************************************************statusbar**************************************************************************

status_bar=ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

def changed(main_application):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,"end-1c").replace(' ',''))
        status_bar.config(text=f'Characters :{characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)


###############################################end statusbar########################################################################







#************************************************main menu functionality**************************************************************************


#********variables***********
url = ''


#******functions for menubar*********
def new_file():
    global url
    url=''
    text_editor.delete(1.0,tk.END)


def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select file",filetypes=(('Text Files','*.txt',),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))


def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text Files','*.txt',),('All Files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return


def saveas_file(event=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text Files','*.txt',),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return


def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel("Warning",'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2=text_editor.get(1.0,tk.END)
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetype=(('Text Files','*.txt',),('All Files','*.*'))) 
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return    





#********File menu command********
file_menu.add_command(label='New File',image=newfile_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)
file_menu.add_command(label='New Window',image=newwindow_icon,compound=tk.LEFT,accelerator='Ctrl+Shift+N')
file_menu.add_separator()
file_menu.add_command(label='Open File',image=openfile_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
file_menu.add_command(label='Save as..',image=saveas_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+s',command=saveas_file)
file_menu.add_separator()
file_menu.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)

#*********edit menu command********
edit_menu.add_command(label='Undo',image=undo_icon,compound=tk.LEFT,accelerator='Ctrl+Z')
edit_menu.add_command(label='Redo',image=redo_icon,compound=tk.LEFT,accelerator='Ctrl+Y')
edit_menu.add_separator()
edit_menu.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X')
edit_menu.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C')
edit_menu.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V')
edit_menu.add_separator()
edit_menu.add_command(label='Clear All',image=replace_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+x')
edit_menu.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F')

#**********veiw menu command*********
veiw_menu.add_checkbutton(label='    Toolbar',image=toolbar_icon,compound=tk.LEFT)
veiw_menu.add_checkbutton(label='    Statusbar',image=statusbar_icon,compound=tk.LEFT)

#**********color theme command*********
count=0
for i in dict_color:
    colour_theme.add_radiobutton(label=i,image=color_icon[count],variable=theme_choice,compound=tk.LEFT)
    count+=1




###############################################end main menu functionality########################################################################






main_application.config(menu=main_menu)

main_application.mainloop()
