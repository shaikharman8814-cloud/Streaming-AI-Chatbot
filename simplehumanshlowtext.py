from openai import OpenAI
import time
client=OpenAI(api_key="Your api key Here",base_url="Url of Website")
              



messages = [

    {

        "role": "system",

        "content": "You are a great teacher"

    }

]

while True:

    user = input("\nYou: ")

    if user == "exit":

        break

    messages.append({

        "role": "user",

        "content": user

    })

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",
        messages=messages,
        stream=True)
    print("\nBot",end="",flush=True)
    full_reply=""
    for chunk in response:
        text=chunk.choices[0].delta.content
        if text:
            for char in text:
                print(char,end="",flush=True)
                time.sleep(0.02)
                full_reply+=char
    print()
    messages.append({"role":"assistant","content":full_reply})