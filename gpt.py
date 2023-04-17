#trying to integrate chat gpt in a python script
#pip install pandas openai
import pandas
import openai
with open('/Users/samik/Desktop/Programming/Automation Sandbox/keys/openai_api_key.txt') as f:
    lines = f.readlines()
print(lines)
openai.api_key = lines

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine= "ada",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()

prompt = input("Enter your question: ")
response = generate_response(prompt)
print(response)
