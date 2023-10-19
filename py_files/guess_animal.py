import openai
from dotenv import load_dotenv
import os
import random

load_dotenv()

OPENAI_API_KEY = str(os.getenv('OPENAI_API_TEST'))
openai.api_key = OPENAI_API_KEY

def get_clue():
    words = ['elefante', 'león', 'jirafa', 'hipopótamo', 'mono', 'cocodrila']
    random_word = random.choice(words)
    prompt = 'Adivina la palabra que estoy pensando. Es un animal que vive en la selva.'
    return prompt, random_word

def check_answer(user_input, answer):
    return user_input == answer

def give_property(animal):
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = 'Dame una caracterísitca del animal ' + animal + ' pero no digas su nombre',
        max_tokens = 100
    )
    return response.choices[0].text

def play_game():
    prompt, answer = get_clue()
    print(prompt)
    while True:
        user_input = input('Ingresa tu respuesta: ')
        if check_answer(user_input, answer):
            print('Correcto. La respuesta correcta era: ' + answer)
            break
        else:
            print('Incorrecto. Intenta de nuevo.')
            print(give_property(answer))


play_game()