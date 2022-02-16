import pyttsx3 # This is the module which will be used to speak the text. 
               #Basically it is the text-to-speech converter library in Python.
               
import datetime # This module supplies classes for manipulating date and time.

import speech_recognition as sr # This module is used to recognise the speech and understand what the user is saying.
                                # Here we are importing the module as sr.

import wikipedia # This module is used to extract the data from the Wikipedia database.

import webbrowser # This module is used to open the browser.

import os # This is the module which is used to perform the system operations.

import smtplib # This module is used to send the email to the user.



engine=pyttsx3.init('sapi5') # SAPI is an API developed by Microsoft to allow the use of speech recognition synthesis within Windows applications.
                             # We are using it here to recongnize the voice of the user.
                             
voices=engine.getProperty('voices') # This is a function which returns a list of all the voices available in the computer.
#print(voices[1].id)

engine.setProperty('voice',voices[0].id) # This is a function which sets the voice of the computer to the first voice in the list.



def speak(audio): # This function is implemented so the AI speaks the audio which will be passed to the function as an arguement.
     engine.say(audio) # This function is implemented so the AI speaks the audio which will be passed to the function as an arguement.
     engine.runAndWait() # This function empties the say queue and returns when all sppeeched text has been spoken.
                         # Without this function the audio will not be audible to us

def wishMe(): # This function is used to wish the user according to the time of the day.
     
     hour=int(datetime.datetime.now().hour) # Storing the current hour of the day.
     if hour>=0 and hour<12: # If the hour is between 0 and 12, the morning greeting will be spoken.
          speak("Good Morning Sir !! Jarvis at your service")
     
     elif hour>= 12 and hour<16: # If the hour is between 12 and 16, the afternoon greeting will be spoken.
          speak("Good Afternoon Sir !! Jarvis always at your service")
     
     elif hour>=16: # If the hour is greater than 16, the evening greeting will be spoken
          speak("Good Evening Sir !! Jarvis always at your service")

def introduction(): #This function is for the introduction of the AI.
     
     speak("I am Jarvis. The Personal AI assistant of Mr. Stark. I assist him in his day to day tasks")

def takeCommand(): # It takes microphone input from the user and returns the string output.
     
     r=sr.Recognizer() # It creates a new Recognizer instance, which represents a collection of speech recognition functionality.
     
     with sr.Microphone() as source: # It creates a new Microphone instance, which represents a physical microphone on the computer 
                                     # And uses it as a source 
          print("Jarvis is listening everything you say")
          
          r.pause_threshold=1 # This is a parameter which is used to determine the pause between the words so that we can take break and speak
          r.energy_threshold=300 # This is a parameter which is used to determine the energy threshold for the speech.
          
          audio=r.listen(source) # Used to listen to the user thorugh source that is microphone.
          
     try:
          print("Recognizing audio...")
          query=r.recognize_google(audio,language='en-in') # This is a function which recognizes the speech and returns the string output.
          print(f"User said: {query}\n") # For printing the said text on the console
          
     except Exception as e:
          print(e) # For printing the error message on the console.
                   # We can comment it if we do not want th error message to be printed on the console.
          print("Say that again please...")
          return "None" # The function returmns None if the user does not speak anything or there is an error

     return query # Return the original string if everything goes fine.

def sendEmail(to,content): # This function is used to send the email to the user.
     
     server=smtplib.SMTP('smtp.gmail.com',587) # Setting up smtp object using gmail's smtp server and port 587 
     server.ehlo() # This is a function which is used to identify the server.
     server.starttls() # Activating the transport layer security to the outgoing mail message.
     server.login('shyaamaltripathi@gmail.com','pinkylalli') # This is the login credentials of the user.
     server.sendmail('shyaamaltripathi@gmail.com',to,content) # This is the function which sends the email to the user.
     server.close() # Closing the server
     
     
if __name__=="__main__":
    wishMe() # Calling the function for wishing the user
    introduction() # Calling the function so as the AI introduces itself.
    
    # Logic for executing tasks based on the query
    while True:  
         query=takeCommand().lower()
         
         if 'wikipedia' in query:
              speak('Alright Sir, It would be a lot better for my processors if you could just tell me the name of the person or object or any stuff that you want to me to search')
              q=takeCommand().lower() # Taking specific name so as to make searching easy
              #query=query.replace("wikipedia","")
              results=wikipedia.summary(q, sentences=2) # This is a function which returns the summary of the page.
              speak("Okay Sir, so according to Wikipedia")
              print(results) # For printing the summary of the page on the console.
              speak(results)
          
         elif 'open youtube' in query:
              speak("Sure Sir")
              webbrowser.open("https://youtube.com") # Opening YouTube in the browser.
          
         elif 'whatsapp' in query:
              speak("Sure Sir")
              webbrowser.open("https://web.whatsapp.com/") # Opening Whatsapp in the browser.
         
         elif 'instagram' in query:
              speak("Sure Sir")
              webbrowser.open("https://www.instagram.com/") # Opening Instagram in the browser.
              
         elif 'my linkedin profile' in query: 
              speak("Sure Sir")
              webbrowser.open("https://www.linkedin.com/in/shyaamal-tripathi-a389051b3/") # Opening LinkedIn in the browser.
          
         elif 'college gmail' in query:
              speak("Sure Sir")
              webbrowser.open("https://mail.google.com/mail/u/0/#inbox") # Opening College Gmail in the browser.
          
         elif 'personal gmail' in query:
              speak("Sure Sir")
              webbrowser.open("https://mail.google.com/mail/u/2/#inbox") # Opening Personal Gmail in the browser.
          
         elif 'hackathon website' in query:
              speak("Sure Sir")
              webbrowser.open("https://hackcbs.tech/") # Opening hackCBS website in the browser.
          
         elif 'open brave' in query:
              speak("Sure Sir")
              webbrowser.open("https://brave.com/") # Opening Brave in the browser.
         
         elif 'github profile' in query:
              speak("Sure Sir")
              webbrowser.open("https://github.com/TripathiShyaamal") # Opening GitHub in the browser.
         
         elif 'discord' in query:
              webbrowser.open("https://discord.com/channels/@me") # Opening Discord in the browser.
         
         elif 'music' in query:
              speak("Ofcourse Sir. Enjoy yourself")
              music_dir='C:\\Users\\hp\\Downloads\\music' # This is the path of the music folder.
              songs=os.listdir(music_dir)
              print(songs)
              os.startfile(os.path.join(music_dir,songs[0])) # This is a function which opens the music file in the music folder.
              # remember random 
         elif 'the time' in query:
              speak("Sure Sir")
              strTime=datetime.datetime.now().strftime("%H:%M:%S")
              speak(f"Sir, the time is {strTime}")
         
         elif 'code editors' in query:
              speak("Sure Sir")
              codePath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # This is the path of the code editor that is VScode
              os.startfile(codePath) # To open the VSCode on the computer.
         
         elif 'family photos' in query:
              speak("Sure Sir")
              Path="C:\\Users\\hp\\Downloads\\Family" # This is the path of the folder that contains the photos of the family.
              os.startfile(Path) # To open the family photos on the computer.
         
         elif 'send email' in query:
              try:
                   speak("What should I say Sir")
                   content=takeCommand() # Taking conten of the email from the user.
                   to="shyaamal1108@gmail.com"
                   sendEmail(to,content) # Calling the function
                   speak("Sir, the mail has been sent")
              except Exception as e:
                   print(e)
                   speak("Sorry Sir but I am unable to send the mail. There might be some error in my processing") # Speaking in case of error
                   
         elif 'thank you' in query:
              speak("You are welcome Sir. It is always a pleasure to be a sidekick of a genius") # Replying to Thank You
              
     
      
