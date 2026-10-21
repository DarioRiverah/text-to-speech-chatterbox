# Chatterbox Text-to-Speech

Proyecto de generación de audio a partir de texto utilizando **Chatterbox Multilingual TTS**, un modelo de inteligencia artificial capaz de convertir texto en voz en diferentes idiomas.

Esta implementación genera audio en español y utiliza la GPU mediante CUDA cuando está disponible. Si no hay una GPU compatible, ejecuta el modelo en la CPU.

## Características

- Generación de voz a partir de texto en español.
- Uso de Chatterbox Multilingual TTS.
- Detección automática del dispositivo disponible (GPU o CPU).
- Configuración de parámetros para controlar la expresividad y la variabilidad de la voz.
- Exportación del audio generado en formato WAV.

## Tecnologías utilizadas

- Python
- PyTorch
- TorchAudio
- Chatterbox Multilingual TTS
- CUDA (opcional, para aceleración mediante GPU compatible)

## Requisitos previos

- Python compatible con las versiones de Chatterbox y PyTorch instaladas.
- `uv` para la gestión del entorno y las dependencias.
- Conexión a Internet para descargar las dependencias y los archivos del modelo durante la primera ejecución.
- GPU NVIDIA compatible con CUDA, opcional.

## Instalación

Clona el repositorio y accede a la carpeta del proyecto:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

Crea el entorno virtual:

```bash
uv venv
```

En Windows PowerShell, activa el entorno:

```powershell
.venv\Scripts\Activate.ps1
```

Instala PyTorch, TorchAudio y Chatterbox Multilingual TTS siguiendo las instrucciones oficiales de instalación compatibles con tu sistema operativo y versión de Python.

Si las dependencias ya están declaradas en `pyproject.toml`, puedes instalarlas con:

```bash
uv sync
```

## Ejecución

Ejecuta el script principal:

```bash
uv run main.py
```

El programa detectará si CUDA está disponible, cargará el modelo, generará el audio a partir del texto definido en el código y guardará el resultado en `audio.wav`.

## Configuración de la generación

El modelo utiliza los siguientes parámetros:

| Parámetro | Descripción |
|---|---|
| `language_id="es"` | Selecciona el español. |
| `exaggeration=0.7` | Ajusta la expresividad de la voz. |
| `cfg_weight=0.4` | Ajusta el condicionamiento de la generación. |
| `temperature=0.8` | Controla la variabilidad de la generación. |
| `repetition_penalty=1.2` | Ayuda a reducir repeticiones no deseadas. |
| `min_p=0.05` | Filtra opciones con probabilidades bajas. |
| `top_p=1.0` | Configura el muestreo probabilístico. |

Estos valores pueden modificarse para experimentar con diferentes resultados de voz.

## Archivo generado

Al finalizar la ejecución, se crea el archivo:

```text
audio.wav
```

Este archivo contiene el audio generado por el modelo y puede reproducirse con cualquier reproductor compatible con el formato WAV.

## Consideraciones

- La primera ejecución puede tardar más debido a la descarga y carga del modelo.
- La generación de audio consume recursos de memoria y procesamiento.
- El rendimiento depende del hardware disponible.
- Para utilizar CUDA, se necesita una instalación compatible de PyTorch y sus dependencias.
- El texto que se convertirá en voz se modifica directamente en el script principal.

## Licencia

Consulta las condiciones de licencia de Chatterbox y de sus dependencias antes de utilizar el proyecto o distribuir los audios generados con fines comerciales.
