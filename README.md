# Chatterbox Text-to-Speech

Proyecto de generación de audio a partir de texto utilizando **Chatterbox Multilingual TTS**, un modelo de inteligencia artificial para la síntesis de voz multilingüe.

El proyecto permite generar audio en español a partir de un texto definido en Python. También detecta automáticamente si hay una GPU compatible con CUDA disponible para aprovechar la aceleración por hardware.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **PyTorch:** procesamiento y ejecución del modelo de inteligencia artificial.
- **TorchAudio:** manejo y exportación de audio.
- **Chatterbox Multilingual TTS:** modelo de generación de voz.
- **uv:** gestión de dependencias y entorno de desarrollo.
- **CUDA:** aceleración por GPU NVIDIA, cuando está disponible.

## Estructura del proyecto

```text
text-to-speech-chatterbox/
├── src/
│   └── text_to_speech_chatterbox/
│       └── __init__.py
├── .gitignore
├── .python-version
├── README.md
├── audio.wav
├── pyproject.toml
└── uv.lock
```

### Descripción de los archivos

- `src/text_to_speech_chatterbox/`: paquete principal del proyecto.
- `__init__.py`: archivo que identifica el directorio como un paquete de Python.
- `.gitignore`: especifica los archivos y directorios que Git debe ignorar.
- `.python-version`: indica la versión de Python configurada para el proyecto.
- `README.md`: documentación del proyecto.
- `audio.wav`: archivo de audio generado durante la ejecución.
- `pyproject.toml`: configuración del proyecto y declaración de sus dependencias.
- `uv.lock`: archivo de bloqueo que registra las versiones resueltas de las dependencias.

## Requisitos previos

- Python compatible con las dependencias del proyecto.
- `uv` instalado.
- Conexión a Internet para descargar las dependencias y los archivos del modelo.
- GPU NVIDIA compatible con CUDA, opcional.

## Instalación

Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Accede al directorio del proyecto:

```bash
cd <NOMBRE_DEL_REPOSITORIO>
```

Instala las dependencias definidas en el proyecto:

```bash
uv sync
```

Este comando prepara el entorno virtual del proyecto e instala las dependencias declaradas en `pyproject.toml`, utilizando `uv.lock` cuando corresponda.

## Funcionamiento

El programa realiza las siguientes operaciones:

1. Comprueba si CUDA está disponible y selecciona la GPU o la CPU.
2. Carga el modelo Chatterbox Multilingual TTS.
3. Define el texto que se convertirá en voz.
4. Genera el audio en español utilizando los parámetros de síntesis configurados.
5. Guarda el resultado en formato WAV mediante TorchAudio.

## Parámetros de generación

La implementación utiliza los siguientes parámetros:

| Parámetro | Descripción |
|---|---|
| `language_id="es"` | Selecciona el español. |
| `exaggeration=0.7` | Controla la expresividad de la voz. |
| `cfg_weight=0.4` | Ajusta el condicionamiento durante la generación. |
| `temperature=0.8` | Controla la variabilidad de la generación. |
| `repetition_penalty=1.2` | Ayuda a reducir repeticiones no deseadas. |
| `min_p=0.05` | Filtra opciones con probabilidades bajas. |
| `top_p=1.0` | Configura el muestreo probabilístico. |

Los valores pueden modificarse para experimentar con diferentes resultados de voz.

## Resultado

El programa genera el archivo `audio.wav`, que contiene el audio sintetizado y puede reproducirse con cualquier reproductor compatible con el formato WAV.

La velocidad de generación depende de los recursos del equipo, del dispositivo seleccionado y de la configuración del modelo.

## Consideraciones

- La primera ejecución puede tardar más debido a la descarga y carga del modelo.
- La ejecución en GPU requiere una instalación de PyTorch compatible con CUDA.
- La ejecución en CPU puede ser más lenta, dependiendo del hardware.
- El audio generado es un archivo de salida y puede excluirse del control de versiones si no es necesario compartirlo en el repositorio.
- Consulta las condiciones de uso y licencia del modelo y sus dependencias antes de distribuir los resultados con fines comerciales.

## Licencia

La licencia de este proyecto debe definirse según las condiciones de uso del código, del modelo Chatterbox Multilingual TTS y de sus dependencias.
