
# coding: utf-8

# In[19]:

#!pip install SpeechRecognition


# In[24]:

get_ipython().system('pip install pyaudio')


# In[33]:

get_ipython().system('pip install google-api-python-client')


# In[2]: !

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Please: ')
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print('You said: {}'.format(text))
    except:
        print("Sorry")

