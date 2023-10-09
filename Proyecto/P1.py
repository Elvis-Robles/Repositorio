import tkinter as tk
from tkinter import ttk
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Función para iniciar sesión
def iniciar_sesion():
    # Obtener el nombre de usuario y contraseña ingresados
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    # Verificar las credenciales en la base de datos
    conn = sqlite3.connect("academia_usac.db")
    cursor = conn.cursor()
    cursor.execute("SELECT tipo_usuario FROM usuarios WHERE usuario=? AND contrasena=?", (usuario, contrasena))
    resultado = cursor.fetchone()

    if resultado:
        tipo_usuario = resultado[0]
        abrir_vista(tipo_usuario)
    else:
        mensaje_label.config(text="Credenciales incorrectas")

    conn.close()

# ... (código anterior)

# Función para abrir la vista correspondiente
def abrir_vista(tipo_usuario):
    ventana_inicio.destroy()

    if tipo_usuario == "Administrador":
        # Código para la vista del administrador
        pass
    elif tipo_usuario == "Catedrático":
        # Código para la vista del catedrático
        pass
    elif tipo_usuario == "Estudiante":
        abrir_ventana_estudiante()

# Función para abrir la ventana del estudiante
def abrir_ventana_estudiante():
    global ventana_estudiante
    ventana_estudiante = tk.Tk()
    ventana_estudiante.title("Ventana de Estudiante")

    # Componentes de la ventana de estudiante
    curso_label = tk.Label(ventana_estudiante, text="Selecciona un curso:")
    curso_label.pack()

    cursos_disponibles = ["Curso 1", "Curso 2", "Curso 3"]  # Reemplaza con la lista de cursos disponibles
    curso_combobox = ttk.Combobox(ventana_estudiante, values=cursos_disponibles)
    curso_combobox.pack()

    inscribirse_button = tk.Button(ventana_estudiante, text="Inscribirse en el curso", command=asignar_curso)
    inscribirse_button.pack()

    # Resto de componentes para la ventana de estudiante

# ... (código anterior)

# Código para abrir la ventana de inicio de sesión
ventana_inicio = tk.Tk()
ventana_inicio.title("Academia USAC")

# Componentes de la ventana de inicio de sesión
usuario_label = tk.Label(ventana_inicio, text="Nombre de usuario:")
usuario_label.pack()
usuario_entry = tk.Entry(ventana_inicio)
usuario_entry.pack()

contrasena_label = tk.Label(ventana_inicio, text="Contraseña:")
contrasena_label.pack()
contrasena_entry = tk.Entry(ventana_inicio, show="*")
contrasena_entry.pack()

iniciar_sesion_button = tk.Button(ventana_inicio, text="Iniciar Sesión", command=iniciar_sesion)
iniciar_sesion_button.pack()

# ... (código anterior)

ventana_inicio.mainloop()
