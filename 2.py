import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as src:
    print("say something...")
    aud = rec.listen(src)

try:
    text = rec.recognize_google(aud, language="en-US")
    print(text)
except sr.UnknownValueError:
    print("i don't understand you")
except sr.RequestError as e:
    print({e})
