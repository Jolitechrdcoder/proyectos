import pyttsx3 as voz
import speech_recognition as sr
import subprocess as sub

from datetime import datetime

#configuracion de la voz del asistente
voice=voz.init()
voices=voice.getProperty('voices')
voice.setProperty('voice',voices[0].id)
voice.setProperty('rate',140)

def say(text):
    voice.say(text)
    voice.runAndWait()

while True:
    recognizer=sr.Recognizer()
#Activar microfono
    with sr.Microphone() as source:
        print('Escuchando...')
        audio=recognizer.listen(source, phrase_time_limit=3)
    
    try:
        comando=recognizer.recognize_google(audio, language='es-ES')
        print(f'Creo que dijiste "{comando}"')

        comando=comando.lower()
        comando=comando.split(' ')

        if 'Xor' in comando:

            if 'abre' in comando or 'abrir' in comando:

                sites={
                    'google':'google.com',
                    'youtube':'youtube.com'
                }

                for i in list(sites.keys()):
                    if i in comando:
                        sub.call(f'start msedge.exe {sites[i]}', shell=True)
                        say(f'Abriendo {i}')
            
            elif 'hora' in comando:
                time=datetime.now().strftime('%H:%M')
                say(f'Son las {time}, Jorge dejame vivir!')


                if 'termina'in comando or 'terminar'in comando or 'término' in comando or 'terminó' in comando:
                    say('Sesión finalizada')
                    break

    except:#si no se reconoce tu voz pedira volver a repetir
        print('No te comprendi Señor jorge, Podria repetir la instruccion')