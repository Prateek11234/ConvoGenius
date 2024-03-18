import os
import openai

openai.api_key = "sk-netjkt0pVRmlSPI84Z6CT83lbkFJbESXpjIpiKhFwt430SBL"


start_sequence = ""\nAI:"
restart_sequence = "\nHuman:"


while true:
    ask = input("Ask your question or type break to stop:  ")

    if ask == "break"
        print("THANK YOU FOR COMING :)")
        break
    else:
        response = openai.completion.create(
            model="text-davinci-003",
            prompt=ask,
            temperature = 0.9,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["Human:","AI"]
        )
        print(response)["choices"][0]["text"]
