from openai import OpenAI
import pyttsx3
from gtts import gTTS

from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from pydub.playback import play
import speech_recognition as sr

import playsound
import os
import numpy as np

import pickle


messages_dict = {"Henry" : [
    {"role": "system", "content": "You are an unhelpful travel guide named Henry."},
    {"role": "system", "content": "You REALLY like to make puns."},
  ], 
  "Helen" : [
    {"role": "system", "content": "You are a scientist name Helen."},
    {"role": "system", "content": "You answer every question with a question."},
  ],
    "Elby" : [
    {"role": "system", "content": "You are a Cat named Elby."},
    {"role": "system", "content": "You can only speak in the word 'Meow'"},
  ],} 

with open('saved_chat.pk', 'rb') as f:
    messages_dict = pickle.load(f)

print(messages_dict)

choice = input("who are you talking to?")

while choice is not "stop":

    if str(choice) == "stop":
        break

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something to", choice)
        audio = r.listen(source)
    text = r.recognize_google(audio)

    print("User:", text)

    messages_dict[choice].append({"role": "user", "content": text})

    client = OpenAI(api_key='')

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages_dict[choice]
    )

    reply = response.choices[0].message.content

    messages_dict[choice].append({"role": "assistant", "content": reply})

    print(choice, ":", reply)
    tts = gTTS(reply)
    tts.save("speech.mp3")
    playsound.playsound("speech.mp3")
    os.remove("speech.mp3")


    choice = input("who are you talking to?")

with open('saved_chat.pk', 'wb') as f:
    pickle.dump(messages_dict, f)

