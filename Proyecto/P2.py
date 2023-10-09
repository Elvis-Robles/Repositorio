import sqlite3
import tkinter as tk
from tkinter import messagebox
import hashlib

# Función para encriptar contraseñas
def encriptar_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

# Función para registrar un nuevo usuario
def registrar_usuario():
    usuario = usuario_registro_entry.get()
    contrasena = contrasena_registro_entry.get()
    tipo_usuario = tipo_usuario_var.get()

    # Verificar que el usuario no exista en la base de datos
    cursor.execute("SELECT * FROM usuarios WHERE usuario=?", (usuario,))
    existe_usuario = cursor.fetchone()

    if existe_usuario:
        messagebox.showerror("Error", "El usuario ya existe.")
    else:
        # Insertar el nuevo usuario en la base de datos
        contrasena_encriptada = encriptar_contrasena(contrasena)
        cursor.execute("INSERT INTO usuarios (usuario, contrasena, tipo_usuario) VALUES (?, ?, ?)",
                       (usuario, contrasena_encriptada, tipo_usuario))
        conn.commit()
        messagebox.showinfo("Registro exitoso", "El usuario ha sido registrado exitosamente.")

# Función para iniciar sesión
def iniciar_sesion():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    cursor.execute("SELECT * FROM usuarios WHERE usuario=?", (usuario,))
    usuario_info = cursor.fetchone()

    if usuario_info:
        usuario_guardado = usuario_info[0]
        contrasena_guardada = usuario_info[1]
        tipo_usuario = usuario_info[2]

        if encriptar_contrasena(contrasena) == contrasena_guardada:
            abrir_vista(tipo_usuario)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

# Función para abrir la vista correspondiente
def abrir_vista(tipo_usuario):
    if tipo_usuario == "Estudiante":
        # Implementa la lógica para la vista de Estudiante
        pass
    elif tipo_usuario == "Catedrático":
        # Implementa la lógica para la vista de Catedrático
        pass
    elif tipo_usuario == "Administrador":
        # Implementa la lógica para la vista de Administrador
        pass

# Configurar la base de datos SQLite
conn = sqlite3.connect('academia.db')
cursor = conn.cursor()

# Crear la tabla de usuarios si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (usuario TEXT PRIMARY KEY, contrasena TEXT, tipo_usuario TEXT)''')
conn.commit()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Academia USAC")

# Componentes de la ventana de inicio de sesión
usuario_label = tk.Label(ventana_principal, text="Usuario:")
usuario_label.pack()
usuario_entry = tk.Entry(ventana_principal)
usuario_entry.pack()

contrasena_label = tk.Label(ventana_principal, text="Contraseña:")
contrasena_label.pack()
contrasena_entry = tk.Entry(ventana_principal, show="*")
contrasena_entry.pack()

iniciar_sesion_button = tk.Button(ventana_principal, text="Iniciar Sesión", command=iniciar_sesion)
iniciar_sesion_button.pack()

# Componentes de la ventana de registro
registro_frame = tk.Frame(ventana_principal)
registro_frame.pack()

usuario_registro_label = tk.Label(registro_frame, text="Nuevo Usuario:")
usuario_registro_label.pack()
usuario_registro_entry = tk.Entry(registro_frame)
usuario_registro_entry.pack()

contrasena_registro_label = tk.Label(registro_frame, text="Contraseña:")
contrasena_registro_label.pack()
contrasena_registro_entry = tk.Entry(registro_frame, show="*")
contrasena_registro_entry.pack()

tipo_usuario_label = tk.Label(registro_frame, text="Tipo de Usuario:")
tipo_usuario_label.pack()
tipo_usuario_var = tk.StringVar()
tipo_usuario_combobox = tk.OptionMenu(registro_frame, tipo_usuario_var, "Estudiante", "Catedrático")
tipo_usuario_combobox.pack()

registro_button = tk.Button(registro_frame, text="Registrar", command=registrar_usuario)
registro_button.pack()

ventana_principal.mainloop()

# Cerrar la conexión a la base de datos al salir de la aplicación
conn.close()

# Configurar la base de datos SQLite
conn = sqlite3.connect('academia.db')
cursor = conn.cursor()

# Función para asignar cursos a estudiantes
def asignar_curso():
    usuario = usuario_actual_var.get()
    curso = curso_var.get()

    # Verificar si el estudiante ya está inscrito en el curso
    cursor.execute("SELECT * FROM inscripciones WHERE usuario=? AND curso=?", (usuario, curso))
    inscripcion_existente = cursor.fetchone()

    if inscripcion_existente:
        messagebox.showwarning("Advertencia", "El estudiante ya está inscrito en este curso.")
    else:
        # Verificar si hay cupo disponible en el curso
        cursor.execute("SELECT cupo FROM cursos WHERE nombre=?", (curso,))
        cupo_disponible = cursor.fetchone()

        if cupo_disponible[0] > 0:
            # Reducir el cupo disponible
            cursor.execute("UPDATE cursos SET cupo=cupo-1 WHERE nombre=?", (curso,))
            
            # Registrar la inscripción en la base de datos
            cursor.execute("INSERT INTO inscripciones (usuario, curso) VALUES (?, ?)", (usuario, curso))
            conn.commit()
            
            messagebox.showinfo("Inscripción exitosa", f"El estudiante {usuario} se ha inscrito en el curso {curso}.")
        else:
            messagebox.showerror("Error", "El curso está lleno. No se puede inscribir al estudiante.")

# Función para crear cursos (administrador)
def crear_curso():
    nombre_curso = nombre_curso_var.get()
    cupo_curso = cupo_curso_var.get()

    # Verificar si el curso ya existe
    cursor.execute("SELECT * FROM cursos WHERE nombre=?", (nombre_curso,))
    curso_existente = cursor.fetchone()

    if curso_existente:
        messagebox.showwarning("Advertencia", "El curso ya existe.")
    else:
        # Registrar el nuevo curso en la base de datos
        cursor.execute("INSERT INTO cursos (nombre, cupo) VALUES (?, ?)", (nombre_curso, cupo_curso))
        conn.commit()
        messagebox.showinfo("Curso creado", f"El curso {nombre_curso} ha sido creado exitosamente.")

# Crear la ventana para la asignación de cursos
ventana_asignacion = tk.Tk()
ventana_asignacion.title("Asignación de Cursos")

# Componentes de la ventana de asignación de cursos
usuario_actual_label = tk.Label(ventana_asignacion, text="Usuario Actual:")
usuario_actual_label.pack()
usuario_actual_var = tk.StringVar()
usuario_actual_entry = tk.Entry(ventana_asignacion, textvariable=usuario_actual_var)
usuario_actual_entry.pack()

curso_label = tk.Label(ventana_asignacion, text="Curso a Asignar:")
curso_label.pack()
curso_var = tk.StringVar()
curso_combobox = tk.OptionMenu(ventana_asignacion, curso_var, "Curso 1", "Curso 2", "Curso 3")
curso_combobox.pack()

asignar_curso_button = tk.Button(ventana_asignacion, text="Asignar Curso", command=asignar_curso)
asignar_curso_button.pack()

# Crear la ventana para la creación de cursos (administrador)
ventana_creacion_curso = tk.Tk()
ventana_creacion_curso.title("Creación de Cursos (Administrador)")

# Componentes de la ventana de creación de cursos (administrador)
nombre_curso_label = tk.Label(ventana_creacion_curso, text="Nombre del Curso:")
nombre_curso_label.pack()
nombre_curso_var = tk.StringVar()
nombre_curso_entry = tk.Entry(ventana_creacion_curso, textvariable=nombre_curso_var)
nombre_curso_entry.pack()

cupo_curso_label = tk.Label(ventana_creacion_curso, text="Cupo del Curso:")
cupo_curso_label.pack()
cupo_curso_var = tk.IntVar()
cupo_curso_entry = tk.Entry(ventana_creacion_curso, textvariable=cupo_curso_var)
cupo_curso_entry.pack()

crear_curso_button = tk.Button(ventana_creacion_curso, text="Crear Curso", command=crear_curso)
crear_curso_button.pack()

ventana_asignacion.mainloop()


# Función para administrar cursos (catedrático)
def administrar_curso():
    # Implementa la lógica para la vista de administración de cursos por parte de los catedráticos
    pass

# Función para generar listados de notas en formato .xlsx
def generar_listado_notas():
    curso = curso_notas_var.get()

    # Obtener las notas de los estudiantes del curso
    cursor.execute("SELECT usuario, nota FROM notas WHERE curso=?", (curso,))
    notas = cursor.fetchall()

    if notas:
        # Crear un archivo Excel
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = f"Notas {curso}"

        # Encabezados
        sheet['A1'] = "Usuario"
        sheet['B1'] = "Nota"

        # Llenar el archivo Excel con las notas
        for idx, (usuario, nota) in enumerate(notas, start=2):
            sheet[f'A{idx}'] = usuario
            sheet[f'B{idx}'] = nota

        # Guardar el archivo Excel
        archivo_excel = f"listado_notas_{curso}.xlsx"
        workbook.save(archivo_excel)
        messagebox.showinfo("Listado de Notas", f"El listado de notas se ha generado en {archivo_excel}.")
    else:
        messagebox.showerror("Error", "No hay notas registradas para este curso.")

# Crear la ventana para administrar cursos (catedrático)
ventana_administracion_cursos = tk.Tk()
ventana_administracion_cursos.title("Administración de Cursos (Catedrático)")

# Componentes de la ventana de administración de cursos (catedrático)
curso_notas_label = tk.Label(ventana_administracion_cursos, text="Curso:")
curso_notas_label.pack()
curso_notas_var = tk.StringVar()
curso_notas_combobox = tk.OptionMenu(ventana_administracion_cursos, curso_notas_var, "Curso 1", "Curso 2", "Curso 3")
curso_notas_combobox.pack()

generar_listado_button = tk.Button(ventana_administracion_cursos, text="Generar Listado de Notas", command=generar_listado_notas)
generar_listado_button.pack()

ventana_administracion_cursos.mainloop()

# Función para ver cursos disponibles
def ver_cursos_disponibles():
    # Implementa la lógica para mostrar la lista de cursos disponibles
    pass

# Función para inscribirse en un curso
def inscribirse_curso():
    # Implementa la lógica para inscribirse en un curso
    pass

# Función para acceder a la página de un curso (estudiante)
def acceder_pagina_curso():
    # Implementa la lógica para acceder a la página del curso
    pass

# Función para desinscribirse de un curso
def desinscribirse_curso():
    # Implementa la lógica para desinscribirse de un curso
    pass

# Función para descargar un certificado
def descargar_certificado():
    # Implementa la lógica para descargar un certificado
    pass

# Crear la ventana para la funcionalidad de estudiantes
ventana_estudiantes = tk.Tk()
ventana_estudiantes.title("Funcionalidad para Estudiantes")

# Componentes de la ventana de estudiantes
ver_cursos_button = tk.Button(ventana_estudiantes, text="Ver Cursos Disponibles", command=ver_cursos_disponibles)
ver_cursos_button.pack()

inscribirse_curso_button = tk.Button(ventana_estudiantes, text="Inscribirse en Curso", command=inscribirse_curso)
inscribirse_curso_button.pack()

acceder_pagina_button = tk.Button(ventana_estudiantes, text="Acceder a Página del Curso", command=acceder_pagina_curso)
acceder_pagina_button.pack()

desinscribirse_curso_button = tk.Button(ventana_estudiantes, text="Desinscribirse de Curso", command=desinscribirse_curso)
desinscribirse_curso_button.pack()

descargar_certificado_button = tk.Button(ventana_estudiantes, text="Descargar Certificado", command=descargar_certificado)
descargar_certificado_button.pack()

ventana_estudiantes.mainloop()
