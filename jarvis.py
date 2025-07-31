# import speech_recognition as sr
# import pyttsx3

# # Initialize recognizer and speech engine
# recognizer = sr.Recognizer()
# # engine = pyttsx3.init()

# # def speak(text):
# #     engine.say(text)
# #     engine.runAndWait()

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()  # optional, ensures it's properly closed



# if __name__ == "__main__":
#     print("Voice Assistant is now listening...")
#     # speak("Voice Assistant is now listening...")

#     while True:
#         with sr.Microphone() as source:
#             print("Listening......")
#             # speak("Listening......")
#             audio = recognizer.listen(source)

#         try:
#             command = recognizer.recognize_google(audio)
#             print("You said:", command)
#             # speak(command)

#             if command.lower() in ['exit', 'stop']:
#                 speak("Goodbye!")
#                 break

#             elif command.lower()== 'taha':
#                 response = "Hey Taha, how are you?"
#                 speak(response)
#                 print(response)

#         except sr.UnknownValueError:
#             print("Sorry, I did not understand that.")
#         except sr.RequestError:
#             print("Could not request results from Google Speech Recognition service.")
#         except Exception as e:
#             print("Error:", e)
            
            
            
            
            
            




import speech_recognition as sr
import pyttsx3


# Initialize recognizer
# recognizer = sr.Recognizer()



def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
    

if __name__ == "__main__":
    print("Voice Assistant is now listening...")
    # speak("Voice Assistant is now listening...")
    
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening......")
                # speak("Listening...")
                audio = r.listen(source)
        
        try:
            command = r.recognize_google(audio)
            print(command)  
            if command.lower()== 'exit' or command.lower()== 'stop':
                speak("Goodbye")
                print("Goodbye")
                break   
            
            elif command.lower()== 'taha':
                speak("Hey Taha, How are you...")
                print('Hey Taha, How are you...')
        except Exception as e:
            print(e)

