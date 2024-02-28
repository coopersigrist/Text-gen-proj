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


client = OpenAI(api_key=)

response = client.images.generate(
  model="dall-e-3",
  prompt="Radical ring-opening polymerization (rROP) of cyclic ketene acetals (CKAs) provides a chain-growth polymerization pathway for polyester synthesis. The radical polymerizations of 2-methylene-1,3,6-trioxocane (MTC) and 5,6-benzo-2-methylene-1,3-dioxepane (BMDO) were investigated, where different radical initiation, termination and transfer pathways were observed. The semi-batch copolymerization of these CKAs with N-vinyl pyrrolidone (NVP) employing slow dosing strategies provides a route to prepare linear copolymers with a uniform ester distribution. The semi-batch polymerization of MTC and NVP using polyethylene oxide (PEO) as the solvent leads to radical transfer onto oxyethylene, enabling the preparation of graft copolymers with a PEO backbone and MTC-co-NVP containing side chains. Differential scanning calorimetry (DSC) characterization of CKA copolymers demonstrates the effects of polymer chemical structures and architectures on their thermal properties.",
  size="1792x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(response)

print(image_url)

# "A stylized poster for the 'Fringe Fest' theatre festival. The poster is dominated by a large white circle with the words 'Fringe Fest' in large bold print. On the bottom of the image (in the black region outside of the white circle) there are 4 medium -sized colorful simple figure outlines dancing and playing music"
# A work in strict notan with birds and a landscape, each part of the image must have a reflected negative space in the opposite color. Each section in black MUST have a corresponding white section of EXACTLY the same shape. It may only use black and white (no gray), and should put a particular emphasis on symmetry. The symmetry should be done only on the instersections of black and white sections. It MUST have exactly the same shape in the black and the white sections
# a three by three grid of squares which tells a love story using only only symbols that are found on airport signage such as the man logo on a men's bathroom logo. The story should be simple to follow and meaningful.