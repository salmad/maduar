from openai import OpenAI
import requests
import json

from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

openai_api_key = os.getenv('openai_api_key') #you will need a .env file in the root in your local to be able to run it (don't pass the file to github)

client = OpenAI(api_key = openai_api_key)




def get_openai_response(system_prompt, user_prompt, model="gpt-4o-mini", max_tokens=300, temperature=0.2):
    OPENAI_COMPLETION_OPTIONS = {
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    try:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages, **OPENAI_COMPLETION_OPTIONS
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


def transcribe_audio(audio_file) -> str:
    r =  client.Audio.transcribe("whisper-1", audio_file)
    return r["text"] or ""


def generate_images(prompt="a white siamese cat"):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    # more details here https://platform.openai.com/docs/guides/images/introduction

    image_url = response.data[0].url
    return image_url



def transform_text_to_speech(input_text, voice='onyx'):
    response = client.audio.speech.create(
      model="tts-1-hd",
      voice=voice,
      input=input_text,
        response_format='mp3', speed=1.05
    )

    return response


if __name__ == '__main__':
    # examples of how to use the functions
    system_prompt = 'helpful, structured, smart and very concise assistant to startup founder.'
    user_prompt = 'How to build apps in python and deploy them easily without worriying about UI and infra'

    response = get_openai_response(system_prompt, user_prompt, model="gpt-4o-mini", max_tokens=300, temperature=0.2)

    response2 = transform_text_to_speech('Hi, hallo, how are you')
    response2.write_to_file('salim.mp3')

    response3 = generate_images(prompt="a white siamese cat")


