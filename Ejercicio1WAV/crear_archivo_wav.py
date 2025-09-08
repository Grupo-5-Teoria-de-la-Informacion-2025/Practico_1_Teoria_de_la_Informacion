import wave
import struct
import math

def crear_archivo_wav_prueba():
    """
    Crea un archivo .wav de prueba con un tono sinusoidal
    """
    # Parámetros del audio
    frecuencia = 440  # Hz (nota La)
    duracion = 3  # segundos
    sample_rate = 44100  # Hz
    amplitud = 0.3
    
    # Calcular número de muestras
    num_muestras = int(sample_rate * duracion)
    
    # Crear el archivo WAV
    with wave.open('prueba.wav', 'w') as wav_file:
        # Configurar parámetros
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16 bits
        wav_file.setframerate(sample_rate)
        
        # Generar datos de audio (tono sinusoidal)
        for i in range(num_muestras):
            # Calcular valor de la onda sinusoidal
            valor = amplitud * math.sin(2 * math.pi * frecuencia * i / sample_rate)
            # Convertir a entero de 16 bits
            valor_int = int(valor * 32767)
            # Escribir al archivo
            wav_file.writeframes(struct.pack('<h', valor_int))
    
    print("Archivo 'prueba.wav' creado exitosamente!")
    print(f"Características: {frecuencia} Hz, {duracion}s, {sample_rate} Hz, Mono, 16-bit")

if __name__ == "__main__":
    crear_archivo_wav_prueba()
