import requests
import time 
import openai
from dotenv import load_dotenv
import os

load_dotenv()
token = str(os.getenv('TELEGRAM_TOKEN'))
OPENAI_API_KEY = str(os.getenv('OPENAI_API_TEST'))
openai.api_key = OPENAI_API_KEY

def get_updates(offset):
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()["result"]

def send_messages(chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response

def get_openai_response(prompt):
    model_engine = "ada:ft-personal-2023-10-25-18-01-26"
    response = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 200,
        n = 1,
        stop = " END",
        temperature = 0.5
    )
    return response.choices[0].text.strip()

def main():
    print('Starting bot...')
    offset = 0
    while True:
        updates = get_updates(offset)
        if updates:
            for update in updates:
                offset = update["update_id"] +1
                chat_id = update["message"]["chat"]['id']
                user_message = update["message"]["text"]
                print(f"Received message: {user_message}")
                GPT = get_openai_response(user_message)
                send_messages(chat_id, GPT)
        else:
            time.sleep(1)

if __name__ == '__main__':
    main()