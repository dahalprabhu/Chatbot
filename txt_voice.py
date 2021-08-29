import speech_recognition as sr
import pyttsx3 as pyt

engine=pyt.init()
r=sr.Recognizer()
program=True
while program:
 with sr.Microphone() as source:
    print("Speak anything")
    audio=r.listen(source)
    try:

      text=r.recognize_google(audio)
      print(f"You said : {text}")
      engine.setProperty("rate",150)
      engine.say(text)
      engine.runAndWait()
      if (text=="exit")|(text=="quit"):
        program=False
      else:
          program=True

    except:
        print("Sorry couldnot recognize your voice")

