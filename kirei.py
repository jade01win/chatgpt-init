import os
import openai

openai.api_key_path = "API_KEY_PATH_FILE"

com1 = input("Enter the Command: ")
response = openai.Completion.create(
    model="text-davinci-003", 
    prompt= com1, 
    temperature=0, 
    max_tokens=4000)

print (response["choices"][0]["text"])
