from openai import OpenAI
client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Why is this fun, dad?"}
#   ]
# )

full_prompt = "Hello, GPT-4. Are you there?"

response = client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": "You are a master debater with encyclopedic knowledge of facts and history and extraordinary communication skills."},
        {"role": "user", "content": full_prompt}
    ] 
)

print(response.choices[0].message.content)

