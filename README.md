# Selector aleatorio de estudiantes

Pequeña aplicación para Windows que muestra un **selector aleatorio de estudiantes** en una ventana flotante. Está pensada para usarla durante clases, mientras presentas con PowerPoint u otro software.

La ventana queda siempre visible encima de tus diapositivas para que puedas elegir un estudiante al azar sin salir de la presentación.

---

## Descargar

### Opción 1: Clonar el repositorio

```bash
git clone https://github.com/danielgara/python-estudiante-aleatorio.git
cd python-estudiante-aleatorio
```

### Opción 2: Descargar como ZIP

1. Abre [https://github.com/danielgara/python-estudiante-aleatorio](https://github.com/danielgara/python-estudiante-aleatorio)
2. Haz clic en **Code** → **Download ZIP**
3. Descomprime el archivo en la carpeta que prefieras

---

## Requisitos

- **Windows 10 o superior**
- No necesitas instalar Python: el proyecto incluye `popup.exe`, un ejecutable listo para usar

---

## Cómo usar

### 1. Preparar la lista de estudiantes

Edita el archivo `estudiantes.txt` y escribe **un nombre por línea**:

```txt
MARIA SUAREZ
CAMILO ARTEAGA
ALEJANDRO ROMERO
```

Guarda el archivo en la **misma carpeta** que `popup.exe`.

### 2. Ejecutar la aplicación

Haz doble clic en `popup.exe`.

La ventana aparecerá en la esquina superior izquierda del monitor secundario (si tienes dos pantallas) o del monitor principal.

### 3. Botones

| Botón | Acción |
|-------|--------|
| **Escoger** | Selecciona un estudiante al azar de la lista |
| **Limpiar** | Borra el nombre mostrado |
| **Cargar** | Abre un archivo `.txt` distinto con otra lista de estudiantes |
| **✖** (junto al nombre) | Quita al estudiante seleccionado de la lista actual |
| **⬇** | Minimiza la ventana a un botón pequeño **Mostrar** |
| **✖** (rojo, arriba a la derecha) | Cierra la aplicación |

### 4. Mover la ventana

Arrastra la ventana desde cualquier zona que no sea un botón para colocarla donde te resulte más cómodo.

---

## Uso con PowerPoint (recomendado)

Para que la ventana flotante funcione bien sobre tu presentación:

1. Abre PowerPoint en **modo ventana** (no en pantalla completa exclusiva)
2. Ejecuta `popup.exe`
3. Coloca la ventana en el monitor del profesor o en un rincón visible
4. Durante la clase, pulsa **Escoger** cuando quieras llamar a alguien al azar

> **Nota:** Si la ventana queda detrás de la presentación, abre primero PowerPoint y luego ejecuta la aplicación. El modo ventana de PowerPoint suele dar mejores resultados que el modo presentación a pantalla completa.

---

## Personalizar la lista sin editar el archivo

1. Pulsa **Cargar**
2. Elige otro archivo `.txt` con un nombre por línea
3. La app usará esa lista de inmediato

---

## Ejecutar desde código fuente (opcional)

Si prefieres modificar la aplicación o ejecutarla con Python:

**Requisitos:** Python 3.8+

```bash
pip install screeninfo==0.8.1 customtkinter==5.1.3
python popup.py
```

Para generar tu propio `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed popup.py
```

El ejecutable se creará en la carpeta `dist/`.

---

## Solución de problemas

| Problema | Qué hacer |
|----------|-----------|
| Aparece "Sin estudiantes" | Verifica que `estudiantes.txt` esté junto a `popup.exe` y tenga al menos un nombre |
| La ventana no se ve encima de PowerPoint | Usa modo ventana en PowerPoint y vuelve a abrir `popup.exe` |
| Windows bloquea el `.exe` | Clic derecho → **Propiedades** → marcar **Desbloquear** (si aparece), o permitir la app en el antivirus |

---

## Licencia

Uso libre para fines educativos y personales.
