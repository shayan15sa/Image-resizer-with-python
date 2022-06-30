from pydoc import text
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox as mb
import RR
import ctypes
from ctypes import wintypes
lpBuffer = wintypes.LPWSTR()
AppUserModelID = ctypes.windll.shell32.GetCurrentProcessExplicitAppUserModelID
AppUserModelID(ctypes.cast(ctypes.byref(lpBuffer), wintypes.LPWSTR))
appid = lpBuffer.value
ctypes.windll.kernel32.LocalFree(lpBuffer)
if appid is not None:
    print(appid)

# create root window
root = Tk()
root.geometry("550x400")
root.title = "Resize"
root.wm_title("Resizer")
#root.wm_iconbitmap("resize.ico")
#root.iconbitmap("resize.ico")

# frame inside root window
frame = Frame(root)
# geometry method
frame.pack()
# button inside frame which is
# inside root
fileT = StringVar()
fileDir = Entry(frame,width=60,font=45,textvariable=fileT)


titel = Label(frame,text="Resize images",font=55)

widT = StringVar()
wid = Entry(frame,textvariable=widT)

higT = StringVar()
hig = Entry(frame,textvariable=higT)
def set_text(e,text):
    e.delete(0,END)
    e.insert(0,text)
    return
def open_file(ft):
   file = filedialog.askopenfile(mode="r",filetypes=ft)
   if file:
        dir = file.name
        file.close()
        return dir
def browseF():
    set_text(fileDir,open_file([('Image', '*.jpg'),('Image',"*.png")]))
def open_folder():
    fol = filedialog.asksaveasfile(defaultextension="*.png",filetypes=[("Image JPG","*.JPG"),("Image PNG","*.PNG")])
    if fol:
        dir = fol.name
        fol.close()
        return dir
def emptycheck(t):
    ts = t.get()
    if ts == "":
        return None
    else:
        return int(ts)



button = Button(frame, text ='Browse',command=browseF)
titel.pack()

button.pack(pady=20)
fileDir.pack(pady=15)
wid.pack(pady=10)
hig.pack(pady=10)
att = Label(text="در صورت وارد نکردن هر یک از اندازه ها بصورت خودکار پر می شود",font=35)
att.pack()
def resize():
    print(fileT.get())
    if fileT.get() != "" and (widT.get() != "" or higT.get() != ""):
        RR.rr(fileT.get(),open_folder(),emptycheck(higT),emptycheck(widT))
        mb.showinfo("DONE","کار تمومه😎")
    else:
        mb.showerror("BUG","عکسی انتخاب نشده")
        # except:
        #     mb.showerror("BUG","bug bro")
resizew = Button(text="Resize تبدیل",command=resize)
resizew.pack(pady=5)
# Tkinter event loop
root.mainloop()