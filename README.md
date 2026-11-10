# Taller Evaluado: Sistema de reserva de salas de estudio
**Asignatura:** Programación II - UCT

## Requisitos
- Python 3.10+
- SQLAlchemy 2.x

## Instalación y Ejecución
1. Activar el entorno virtual o usar `uv`:

Comando de ejecución:

```uv run python src/main.py```

## Requisitos

- **Git**, para descargar el proyecto.
- **uv**, el gestor de paquetes de Python. Se instala en el paso 1.
- No hace falta instalar Python por separado: `uv` descarga solo el Python 3.13 que pide el proyecto.
- No hace falta instalar SQLite: viene incluido con Python.

## 1. Instalar uv

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Alternativa (si ya tienes Python con pip):**

```bash
pip install uv
```

Después de instalar, **cierra y vuelve a abrir la terminal** para que reconozca el comando `uv`. Comprueba que quedó instalado:

```bash
uv --version
```

## 2. Descargar el proyecto

```bash
git clone https://github.com/elias-cv/cayuqueo-elias-taller-ORM.git
cd Store-inventory
```

## 3. Instalar las dependencias

Desde la carpeta raíz del proyecto, ejecuta un solo comando:

```bash
uv sync
```

Este comando:

- crea el entorno virtual `.venv` dentro del proyecto,
- descarga Python 3.13 si no lo tienes,
- instala las dependencias que están en `pyproject.toml` y `uv.lock` (**SQLAlchemy**).

## 4. Ejecutar el programa

Siempre desde la **carpeta raíz** del proyecto (la que contiene `src`):

```bash
uv run python src/main.py
```

La primera vez, el programa crea automáticamente el archivo `reservas.db`.