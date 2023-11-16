from openai import OpenAI
import os
import json

OPEN_API_KEY = os.environ.get('OPEN_API_SANDBOX_KEY')

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_things",
            "description": "Get a list of things",
            "parameters": {
                "type": "object",
                "properties": {
                    "thing_type": {
                        "type": "string",
                        "description": "The type of thing to get",
                        "enum": [
                            "programming_languages",
                            "fruits",
                            "devices",
                        ],
                    },
                    "num_things": {
                        "type": "integer",
                        "description": "The number of things to get",
                        "minimum": 1,
                        "maximum": 10,
                    },
                }
            }
        }
    }
]

def main():
    client = OpenAI(api_key=OPEN_API_KEY)

    chat_completions = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a sample app that can call functions",
            },
            {
                "role": "user",
                "content": "Get me a list of 2 progamming languages",
            }
        ],
        tools=tools,
        model='gpt-4-1106-preview',
        # response_format={
        #     "type": "json_object" 
        # },
    )
    first_choice_message = chat_completions.choices[0].message
    tool_call = first_choice_message.tool_calls[0]

    function_list = {
        'get_things': get_things,
    }

    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)
    things = function_list[function_name](function_args)
    print(things)
    

THINGS = {
        'programming_languages': [
            'python',
            'java',
            'javascript',
            'c#',
            'c++',
            'php',
            'rust',
            'ruby',
            'go',
        ],
        'fruits': [
            'apple',
            'banana',
            'orange',
            'grape',
            'strawberry',
            'peach',
        ],
        'devices': [
            'laptop',
            'phone',
            'tablet',
            'smart watch',
            'desktop',
            'smart tv',
        ],
    }

def get_things(params) -> list[str]:
    thing_type = params['thing_type']
    num_things = params['num_things']
    things = THINGS[thing_type]
    return things[:num_things]


if __name__ == '__main__':
    main()
    