import customtkinter as ctk
import random
from screeninfo import get_monitors
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def cargar_estudiantes(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]

# Cargar estudiantes desde archivo
estudiantes = cargar_estudiantes("estudiantes.txt")
estudiante_actual = None

offset_x = 0
offset_y = 0
collapsed = False  # 👈 estado

def seleccionar_archivo():
    global estudiantes, estudiante_actual
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo de estudiantes",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if ruta:
        estudiantes = cargar_estudiantes(ruta)
        estudiante_actual = None
        label_nombre.configure(text="Lista cargada ✔")
        btn_quitar.configure(state="disabled")

def iniciar_arrastre(event):
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y

def mover_ventana(event):
    x = root.winfo_pointerx() - offset_x
    y = root.winfo_pointery() - offset_y
    root.geometry(f"+{x}+{y}")

def elegir():
    global estudiante_actual
    if not estudiantes:
        estudiante_actual = None
        label_nombre.configure(text="Sin estudiantes")
        btn_quitar.configure(state="disabled")
        return
    estudiante_actual = random.choice(estudiantes)
    label_nombre.configure(text=estudiante_actual)
    btn_quitar.configure(state="normal")

def limpiar():
    global estudiante_actual
    estudiante_actual = None
    label_nombre.configure(text="")
    btn_quitar.configure(state="disabled")

def quitar_estudiante():
    global estudiantes, estudiante_actual
    if estudiante_actual and estudiante_actual in estudiantes:
        estudiantes.remove(estudiante_actual)
    estudiante_actual = None
    label_nombre.configure(text="")
    btn_quitar.configure(state="disabled")

def cerrar():
    root.destroy()

def toggle_view():
    global collapsed

    if not collapsed:
        frame.pack_forget()
        root.geometry("160x50")
        toggle_btn.place(relx=0.5, rely=0.5, anchor="center")
        collapsed = True
    else:
        frame.pack(fill="both", expand=True, padx=5, pady=5)
        root.geometry("380x140")
        toggle_btn.place_forget()
        collapsed = False


def posicionar_ventana(root, ancho=380, alto=140):
    monitores = get_monitors()
    monitor = monitores[1] if len(monitores) > 1 else monitores[0]
    x = monitor.x + 20
    y = monitor.y + 20
    root.geometry(f"{ancho}x{alto}+{x}+{y}")

# 🔹 Ventana principal
root = ctk.CTk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.bind("<Button-1>", iniciar_arrastre)
root.bind("<B1-Motion>", mover_ventana)

frame = ctk.CTkFrame(root, corner_radius=15)
frame.pack(fill="both", expand=True, padx=5, pady=5)

header = ctk.CTkFrame(frame, fg_color="transparent")
header.pack(fill="x", padx=10, pady=(10, 5))

btn_elegir = ctk.CTkButton(header, text="Escoger", command=elegir, width=80)
btn_elegir.pack(side="left", padx=5)

btn_limpiar = ctk.CTkButton(header, text="Limpiar", command=limpiar, width=80, fg_color="#444")
btn_limpiar.pack(side="left", padx=5)

btn_cargar = ctk.CTkButton(header, text="Cargar", command=seleccionar_archivo, width=80)
btn_cargar.pack(side="left", padx=5)

btn_cerrar = ctk.CTkButton(header, text="✖", command=cerrar, width=40, fg_color="#d32f2f", hover_color="#b71c1c")
btn_cerrar.pack(side="right", padx=5)

# BOTÓN TOGGLE (visible cuando está colapsado)
toggle_btn = ctk.CTkButton(
    root,
    text="Mostrar",
    command=toggle_view,
    width=120,
    corner_radius=10
)

# botón también dentro del header
btn_toggle = ctk.CTkButton(
    header,
    text="⬇",
    width=40,
    command=toggle_view
)
btn_toggle.pack(side="right", padx=5)

resultado_frame = ctk.CTkFrame(frame, fg_color="transparent")
resultado_frame.pack(expand=True, fill="x", padx=8, pady=8)
label_nombre = ctk.CTkLabel(
    resultado_frame, text="", font=("Segoe UI", 14, "bold"), anchor="w"
)
resultado_frame.columnconfigure(0, weight=1)
resultado_frame.columnconfigure(1, weight=0)

label_nombre.grid(row=0, column=0, sticky="e", pady=0, padx=(0, 0))
btn_quitar = ctk.CTkButton(
    resultado_frame,
    text="✖",
    width=28,
    height=28,
    command=quitar_estudiante,
    fg_color="#d32f2f",
    hover_color="#b71c1c",
    state="disabled",
)
btn_quitar.grid(row=0, column=1, sticky="w", pady=0, padx=(10, 0))

# Center both widgets in the middle of the parent frame horizontally
resultado_frame.grid_columnconfigure(0, weight=1)
resultado_frame.grid_columnconfigure(1, weight=1)

posicionar_ventana(root)

root.mainloop()