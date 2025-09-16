import tkinter as tk
from tkinter import messagebox
import mysql.connector # type: ignore

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="videojuegos_db"
)

cursor = conexion.cursor()

# Función para agregar un videojuego
def agregar_videojuego():
    id = entry_id.get()
    titulo = entry_titulo.get()
    genero = entry_genero.get()
    clasificacion = entry_clasificacion.get()
    plataforma = entry_plataforma.get()

    if id and titulo:
        try:
            cursor.execute("INSERT INTO Videojuegos (ID, Titulo, Genero, Clasificacion, Plataforma) VALUES (%s, %s, %s, %s, %s)",
                           (id, titulo, genero, clasificacion, plataforma))
            conexion.commit()
            messagebox.showinfo("Éxito", "Videojuego agregado correctamente")
            mostrar_videojuegos()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Error al agregar: {error}")
    else:
        messagebox.showwarning("Aviso", "El campo ID y Título son obligatorios")

# Función para mostrar videojuegos
def mostrar_videojuegos():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM Videojuegos")
    for row in cursor.fetchall():
        listbox.insert(tk.END, row)

# Función para eliminar un videojuego por ID
def eliminar_videojuego():
    id = entry_id.get()
    if id:
        cursor.execute("DELETE FROM Videojuegos WHERE ID = %s", (id,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Videojuego eliminado")
        mostrar_videojuegos()
    else:
        messagebox.showwarning("Aviso", "Debes ingresar un ID para eliminar")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Gestión de Videojuegos")
ventana.geometry("600x500")

# Entradas
tk.Label(ventana, text="ID").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="Título").pack()
entry_titulo = tk.Entry(ventana)
entry_titulo.pack()

tk.Label(ventana, text="Género").pack()
entry_genero = tk.Entry(ventana)
entry_genero.pack()

tk.Label(ventana, text="Clasificación").pack()
entry_clasificacion = tk.Entry(ventana)
entry_clasificacion.pack()

tk.Label(ventana, text="Plataforma").pack()
entry_plataforma = tk.Entry(ventana)
entry_plataforma.pack()

# Botones
tk.Button(ventana, text="Agregar", command=agregar_videojuego).pack(pady=5)
tk.Button(ventana, text="Eliminar", command=eliminar_videojuego).pack(pady=5)
tk.Button(ventana, text="Mostrar", command=mostrar_videojuegos).pack(pady=5)

# Lista
listbox = tk.Listbox(ventana, width=80)
listbox.pack(pady=10)

ventana.mainloop()
