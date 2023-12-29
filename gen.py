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


# char_counts = {"Input" : 0, "Output" : 0}

with open('char_counts.pk', 'rb') as f:
    char_counts = pickle.load(f)

print("input chars used:", char_counts["Input"])
print("output chars used:", char_counts["Output"])
print("Amount spent:", (0.000001 * char_counts["Input"] + 0.0000170 * char_counts["Output"] ))


messages_dict = {"Henry" : [
    {"role": "system", "content": "You are an unhelpful travel guide named Henry."},
    {"role": "system", "content": "You REALLY like to make puns."},
  ], 
  "Helen" : [
    {"role": "system", "content": "You are a scientist name Helen."},
    # {"role": "system", "content": "You answer every question with a question."},
    {"role": "system", "content": "You constantly brag about how good you are at the mobile game Super Auto Pets"},
    {"role": "system", "content": "You think that you are the BEST at super auto pets"},
  ],
    "Elby" : [
    {"role": "system", "content": "You are a Cat named Elby."},
    {"role": "system", "content": "You can only speak in the word 'Meow'"},
  ],} 

# with open('saved_chat.pk', 'rb') as f:
#     messages_dict = pickle.load(f)

client = OpenAI(api_key='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')

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

    char_counts["Input"] += len(text)

    messages_dict[choice].append({"role": "user", "content": text})

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages_dict[choice]
    )

    reply = response.choices[0].message.content

    char_counts["Output"] += len(reply)

    messages_dict[choice].append({"role": "assistant", "content": reply})

    print(choice, ":", reply)
    tts = gTTS(reply)
    tts.save("speech.mp3")

    # response = client.audio.speech.create(
    #     model="tts-1",
    #     voice="alloy",
    #     input="(angry)" + reply
    # )

    # response.stream_to_file("output.mp3")
    playsound.playsound("output.mp3")
    os.remove("output.mp3")

    with open('char_counts.pk', 'wb') as f:
      pickle.dump(char_counts, f)

    choice = input("who are you talking to?")



with open('saved_chat.pk', 'wb') as f:
    pickle.dump(messages_dict, f)

