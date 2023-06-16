import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo


#inisialisasi
window = tkinter.Tk()
window.configure(bg="gray")
icon_img = PhotoImage(file='asset\icons8-school-100.png')
window.iconphoto(False, icon_img)
window.geometry("400x400")
window.resizable(False,False)
window.title("Login Mahasiswa")

# Header
header_label = ttk.Label(window, text="Pengisiian Formulir", font=(16), background="gray", foreground="white")
header_label.pack(pady=20)

# Variable dan Function
NAMA_LENGKAP = tkinter.StringVar()
NIM = tkinter.StringVar()
KELAS = tkinter.StringVar()
JURUSAN = tkinter.StringVar()
WALI_DOSEN = tkinter.StringVar()

#Fungsi Tombol
def tombol_click():
 if not NAMA_LENGKAP.get() or not NIM.get() or not KELAS.get() or not JURUSAN.get() or not WALI_DOSEN.get():
        showinfo(title="Error!", message="Mohon lengkapi semua data!")
 else:
        pesan = f"Hallo {NAMA_LENGKAP.get()}, Kamu sudah terdaftar!"
        showinfo(title="Selamat",message=pesan)


# frame input
style = ttk.Style()
style.configure(style="TEntry", fieldbackground="red")
input_frame = ttk.Frame(window)
# penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x", expand=True)

# komponen nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Lengkap:")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_label_entry = ttk.Entry(input_frame,textvariable=NAMA_LENGKAP)
nama_depan_label_entry.pack(padx=10,fill="x",expand=True)
# komponen nim
nim_label = ttk.Label(input_frame,text="NIM:")
nim_label.pack(padx=10,fill="x",expand=True)
nim_label_entry = ttk.Entry(input_frame,textvariable=NIM)
nim_label_entry.pack(padx=10,fill="x",expand=True)
# komponen kelas
kelas_label = ttk.Label(input_frame,text="Kelas:")
kelas_label.pack(padx=10,fill="x",expand=True)
kelas_label_entry = ttk.Entry(input_frame,textvariable=KELAS)
kelas_label_entry.pack(padx=10,fill="x",expand=True)
# komponen jurusan
jurusan_label = ttk.Label(input_frame,text="Jurusan:")
jurusan_label.pack(padx=10,fill="x",expand=True)
jurusan_label_entry = ttk.Entry(input_frame,textvariable=JURUSAN)
jurusan_label_entry.pack(padx=10,fill="x",expand=True)
# komponen wali dosens
wali_dosen_label = ttk.Label(input_frame,text="Wali Dosen:")
wali_dosen_label.pack(padx=10,fill="x",expand=True)
wali_dosen_label_entry = ttk.Entry(input_frame,textvariable=WALI_DOSEN)
wali_dosen_label_entry.pack(padx=10,fill="x",expand=True)

# tombol
tombol_daftar = ttk.Button(input_frame,text="Daftar",command=tombol_click)
tombol_daftar.pack(fill="x",expand=True, padx=10,pady=10)





window.mainloop()