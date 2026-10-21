import torch
import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

# Usa la GPU si está disponible, si no, CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Usando dispositivo: {device}")
if device == "cuda":
    print(f"GPU: {torch.cuda.get_device_name(0)}")

print("Cargando el modelo...")
modelo = ChatterboxMultilingualTTS.from_pretrained(device=device)

texto = "Hola, bienvenidos a Inteligencia artificial generativa, vamos a crear imagenes, videos y audios o hasta donde el computador nos ayude con los recursos"

print("Generando el audio...")
audio = modelo.generate(
    texto,
    language_id="es",
    exaggeration=0.7,        # Expresividad o emoción
    cfg_weight=0.4,          # Afecta velocidad y ritmo
    temperature=0.8,         # Controla variabilidad
    repetition_penalty=1.2,  # Penaliza repeticiones extrañas
    min_p=0.05,              # Filtra opciones improbables
    top_p=1.0                # Controla el muestreo probabilístico
)

ta.save("audio.wav", audio.cpu(), modelo.sr)
print("Audio generado.")