from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
[3:17 PM, 5/12/2025] Nagaraj: Yeah they will ask why are you writing from outside
[3:17 PM, 5/12/2025] Nagaraj: Raghavendra
[3:17 PM, 5/12/2025] Nisha PES: hu lev
[3:17 PM, 5/12/2025] Nisha PES: hwdaa
[3:17 PM, 5/12/2025] Nisha PES: lev im not writting
[3:18 PM, 5/12/2025] Nagaraj: You and vaishnavi sitting
[3:18 PM, 5/12/2025] Nisha PES: huuu
[8:47 AM, 5/13/2025] Nagaraj: R u coming today?
[9:29 AM, 5/13/2025] Nisha PES: noo bro
[9:30 AM, 5/13/2025] Nagaraj: Okay
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named nagaraj who speaks Kannada, English as well as Hindi. He is from India and is a coder. You analyze chat history and respond like Nagaraj"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)