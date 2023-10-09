import getpass
import hashlib

# Base de datos simulada con un diccionario
database = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Ingresa tu nombre de usuario: ")
    if username in database:
        print("El nombre de usuario ya existe.")
        return
    password = getpass.getpass("Ingresa tu contraseña: ")
    password_confirm = getpass.getpass("Confirma tu contraseña: ")
    if password != password_confirm:
        print("Las contraseñas no coinciden.")
        return
    database[username] = hash_password(password)
    print("Usuario registrado con éxito.")

def login():
    username = input("Ingresa tu nombre de usuario: ")
    if username not in database:
        print("El nombre de usuario no existe.")
        return
    password = getpass.getpass("Ingresa tu contraseña: ")
    if database[username] != hash_password(password):
        print("Contraseña incorrecta.")
        return
    print("Inicio de sesión exitoso.")

while True:
    action = input("¿Quieres iniciar sesión o registrarte? (login/register): ")
    if action == "login":
        login()
    elif action == "register":
        register()
class Curso:
    def __init__(self, nombre, costo, horario, codigo, cupo, catedratico):
        self.nombre = nombre
        self.costo = costo
        self.horario = horario
        self.codigo = codigo
        self.cupo = cupo
        self.catedratico = catedratico
        self.estudiantes = []

    def inscribir_estudiante(self, estudiante):
        if len(self.estudiantes) < self.cupo:
            self.estudiantes.append(estudiante)
            print(f"Estudiante {estudiante} inscrito con éxito en el curso {self.nombre}.")
        else:
            print("El cupo para este curso está lleno.")

    def desinscribir_estudiante(self, estudiante):
        if estudiante in self.estudiantes:
            self.estudiantes.remove(estudiante)
            print(f"Estudiante {estudiante} desinscrito con éxito del curso {self.nombre}.")
        else:
            print("El estudiante no está inscrito en este curso.")

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)

# Ejemplo de uso
curso_python = Curso("Python para principiantes", 100, "Lunes 10:00-12:00", "PY101", 30, "Prof. García")
curso_python.inscribir_estudiante("Juan Pérez")
curso_python.mostrar_estudiantes()
class Administrador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []
        self.profesores = []

    def crear_curso(self, nombre, costo, horario, codigo, cupo, catedratico):
        curso = Curso(nombre, costo, horario, codigo, cupo, catedratico)
        self.cursos.append(curso)
        print(f"Curso {nombre} creado con éxito.")

    def registrar_profesor(self, nombre):
        if nombre not in self.profesores:
            self.profesores.append(nombre)
            print(f"Profesor {nombre} registrado con éxito.")
        else:
            print("El profesor ya está registrado.")

    def mostrar_cursos(self):
        for curso in self.cursos:
            print(curso.nombre)

    def mostrar_profesores(self):
        for profesor in self.profesores:
            print(profesor)

# Ejemplo de uso
admin = Administrador("Admin")
admin.crear_curso("Python para principiantes", 100, "Lunes 10:00-12:00", "PY101", 30, "Prof. García")
admin.registrar_profesor("Prof. García")
admin.mostrar_cursos()
admin.mostrar_profesores()
class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def editar_curso(self, curso, nombre=None, costo=None, horario=None, codigo=None, cupo=None, catedratico=None):
        if curso in self.cursos:
            if nombre is not None:
                curso.nombre = nombre
            if costo is not None:
                curso.costo = costo
            if horario is not None:
                curso.horario = horario
            if codigo is not None:
                curso.codigo = codigo
            if cupo is not None:
                curso.cupo = cupo
            if catedratico is not None:
                curso.catedratico = catedratico
            print(f"Curso {curso.nombre} editado con éxito.")
        else:
            print("El profesor no imparte este curso.")

    def ver_notas(self, curso):
        if curso in self.cursos:
            for estudiante in curso.estudiantes:
                print(f"{estudiante}: {estudiante.nota}")

    def editar_nota(self, estudiante, nota):
        if estudiante in self.cursos.estudiantes:
            estudiante.nota = nota
            print(f"Nota de {estudiante} editada con éxito.")
        else:
            print("El estudiante no está inscrito en este curso.")

# Ejemplo de uso
profesor_garcia = Profesor("Prof. García")
profesor_garcia.agregar_curso(curso_python)
profesor_garcia.editar_curso(curso_python, nombre="Python avanzado")
profesor_garcia.ver_notas(curso_python)
