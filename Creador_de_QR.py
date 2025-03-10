"""
Versión 1.0 19/11/2024
Falta agregar funciones a todos los botones.
Falta incorporar que, cuando se guarde un archivo nuevo no se sustituya el anterior.
"""

import tkinter as tk 
from tkinter import simpledialog
from tkinter import messagebox
import qrcode
import os

class MyQr: 
    def __init__(self, master, size=30, padding=2): 
        self.master = master
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name, fg, bg): 
        #Solicitar al usuario que ingrese el texto para el código QR
        user_input = simpledialog.askstring(title="Entrada", prompt="Introduce el texto para el código QR: ", parent=self.master) #El simpledialog es la ventana que se abrirá al presionar el botón
        if user_input is None: 
            return # Salir del método sin hacer nada más

        # Solicitar al usuario que ingrese el nombre del archivo 
        file_name = simpledialog.askstring(title="Guardar como", prompt="Introduce el nombre del archivo:", parent=self.master)

        if file_name is None: # Si el usuario presiona "Cancel" 
            return # Salir del método sin hacer nada más
        
        file_name = file_name + ".png"

        # Revisión de la existencia de un archivo con el mismo nombre. Si el archivo ya existe, agregar un sufijo numérico 
        def generate_unique_file_name(file_name): 
            if not os.path.exists(file_name): 
                return file_name 
        
            base, ext = os.path.splitext(file_name) 
            counter = 1 
            new_file_name = f"{base} ({counter}){ext}" 
            
            while os.path.exists(new_file_name): 
                counter += 1 
                new_file_name = f"{base} ({counter}){ext}" 
            
            return new_file_name

        try:
            self.qr.add_data(user_input)
            self.qr.make(fit=True)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
           
            # Generar un nombre de archivo único 
            file_name = generate_unique_file_name(file_name) 
            qr_image.save(file_name) 
            messagebox.showinfo(title="Éxito", message=f"Se creó exitosamente: {file_name}") 
        except Exception as e: 
            messagebox.showerror(title="Error", message=f"Ocurrió un error: {e}")

#Interfaz gráfica

root = tk.Tk()
root.title("Creador de códigos QR")
root.geometry("400x400")
app = MyQr(root)
button = tk.Button(root, text="Crear código QR", command=lambda: app.create_qr(file_name="sample.png", fg="white", bg="black"))

button.pack(pady=20)

root.mainloop()

