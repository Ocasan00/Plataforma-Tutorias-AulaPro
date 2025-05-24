import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tutoback import Plataforma  
from PIL import ImageTk, Image, ImageFilter
import os
from tkcalendar import DateEntry, Calendar

plataforma = Plataforma()

def ventana_estudiantes():
    ventana_estudiantes = tk.Toplevel()
    ventana_estudiantes.title("Estudiantes")
    ventana_estudiantes.geometry("900x600")


    #Codigo para insertar imagen de fondo
    image_path = os.path.join(os.path.dirname(__file__), 'fondo4.jpg')


    imagen_fondo = Image.open(image_path)
    imagen_fondo = imagen_fondo.resize((900, 600))
    imagen_desenfocada = imagen_fondo.filter(ImageFilter.GaussianBlur(radius=0))  
    imagen_fondo = ImageTk.PhotoImage(imagen_desenfocada)

    ventana_estudiantes.imagen_fondo = imagen_fondo

    fondo_label = tk.Label(ventana_estudiantes, image=imagen_fondo)
    fondo_label.pack(side="top", fill="x")
    #fondo_label.place(x=0, y=10, relwidth=1, relheight=1)


    #Botones de ventana de estudiantes

    boton_registrar = tk.Button(ventana_estudiantes, text="Registrar", command=ventana_registrar_estudiantes, width=20, height=2, font=("Arial", 14, "bold"), bg="#DD8100", fg="#FFFFFF")
    boton_registrar.place(relx=0.65, rely=0.4, anchor="w")  

    boton_agendar = tk.Button(ventana_estudiantes, text="Agendar Tutoría", command=ventana_agendar, width=20, height=2, font=("Arial", 14, "bold"), bg="#DD8100", fg="#FFFFFF")
    boton_agendar.place(relx=0.65, rely=0.55, anchor="w")  

    boton_progreso = tk.Button(ventana_estudiantes, text="Progreso Académico", command=ventana_progreso_academico, width=20, height=2, font=("Arial", 14, "bold"), bg="#DD8100", fg="#FFFFFF")
    boton_progreso.place(relx=0.65, rely=0.7, anchor="w")

    boton_tutores_activos = tk.Button(ventana_estudiantes, text="Tutores más Activos", command=ventana_tutores_activos, width=20, height=2, font=("Arial", 14, "bold"), bg="#DD8100", fg="#FFFFFF")
    boton_tutores_activos.place(relx=0.65, rely=0.85, anchor="w")


     

def ventana_registrar_estudiantes():
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registrar Estudiante")
    ventana_registro.geometry("700x500")

    #Codigo para insertar imagen de fondo
    image_path = os.path.join(os.path.dirname(__file__), 'fondo9.jpg')

    #ventana_admin.configure(bg="#020302")
    imagen_fondo = Image.open(image_path)
    imagen_fondo = imagen_fondo.resize((900, 600))
    imagen_desenfocada = imagen_fondo.filter(ImageFilter.GaussianBlur(radius=0))  
    imagen_fondo = ImageTk.PhotoImage(imagen_desenfocada)

    ventana_registro.imagen_fondo = imagen_fondo

    fondo_label = tk.Label(ventana_registro, image=imagen_fondo)
    #fondo_label.pack(side="top", fill="x")
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Etiquetas y campos de entrada
    
    titulo_label = tk.Label(ventana_registro, text="Registro de Estudiante", font=("Arial", 16, "bold"), fg="white", bg="#1a1a1a")
    titulo_label.pack(pady=30)

    nombre_label = tk.Label(ventana_registro, text="Nombre:", fg="white", bg="#1a1a1a", font=("Arial", 12))
    nombre_label.pack()
    nombre_entry = tk.Entry(ventana_registro)
    nombre_entry.pack(pady=20)

    edad_label = tk.Label(ventana_registro, text="Edad:", fg="white", bg="#1a1a1a", font=("Arial", 12))
    edad_label.pack()
    edad_entry = tk.Entry(ventana_registro)
    edad_entry.pack(pady=20)

    materias_label = tk.Label(ventana_registro, text="Materias de interés (separadas por coma):", fg="white", bg="#1a1a1a", font=("Arial", 12))
    materias_label.pack()
    materias_entry = tk.Entry(ventana_registro)
    materias_entry.pack(pady=20)

    # Función para registrar estudiante
    def registrar_estudiante():
        nombre = nombre_entry.get()
        edad = edad_entry.get()
        materias = materias_entry.get()

        if not nombre or not edad or not materias:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        try:
            edad = int(edad)
        except ValueError:
            messagebox.showerror("Error", "Edad debe ser un número.")
            return

        materias_lista = [m.strip() for m in materias.split(",")]

        plataforma.registrar_estudiante(nombre, edad, materias_lista)
        messagebox.showinfo("Éxito", f"Estudiante {nombre} registrado correctamente.")
        ventana_registro.destroy()

    # Botón de registrar
    registrar_btn = tk.Button(ventana_registro, text="Registrar", command=registrar_estudiante, bg="#DD8100", fg="white", font=("Arial", 12, "bold"))
    registrar_btn.pack(pady=20)

def ventana_agendar():
    ventana_agendar = tk.Toplevel()
    ventana_agendar.title("Agendar Tutoría")
    ventana_agendar.geometry("700x500")

    #Codigo para insertar imagen de fondo

    image_path = os.path.join(os.path.dirname(__file__), 'fondo9.jpg')

    #ventana_admin.configure(bg="#020302")
    imagen_fondo = Image.open(image_path)
    imagen_fondo = imagen_fondo.resize((900, 600))
    imagen_desenfocada = imagen_fondo.filter(ImageFilter.GaussianBlur(radius=0))  
    imagen_fondo = ImageTk.PhotoImage(imagen_desenfocada)

    ventana_agendar.imagen_fondo = imagen_fondo

    fondo_label = tk.Label(ventana_agendar, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Etiquetas y campos de entrada 

    titulo_label = tk.Label(ventana_agendar, text="Agendar una Tutoría", font=("Arial", 16, "bold"), fg="white", bg="#1a1a1a")
    titulo_label.pack(pady=10)

    estudiante_label = tk.Label(ventana_agendar, text="Tu nombre:", fg="white", bg="#1a1a1a", font=("Arial", 12))
    estudiante_label.pack()
    estudiante_entry = tk.Entry(ventana_agendar)
    estudiante_entry.pack()

    materia_label = tk.Label(ventana_agendar, text="Materia:", fg="white", bg="#1a1a1a", font=("Arial", 12))
    materia_label.pack()
    materia_entry = tk.Entry(ventana_agendar)
    materia_entry.pack()

    fecha_label = tk.Label(ventana_agendar, text="Fecha deseada:", fg="white", bg="#1a1a1a", font=("Arial", 12))
    fecha_label.pack(pady=5)
    calendario = DateEntry(ventana_agendar, date_pattern='yyyy-mm-dd')
    calendario.pack()

    tutor_combo = ttk.Combobox(ventana_agendar, state="readonly")
    tutor_combo.pack(pady=10)

    hora_combo = ttk.Combobox(ventana_agendar, state="readonly")
    hora_combo.pack(pady=10)

    #Funcion para buscar tutores disponibles de acuerdo a la fecha elegida
    def buscar_tutores():
        materia = materia_entry.get().strip().lower()
        fecha = calendario.get_date().strftime("%Y-%m-%d")

        if not materia:
            messagebox.showerror("Error", "Ingresa una materia.")
            return

        tutores_disponibles = []
        for tutor in plataforma.obtener_tutores_por_materia(materia):
            for disp in tutor.disponibilidad:
                if disp.startswith(fecha):
                    tutores_disponibles.append(tutor)
                    break  # Solo necesita una coincidencia

        if not tutores_disponibles:
            messagebox.showinfo("Sin resultados", "No hay tutores disponibles ese día para esa materia.")
            tutor_combo['values'] = []
            hora_combo['values'] = []
            return

        nombres_tutores = [t.nombre for t in tutores_disponibles]
        tutor_combo['values'] = nombres_tutores
        tutor_combo.set("Selecciona un tutor")

        hora_combo.set("")
        hora_combo['values'] = []

    buscar_btn = tk.Button(ventana_agendar, text="Buscar Tutores", command=buscar_tutores, bg="#7B0061", fg="white")
    buscar_btn.pack(pady=5)

    # Funcion para que al seleccionar un tutor, muestre sus horas disponibles para ese día
    def actualizar_horas_disponibles(event):
        tutor_nombre = tutor_combo.get()
        fecha = calendario.get_date().strftime("%Y-%m-%d")
        tutor = next((t for t in plataforma.tutores if t.nombre == tutor_nombre), None)

        if tutor:
            horas_disponibles = []
            for disp in tutor.disponibilidad:
                if disp.startswith(fecha):
                    horas_disponibles.append(disp.split()[1])
            hora_combo['values'] = horas_disponibles
            if horas_disponibles:
                hora_combo.set(horas_disponibles[0])

    tutor_combo.bind("<<ComboboxSelected>>", actualizar_horas_disponibles)

    def agendar_tutoria():
        nombre_estudiante = estudiante_entry.get().strip()
        materia = materia_entry.get().strip()
        fecha = calendario.get_date().strftime("%Y-%m-%d")
        tutor_nombre = tutor_combo.get()
        hora = hora_combo.get()

        if not all([nombre_estudiante, materia, tutor_nombre, hora]):
            messagebox.showerror("Error", "Completa todos los campos.")
            return

        estudiante = next((e for e in plataforma.estudiantes if e.nombre == nombre_estudiante), None)
        tutor = next((t for t in plataforma.tutores if t.nombre == tutor_nombre), None)

        if not estudiante:
            messagebox.showerror("Error", f"Estudiante {nombre_estudiante} no registrado.")
            return

        try:
            plataforma.agendar_tutoria(estudiante, tutor, fecha, hora, materia)
            messagebox.showinfo("Éxito", f"Tutoría agendada con {tutor_nombre} el {fecha} a las {hora}.")
            ventana_agendar.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    agendar_btn = tk.Button(ventana_agendar, text="Agendar", command=agendar_tutoria, bg="#DD8100", fg="white", font=("Arial", 12, "bold"))
    agendar_btn.pack(pady=20)

def ventana_progreso_academico():

    #Muestra un reporte del progreso academico de los estudiantes con su promedio
    ventana_reporte = tk.Toplevel()
    ventana_reporte.title("Progreso Académico")
    ventana_reporte.geometry("500x400")

    reporte_text = plataforma.reporte_progreso_estudiantes()

    text_widget = tk.Text(ventana_reporte, wrap="word")
    text_widget.pack(expand=True, fill="both")
    text_widget.insert("1.0", reporte_text)
    text_widget.config(state="disabled")




def ventana_tutores():
    ventana_tutores = tk.Toplevel()
    ventana_tutores.title("Tutores")
    ventana_tutores.geometry("900x600")

    image_path = os.path.join(os.path.dirname(__file__), 'fondo8.jpg')

    #ventana_admin.configure(bg="#020302")
    imagen_fondo = Image.open(image_path)
    imagen_fondo = imagen_fondo.resize((900, 600))
    imagen_desenfocada = imagen_fondo.filter(ImageFilter.GaussianBlur(radius=0))  
    imagen_fondo = ImageTk.PhotoImage(imagen_desenfocada)

    ventana_tutores.imagen_fondo = imagen_fondo

    fondo_label = tk.Label(ventana_tutores, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)


    boton_registrar = tk.Button(ventana_tutores, text="Registrar", command=ventana_registrar_tutores, width=20, height=3, font=("Arial", 14, "bold"), bg="#7B0061", fg="#FFFFFF")
    boton_registrar.place(relx=0.4, rely=0.3, anchor="e")  

    boton_calificacion = tk.Button(ventana_tutores, text="Agregar Calificación", command=ventana_agregar_calificacion, width=20, height=3, font=("Arial", 14, "bold"), bg="#7B0061", fg="#FFFFFF")
    boton_calificacion.place(relx=0.4, rely=0.5, anchor="e")

    boton_materias = tk.Button(ventana_tutores, text="Materias más Solicitadas", command=ventana_materias_solicitadas, width=20, height=3, font=("Arial", 14, "bold"), bg="#7B0061", fg="#FFFFFF")
    boton_materias.place(relx=0.4, rely=0.7, anchor="e")

    




def ventana_registrar_tutores():
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registrar Tutor")
    ventana_registro.geometry("700x600")

    image_path = os.path.join(os.path.dirname(__file__), 'fondo9.jpg')

    #ventana_admin.configure(bg="#020302")
    imagen_fondo = Image.open(image_path)
    imagen_fondo = imagen_fondo.resize((900, 600))
    imagen_desenfocada = imagen_fondo.filter(ImageFilter.GaussianBlur(radius=0))  
    imagen_fondo = ImageTk.PhotoImage(imagen_desenfocada)

    ventana_registro.imagen_fondo = imagen_fondo

    fondo_label = tk.Label(ventana_registro, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Etiquetas y campos de entrada
    titulo_label = tk.Label(ventana_registro, text="Registro de Tutor", font=("Arial", 16, "bold"), fg="white", bg="#1a1a1a")
    titulo_label.pack(pady=10)

    nombre_label = tk.Label(ventana_registro, text="Nombre:", fg="white", bg="#1a1a1a", font=("Arial", 12))
    nombre_label.pack()
    nombre_entry = tk.Entry(ventana_registro)
    nombre_entry.pack(pady=10)

    especialidades_label = tk.Label(ventana_registro, text="Especialidades (separadas por coma):", fg="white", bg="#1a1a1a", font=("Arial", 12))
    especialidades_label.pack()
    especialidades_entry = tk.Entry(ventana_registro)
    especialidades_entry.pack(pady=10)

    disponibilidad_label = tk.Label(ventana_registro, text="Disponibilidad:", fg="white", bg="#1a1a1a", font=("Arial", 12))
    disponibilidad_label.pack(pady=10)

    # Calendario para que el tutpr registre su disponibilidad
    calendario = DateEntry(ventana_registro, date_pattern='yyyy-mm-dd')
    calendario.pack(pady=10)

    # Lista para definir las horas disponibles
    horas = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
    hora_combo = ttk.Combobox(ventana_registro, values=horas, state="readonly")
    hora_combo.pack(pady=10)

    # Lista para mostrar disponibilidades agregadas
    disponibilidades = []

    lista_disponibilidad = tk.Listbox(ventana_registro, height=5)
    lista_disponibilidad.pack(pady=10)

    # Función para agregar disponibilidad a la lista
    def agregar_disponibilidad():
        fecha = calendario.get_date().strftime("%Y-%m-%d")
        hora = hora_combo.get()
        if not hora:
            messagebox.showerror("Error", "Selecciona una hora.")
            return
        disponibilidad = f"{fecha} {hora}"
        disponibilidades.append(disponibilidad)
        lista_disponibilidad.insert(tk.END, disponibilidad)

    agregar_btn = tk.Button(ventana_registro, text="Agregar Disponibilidad", command=agregar_disponibilidad, bg="#7B0061", fg="white")
    agregar_btn.pack(pady=10)

    # Función para registrar tutor
    def registrar_tutor():
        nombre = nombre_entry.get()
        especialidades = especialidades_entry.get()

        if not nombre or not especialidades or not disponibilidades:
            messagebox.showerror("Error", "Completa todos los campos y al menos una disponibilidad.")
            return

        especialidades_lista = [e.strip() for e in especialidades.split(",")]

        plataforma.registrar_tutor(nombre, especialidades_lista, disponibilidades)
        messagebox.showinfo("Éxito", f"Tutor {nombre} registrado correctamente.")
        ventana_registro.destroy()

    # Botón de registrar tutor
    registrar_btn = tk.Button(ventana_registro, text="Registrar Tutor", command=registrar_tutor, bg="#7B0061", fg="white", font=("Arial", 12, "bold"))
    registrar_btn.pack(pady=10)


def ventana_agregar_calificacion():
    ventana_calificacion = tk.Toplevel()
    ventana_calificacion.title("Agregar Calificación")
    ventana_calificacion.geometry("700x400")

    image_path = os.path.join(os.path.dirname(__file__), 'fondo9.jpg')

    #ventana_admin.configure(bg="#020302")
    imagen_fondo = Image.open(image_path)
    imagen_fondo = imagen_fondo.resize((900, 600))
    imagen_desenfocada = imagen_fondo.filter(ImageFilter.GaussianBlur(radius=0))  
    imagen_fondo = ImageTk.PhotoImage(imagen_desenfocada)

    ventana_calificacion.imagen_fondo = imagen_fondo

    fondo_label = tk.Label(ventana_calificacion, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(ventana_calificacion, text="Estudiante:", fg="white", bg="#1a1a1a", font=("Arial", 12)).pack(pady=10)
    estudiante_cb = ttk.Combobox(ventana_calificacion, values=[e.nombre for e in plataforma.estudiantes])
    estudiante_cb.pack()

    tk.Label(ventana_calificacion, text="Materia:", fg="white", bg="#1a1a1a", font=("Arial", 12)).pack(pady=10)
    materia_entry = tk.Entry(ventana_calificacion)
    materia_entry.pack()

    tk.Label(ventana_calificacion, text="Nota:", fg="white", bg="#1a1a1a", font=("Arial", 12)).pack(pady=10)
    nota_entry = tk.Entry(ventana_calificacion)
    nota_entry.pack()

    def registrar_nota():
        nombre_estudiante = estudiante_cb.get()
        materia = materia_entry.get()
        nota = nota_entry.get()

        if not nombre_estudiante or not materia or not nota:
            messagebox.showerror("Error", "Completa todos los campos.")
            return

        try:
            nota = float(nota)
        except ValueError:
            messagebox.showerror("Error", "Nota debe ser numérica.")
            return

        estudiante = next((e for e in plataforma.estudiantes if e.nombre == nombre_estudiante), None)
        if not estudiante:
            messagebox.showerror("Error", "Estudiante no encontrado.")
            return

        plataforma.registrar_progreso(estudiante, materia, nota)
        messagebox.showinfo("Éxito", f"Nota registrada correctamente para {nombre_estudiante}.")
        ventana_calificacion.destroy()

    tk.Button(ventana_calificacion, text="Guardar Nota", command=registrar_nota, bg="#7B0061", fg="white", font=("Arial", 12, "bold")).pack(pady=20)


def ventana_materias_solicitadas():
    ventana_materias = tk.Toplevel()
    ventana_materias.title("Materias Más Solicitadas")
    ventana_materias.geometry("400x300")

    reporte = plataforma.reporte_materias_mas_solicitadas()
    texto = "\n".join([f"{materia}: {cantidad} tutorías" for materia, cantidad in reporte])

    text_widget = tk.Text(ventana_materias, wrap="word")
    text_widget.pack(expand=True, fill="both")
    text_widget.insert("1.0", texto if texto else "Aún no hay tutorías registradas.")
    text_widget.config(state="disabled")

def ventana_tutores_activos():
    ventana_tutores_mas = tk.Toplevel()
    ventana_tutores_mas.title("Tutores Más Activos")
    ventana_tutores_mas.geometry("400x300")

    reporte = plataforma.reporte_tutores_mas_activos()
    texto = "\n".join([f"{tutor.nombre}: {tutor.sesiones} tutorías" for tutor in reporte])

    text_widget = tk.Text(ventana_tutores_mas, wrap="word")
    text_widget.pack(expand=True, fill="both")
    text_widget.insert("1.0", texto if texto else "Aún no hay tutorías registradas.")
    text_widget.config(state="disabled")



ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("900x600")

image_path = os.path.join(os.path.dirname(__file__), 'fondo7.jpg')

#ventana_admin.configure(bg="#020302")
imagen_fondo = Image.open(image_path)
imagen_fondo = imagen_fondo.resize((1600, 1000))
imagen_desenfocada = imagen_fondo.filter(ImageFilter.GaussianBlur(radius=0))  
imagen_fondo = ImageTk.PhotoImage(imagen_desenfocada)

ventana_principal.imagen_fondo = imagen_fondo

fondo_label = tk.Label(ventana_principal, image=imagen_fondo)
#fondo_label.pack(side="top", fill="x")
fondo_label.place(x=0, y=100, relwidth=1, relheight=1)


titulo = tk.Label(ventana_principal, text="AulaPro", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#242424", padx=800, pady=40)
titulo.place(relx=0.5, rely=0.05, anchor="center")



boton_administracion = tk.Button(ventana_principal, text="Estudiantes", command=ventana_estudiantes, width=20, height=3, font=("Arial", 14, "bold"), bg="#DD8100", fg="#FFFFFF")
boton_administracion.place(relx=0.5, rely=0.5, anchor="center", y=-70)  

boton_reservar = tk.Button(ventana_principal, text="Tutores", command=ventana_tutores, width=20, height=3, font=("Arial", 14, "bold"), bg="#7B0061", fg="#FFFFFF")
boton_reservar.place(relx=0.5, rely=0.5, anchor="center", y=90)  


ventana_principal.mainloop()




