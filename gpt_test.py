from openai import OpenAI

# Setup a client with my API KEY genereated by OpenAI
client = OpenAI(
    api_key="your_key"
)

question = input("Pergunte algo ou tecle [enter] para sair: ")

while question != "":
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": question}]
    )

    # Unwrap the content of the message returned by OpenAI
    print(completion.choices[0].message.content.strip(), end="\n")

    question = input("Continue perguntando ou tecle [enter] para sair: ")
