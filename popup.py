import sys
from pathlib import Path

import customtkinter as ctk
import random
from screeninfo import get_monitors
from tkinter import filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def cargar_estudiantes(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]

def ruta_estudiantes():
    nombre = "estudiantes.txt"
    candidatos = []
    if getattr(sys, "frozen", False):
        exe = Path(sys.executable).resolve()
        candidatos.append(exe.parent / nombre)
        if exe.parent.name == "MacOS":
            candidatos.append(exe.parent.parent.parent.parent / nombre)
        if hasattr(sys, "_MEIPASS"):
            candidatos.append(Path(sys._MEIPASS) / nombre)
    else:
        candidatos.append(Path(__file__).resolve().parent / nombre)
    for ruta in candidatos:
        if ruta.exists():
            return ruta
    return None

ruta_inicial = ruta_estudiantes()
estudiantes = cargar_estudiantes(ruta_inicial) if ruta_inicial else []
estudiante_actual = None

offset_x = 0
offset_y = 0
arrastrando = False
collapsed = False
_animando = False

COLOR_NOMBRE = "#f9fafb"
COLOR_PLACEHOLDER = "#9ca3af"
ANIM_CARD_H = 60
ANIM_CENTER_Y = ANIM_CARD_H // 2

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

def _widget_es_interactivo(widget):
    """Evita arrastrar la ventana al hacer clic en botones o etiquetas."""
    while widget is not None:
        if isinstance(widget, (ctk.CTkButton, ctk.CTkEntry, ctk.CTkOptionMenu)):
            return True
        widget = widget.master
    return False

def iniciar_arrastre(event):
    global offset_x, offset_y, arrastrando
    if _widget_es_interactivo(event.widget):
        arrastrando = False
        return
    arrastrando = True
    offset_x = event.x_root - root.winfo_x()
    offset_y = event.y_root - root.winfo_y()

def mover_ventana(event):
    if not arrastrando:
        return
    x = root.winfo_pointerx() - offset_x
    y = root.winfo_pointery() - offset_y
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{x}+{y}")

def fin_arrastre(_event):
    global arrastrando
    arrastrando = False

def elegir():
    global estudiante_actual
    if _animando:
        return
    if not estudiantes:
        estudiante_actual = None
        label_nombre.configure(text="Sin estudiantes", text_color=COLOR_PLACEHOLDER)
        label_nombre.place_configure(y=ANIM_CENTER_Y)
        btn_quitar.configure(state="disabled")
        return
    estudiante_actual = random.choice(estudiantes)
    animar_seleccion(estudiante_actual)

def limpiar():
    global estudiante_actual
    estudiante_actual = None
    label_nombre.configure(text="Presiona Escoger", text_color=COLOR_PLACEHOLDER)
    label_nombre.place_configure(y=ANIM_CENTER_Y)
    btn_quitar.configure(state="disabled")

def quitar_estudiante():
    global estudiantes, estudiante_actual
    if estudiante_actual and estudiante_actual in estudiantes:
        estudiantes.remove(estudiante_actual)
    estudiante_actual = None
    label_nombre.configure(text="Presiona Escoger", text_color=COLOR_PLACEHOLDER)
    label_nombre.place_configure(y=ANIM_CENTER_Y)
    btn_quitar.configure(state="disabled")

def animar_seleccion(final):
    global _animando
    _animando = True
    btn_quitar.configure(state="disabled")
    label_nombre.configure(text_color=COLOR_NOMBRE)

    pasos = [(16, 10)] * 6 + [(11, 12)] * 3 + [(7, 15)] * 3
    total = len(pasos)

    def _caer(y, destino, step, fdelay, done):
        label_nombre.place_configure(y=y)
        if y < destino:
            root.after(fdelay, lambda: _caer(min(y + step, destino),
                                             destino, step, fdelay, done))
        else:
            done()

    def _correr(i):
        if i >= total:
            label_nombre.configure(text=final)
            _caer(-22, ANIM_CENTER_Y, 6, 15, _terminar)
            return
        label_nombre.configure(text=random.choice(estudiantes))
        step, fdelay = pasos[i]
        _caer(-22, ANIM_CARD_H + 22, step, fdelay, lambda: _correr(i + 1))

    _correr(0)

def _terminar():
    global _animando
    _animando = False
    label_nombre.place_configure(y=ANIM_CENTER_Y)
    btn_quitar.configure(state="normal")

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
        root.geometry("380x150")
        toggle_btn.place_forget()
        collapsed = False


def posicionar_ventana(root, ancho=380, alto=150):
    monitores = get_monitors()
    monitor = monitores[1] if len(monitores) > 1 else monitores[0]
    x = monitor.x + 20
    y = monitor.y + 20
    root.geometry(f"{ancho}x{alto}+{x}+{y}")

# 🔹 Ventana principal
root = ctk.CTk()
root.title("")

if sys.platform == "darwin":
    try:
        from AppKit import NSApplication, NSApplicationActivationPolicyAccessory
        NSApplication.sharedApplication().setActivationPolicy_(
            NSApplicationActivationPolicyAccessory
        )
    except Exception:
        pass

root.attributes("-topmost", True)
root.bind("<Button-1>", iniciar_arrastre)
root.bind("<B1-Motion>", mover_ventana)
root.bind("<ButtonRelease-1>", fin_arrastre)

frame = ctk.CTkFrame(root, corner_radius=15)
frame.pack(fill="both", expand=True, padx=5, pady=5)

header = ctk.CTkFrame(frame, fg_color="transparent")
header.pack(fill="x", padx=10, pady=(10, 5))

btn_elegir = ctk.CTkButton(header, text="Escoger", command=elegir, width=80,
                           fg_color="#22c55e", hover_color="#16a34a")
btn_elegir.pack(side="left", padx=5)

btn_limpiar = ctk.CTkButton(header, text="Limpiar", command=limpiar, width=80,
                            fg_color="#374151", hover_color="#4b5563")
btn_limpiar.pack(side="left", padx=5)

btn_cargar = ctk.CTkButton(header, text="Cargar", command=seleccionar_archivo, width=80,
                           fg_color="#2563eb", hover_color="#1d4ed8")
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

tarjeta = ctk.CTkFrame(frame, corner_radius=12, fg_color="#1f2937", height=ANIM_CARD_H)
tarjeta.pack(fill="x", padx=12, pady=(4, 10))
tarjeta.pack_propagate(False)

btn_quitar = ctk.CTkButton(
    tarjeta,
    text="✖",
    width=28,
    height=28,
    command=quitar_estudiante,
    fg_color="#d32f2f",
    hover_color="#b71c1c",
    state="disabled",
)
btn_quitar.pack(side="right", padx=(6, 10))

viewport = ctk.CTkFrame(tarjeta, fg_color="transparent")
viewport.pack(side="left", fill="both", expand=True)

label_nombre = ctk.CTkLabel(
    viewport,
    text="Presiona Escoger",
    font=("Segoe UI", 12, "bold"),
    text_color=COLOR_PLACEHOLDER,
)
label_nombre.place(relx=0.5, y=ANIM_CENTER_Y, anchor="center")

posicionar_ventana(root)

root.mainloop()