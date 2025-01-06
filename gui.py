import tkinter as tk
import webbrowser
from tkinter import filedialog
from Reader.reader import Reader
from Parser.Parser import Parser
from Writer.Writer import Writer
#from tkinterhtml import HtmlFrame
read = None
parser = None
write = None
filename = ""
texto = ""
def cargar_archivo():
    global filename, texto  # Declaramos las variables globales
    archivo = filedialog.askopenfilename(title="Abrir archivo", filetypes=[("Source Code", "*.m"),("Text files", "*.txt")])
    filename = archivo
    if archivo:
        with open(archivo, "r") as f:
            texto = f.read()
            text_panel.delete(1.0, tk.END)
            text_panel.insert(tk.END, texto)  # Cargar el contenido en el panel de texto
def abrir_navegador():
    read = Reader(content=texto)
    parser = Parser(read)
    fileout = filename.split(".")[0]+".html"
    write = Writer(fileout, parser)
    write.write()
    url = fileout  
    webbrowser.open(url) 
root = tk.Tk()
root.title("Interfaz grafica MELI")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

text_panel = tk.Text(frame, wrap=tk.WORD, height=15, width=50)
text_panel.grid(row=0, column=0, padx=10, pady=10)

cargar_button = tk.Button(frame, text="Cargar Archivo", command=cargar_archivo)
cargar_button.grid(row=1, column=0, padx=10, pady=10)


boton_abrir = tk.Button(root, text="Abrir en el Navegador", command=abrir_navegador)
boton_abrir.pack(pady=20)

root.mainloop()
