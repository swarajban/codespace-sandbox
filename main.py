from openai import OpenAI
import os

OPEN_API_KEY = os.environ.get('OPEN_API_SANDBOX_KEY')

def main():
    client = OpenAI(api_key=OPEN_API_KEY)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "If I put an apple in the garage. What fruits are located in the garage?"
            }
        ],
        model='gpt-4-1106-preview'
    )
    first_message = chat_completion.choices[0].message
    response = first_message.content
    print(response)





if __name__ == '__main__':
    main()
    