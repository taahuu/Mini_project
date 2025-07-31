import speech_recognition as sr
import pyttsx3
import webbrowser


# Initialize recognizer
# recognizer = sr.Recognizer()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=UrsmFxEIp5k&t=27953s")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
    

if __name__ == "__main__":
    print("Voice Assistant is now listening...")
    # speak("Voice Assistant is now listening...")
    
    while True:
        
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                    print("Listening......")
                    # speak("Listening...")
                    audio = r.listen(source,timeout=2 )
            word = r.recognize_google(audio)
            print(word)  
            if word.lower()== 'exit' or word.lower()== 'stop':
                speak("Goodbye")
                print("Goodbye")
                break   
            
            elif word.lower()== 'hello buddy':
                # speak("Hey Taha, How are you...")
                print('Hey Taha, How are you...')
                
                with sr.Microphone() as source:
                    print("Say Something......")
                    
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)
                    processCommand(command)
                    print("processing..")
                    
        except Exception as e:
            print(e)

