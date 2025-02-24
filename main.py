from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tempfile
import os
import shutil
import logging
from encrypt import encypt_file


file_key = None

def select_key():
    filetypes = (
        ('pgp files', '*.pgp'),
        ('asc files', '*.asc'),
        ('gpg files', '*.gpg'),
        ('All files', '*.*')
    )

    file_key = fd.askopenfilename(
        title='Open a GPG public key',
        initialdir=os.getcwd(),
        filetypes=filetypes)
    return file_key


root = Tk()


temp_dir = tempfile.gettempdir()

temp_home_gnupg = os.path.join(temp_dir, "gnupghome")
os.makedirs(temp_home_gnupg, exist_ok=True)


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file to encrypt',
        initialdir='/',
        filetypes=filetypes)
    filetypes_gpg = (
        ('pgp files', '*.pgp'),
        ('asc files', '*.asc'),
        ('gpg files', '*.gpg'),
        ('All files', '*.*')
    )

    file_key = fd.askopenfilename(
        title='Open a GPG public key',
        initialdir=os.getcwd(),
        filetypes=filetypes_gpg)
    output_path = encypt_file(filename, file_key, temp_home_gnupg)
   

logo = PhotoImage(file="resources/gnupg.png")
image_label = Label(root, image=logo)
image_label.pack(padx=15, pady=15)

button_file = Button(master=root, text="Choose file to encrypt", command=select_file)
button_file.pack(padx=10, pady=10)
button_key = Button(master=root, text="Choose public key file", command=select_key)
button_key.pack(padx=10, pady=10)
label_filename = Label(master=root, text="")
label_filename.pack(padx=15, pady=15)



if __name__ == "__main__":
    root.geometry("800x800")
    root.title("Decrypter")
    root.mainloop()
    shutil.rmtree(temp_home_gnupg)