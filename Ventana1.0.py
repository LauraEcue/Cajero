from tkinter import Tk, ttk

def mostrar_info():
    lbl_saludo.config(text="Esta es una ventana con información")

def saludar():
    nombre = entrada_nombre.get()
    lbl_saludo.config(text=f"Bienvenido, {nombre}")

def limpiar():
    entrada_nombre.delete(0, 'end')
    lbl_saludo.config(text="Ventana Python")

if __name__ == "__main__":
    root = Tk()
    root.title("Mi aplicación")
    root.geometry("400x200")

    frm = ttk.Frame(root, padding=10)
    frm.grid()

    # Texto principal
    lbl_saludo = ttk.Label(frm, text="Ventana Python")
    lbl_saludo.grid(column=0, row=0, columnspan=3)

    # Solicitar nombre
    lbl_nombre = ttk.Label(frm, text="Ingrese su nombre:")
    lbl_nombre.grid(column=0, row=1)

    # Cuadro de texto
    entrada_nombre = ttk.Entry(frm, width=25)
    entrada_nombre.grid(column=1, row=1)

    # Botón saludar
    btn_saludar = ttk.Button(frm, text="Saludar", command=saludar)
    btn_saludar.grid(column=0, row=2)

    # Botón información
    btn_info = ttk.Button(frm, text="Información", command=mostrar_info)
    btn_info.grid(column=1, row=2)

    # Botón limpiar
    btn_limpiar = ttk.Button(frm, text="Limpiar", command=limpiar)
    btn_limpiar.grid(column=2, row=2)

    root.mainloop()