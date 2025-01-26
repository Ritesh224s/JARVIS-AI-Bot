from openai import OpenAI

client=OpenAI(
  api_key="", # Have to integrate OpenAI API Key here from OpenAI api.
)
comletion=client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a virtual named JARVIS assistant, skilled in general tasks like Alexa and google cloud."},
        {'role':"user","content":"what is coading "}
    ]
        
)
print(comletion.choices[0].message.content)