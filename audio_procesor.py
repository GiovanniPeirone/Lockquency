import librosa
import numpy as np
import sounddevice as sd
import os

procesed_json_path = "./data/procesed/"

def AudioProcessor(path, object_name):
    pass

def AudioFolderList(path):
    return os.listdir(path)

def AudioData(audio_path):
    print(audio_path)

    y, sr = librosa.load(audio_path, sr=None)
    
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

    return [
        half_n,
        fft_pos,
        umbral,
        indices
    ]

def AudioMaxAmp(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    return np.max(y)

def AudioMinAmp(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    return np.min(y)

def AudioPlay():
    pass