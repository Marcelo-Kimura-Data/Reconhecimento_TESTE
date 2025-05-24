import speech_recognition as sr
# Arroz, feijão, e Batata
rec = sr.Recognizer()

with sr.AudioFile("teste.wav") as arquivo_audio:
    audio = rec.record(arquivo_audio)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
