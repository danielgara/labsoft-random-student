# Selector aleatorio de estudiantes

Aplicación de escritorio para Windows y macOS que muestra un **selector aleatorio de estudiantes** en una ventana flotante. Pensada para usarla durante clases, mientras presentas con PowerPoint, Keynote u otro software.

La ventana queda siempre visible encima de tus diapositivas para elegir un estudiante al azar sin salir de la presentación.

No necesitas instalar Python.

---

## Descargar (usuario final)

1. Abre el repositorio:  
   [https://github.com/danielgara/python-estudiante-aleatorio](https://github.com/danielgara/python-estudiante-aleatorio)
2. Haz clic en **Code** → **Download ZIP**
3. Descomprime el ZIP en la carpeta que prefieras

### Windows

- Usa el archivo **`popup.exe`**
- Requisitos: Windows 10 o superior

### macOS

- Usa la aplicación **`popup.app`**
- Requisitos: macOS reciente (Apple Silicon o Intel, según el build que descargues)

> **Tip:** También puedes clonar el repositorio con `git clone` si prefieres; el uso de la app es el mismo.

---

## Cómo usar (modo usuario final)

### 1. Preparar la lista de estudiantes

Edita el archivo `estudiantes.txt` y escribe **un nombre por línea**:

```txt
MARIA SUAREZ
CAMILO ARTEAGA
ALEJANDRO ROMERO
```

Guárdalo en la **misma carpeta** que el ejecutable:

| Sistema | Archivo de la app | Coloca `estudiantes.txt` junto a… |
|---------|-------------------|-----------------------------------|
| Windows | `popup.exe`       | `popup.exe`                       |
| macOS   | `popup.app`       | `popup.app`                       |

### 2. Abrir la aplicación

**Windows**

1. Haz doble clic en `popup.exe`
2. Si Windows SmartScreen avisa: **Más información** → **Ejecutar de todas formas**  
   (o clic derecho → **Propiedades** → marcar **Desbloquear**, si aparece)

**macOS**

1. Haz doble clic en `popup.app`
2. Si macOS bloquea la app (“no se puede abrir porque es de un desarrollador no identificado”):
   - Clic derecho (o Control + clic) sobre `popup.app` → **Abrir** → confirma **Abrir**
   - O ve a **Ajustes del Sistema** → **Privacidad y seguridad** y permite abrir la app

La ventana aparece en la esquina superior izquierda del monitor secundario (si tienes dos pantallas) o del monitor principal.

### 3. Botones

| Botón | Acción |
|-------|--------|
| **Escoger** | Selecciona un estudiante al azar de la lista |
| **Limpiar** | Borra el nombre mostrado |
| **Cargar** | Abre un archivo `.txt` distinto con otra lista |
| **✖** (junto al nombre) | Quita al estudiante seleccionado de la lista actual |
| **⬇** | Minimiza la ventana a un botón pequeño **Mostrar** |
| **✖** (rojo, arriba a la derecha) | Cierra la aplicación |

### 4. Mover la ventana

Arrastra la ventana desde cualquier zona que no sea un botón.

---

## Uso con PowerPoint / Keynote

1. Abre la presentación en **modo ventana** (evita pantalla completa exclusiva si la app queda detrás)
2. Ejecuta `popup.exe` (Windows) o `popup.app` (macOS)
3. Coloca la ventana en el monitor del profesor o en un rincón visible
4. Durante la clase, pulsa **Escoger** cuando quieras llamar a alguien al azar

> Si la ventana queda detrás, abre primero la presentación y luego la app.

---

## Cambiar de lista sin editar el archivo

1. Pulsa **Cargar**
2. Elige otro `.txt` (un nombre por línea)
3. La app usará esa lista de inmediato

---

## Solución de problemas

| Problema | Qué hacer |
|----------|-----------|
| Aparece "Sin estudiantes" | Verifica que `estudiantes.txt` esté junto a `popup.exe` / `popup.app` y tenga al menos un nombre |
| La ventana no se ve encima de la presentación | Usa modo ventana en PowerPoint/Keynote y vuelve a abrir la app |
| Windows bloquea el `.exe` | Desbloquear en Propiedades, o permitir en el antivirus / SmartScreen |
| macOS bloquea `.app` | Clic derecho → **Abrir**, o permitir en Privacidad y seguridad |

---

## Ejecutar desde código fuente (opcional, desarrolladores)

**Requisitos:** Python 3.8+

```bash
pip install screeninfo==0.8.1 customtkinter==5.1.3
python popup.py
```

Generar ejecutables con PyInstaller:

```bash
# Windows → .exe
pip install pyinstaller
pyinstaller --onefile --windowed popup.py

# macOS → .app
pip install pyinstaller
pyinstaller --windowed popup.py
```

Los artefactos quedan en `dist/`.

---

## Licencia

Uso libre para fines educativos y personales.
```