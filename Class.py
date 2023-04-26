from tkinter import *

root = Tk()
root.geometry("600x400")

list_name = ["Mickey Mouse", "Minnie Mouse", "Pikachu", "Donald duck"]
dict_student = { "name" : "Dilean",
                "age" : "10"}
try: 
    print(list_name[6])
    print(dict_student[dad])
    
 exept IndexError :
      messagebox.showinfo("Error", "This index does not exist!")
 exept KeyError : 
  Traceback (most recent call last):
File "/Users/allanasaam/opt/anaconda3/bin/spyder", line 11, in 
sys.exit(main())
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/app/start.py", line 252, in main
mainwindow.main(options, args)
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/app/mainwindow.py", line 1956, in main
mainwindow = create_window(MainWindow, app, splash, options, args)
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/app/utils.py", line 289, in create_window
main.setup()
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/app/mainwindow.py", line 778, in setup
PLUGIN_REGISTRY.register_plugin(self, PluginClass,
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/api/plugin_registration/registry.py", line 342, in register_plugin
instance = self._instantiate_spyder5_plugin(
File "/Users/allanasaam/opt/anaconda3/lifrom tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import os

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open ("open.png"))
save_img = ImageTk.PhotoImage(Image.open ("save.png"))
exit_img = ImageTk.PhotoImage(Image.open ("exit.jpg"))

label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)

my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)





open_button=Button(root,image=open_img, command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)    
    
root.mainloop()
b/python3.9/site-packages/spyder/api/plugin_registration/registry.py", line 184, in _instantiate_spyder5_plugin
plugin_instance = PluginClass(main_window, configuration=CONF)
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/api/plugins/new_api.py", line 973, in __init__
super().__init__(parent, configuration=configuration)
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/api/plugins/new_api.py", line 313, in __init__
self._container = container = self.CONTAINER_CLASS(
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/plugins/console/widgets/main_widget.py", line 135, in __init__
self.shell = InternalShell( # TODO: Move to use SpyderWidgetMixin?
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/plugins/console/widgets/internalshell.py", line 153, in __init__
super().__init__(parent, get_conf_path('history_internal.py'),
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/plugins/console/widgets/shell.py", line 665, in __init__
ShellBaseWidget.__init__(self, parent, history_filename,
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/plugins/console/widgets/shell.py", line 75, in __init__
self.history = self.load_history()
File "/Users/allanasaam/opt/anaconda3/lib/python3.9/site-packages/spyder/plugins/console/widgets/shell.py", line 503, in load_history
if rawhistory[1] != self.INITHISTORY[1]:
IndexError: list index out of range
      messagebox.showinfo("Error", "This key does not exist!")
      
root.mainloop()
