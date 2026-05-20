from tkinter import Tk, ttk
from tkinter import messagebox

if __name__ == "__main__":
    root = Tk()
    root.title("Mi aplicación")
      
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    
    lbl = ttk.Button(frm, text="Ventana Python - ")
    lbl.grid(column=1, row=0)

    btn = ttk.Button(frm, text="información", command=root.destroy)
    btn.grid(column=0, row=0)
    
    btn = ttk.Button(frm, text="Quit", command=root.destroy)
    btn.grid(column=2, row=0)
    
    root.mainloop()
    