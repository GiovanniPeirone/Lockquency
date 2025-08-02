import librosa
import numpy as np
import sounddevice as sd

from audio_procesor import AudioProcessor 

"""
y, sr = librosa.load("./data/sounds/cats/cat0.wav", sr=None)


# Datos básicos
print(f"Duración: {librosa.get_duration(y=y, sr=sr):.2f} segundos")
print(f"Frecuencia de muestreo: {sr} Hz")
print(f"Número de muestras: {len(y)}")

# Amplitud máxima y mínima
print(f"Amplitud máxima: {np.max(y)}")
print(f"Amplitud mínima: {np.min(y)}")

# RMS (Root Mean Square) - nivel de energía
rms = librosa.feature.rms(y=y)
print(f"Energía RMS media: {np.mean(rms):.4f}")

tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

# Si es un array, tomar el primer valor
if isinstance(tempo, np.ndarray):
    tempo = tempo[0]

print(f"Tempo estimado: {tempo:.2f} BPM")

print(f"Beats detectados: {len(beats)}")

# MFCCs (coeficientes cepstrales)
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
print(f"MFCC shape: {mfccs.shape}")

# Espectrograma
S = librosa.stft(y)
S_db = librosa.amplitude_to_db(abs(S))
print(f"Espectrograma shape: {S_db.shape}")


#Reproduce
# Generar onda combinada
t = np.linspace(0, librosa.get_duration, int(sr * librosa.get_duration), endpoint=False)
onda = sum(np.sin(2 * int(np.pi) * f * t) for f in sr)

# Normalizar para que no sature
onda = onda / np.max(np.abs(onda))

# Reproducir
sd.play(onda, sr)
sd.wait()






"""

def main():
    AudioProcessor("./data/sounds/cats/", "cat")
if __name__ == '__main__':
    main()
    exit()

"""

# Cargar audio
y, sr = librosa.load("./data/sounds/cats/cat0.wav", sr=None)

# Duración del audio
duration = librosa.get_duration(y=y, sr=sr)

# FFT (transformada rápida de Fourier)
fft = np.fft.fft(y)
freqs = np.fft.fftfreq(len(y), 1/sr)

# Tomar solo la mitad positiva de frecuencias (por simetría)
half_n = len(y)//2
freqs_pos = freqs[:half_n]
fft_pos = fft[:half_n]

# Opcional: filtrar para quedarte solo con las frecuencias con amplitud alta
umbral = np.max(np.abs(fft_pos)) * 0.1  # ejemplo: tomar frecuencias > 10% de la máxima amplitud
indices = np.where(np.abs(fft_pos) > umbral)[0]

# Reconstruir la señal solo con esas frecuencias "fuertes"
t = np.linspace(0, duration, len(y), endpoint=False)
reconstructed = np.zeros_like(t, dtype=np.float64)

for i in indices:
    amplitude = np.abs(fft_pos[i]) / half_n
    phase = np.angle(fft_pos[i])
    freq = freqs_pos[i]
    reconstructed += amplitude * np.cos(2 * np.pi * freq * t + phase)

# Normalizar para evitar saturación
reconstructed /= np.max(np.abs(reconstructed))

# Reproducir señal reconstruida con frecuencias principales
sd.play(reconstructed, sr)
sd.wait()

"""