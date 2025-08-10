from ollama import chat

# Test basic query
response = chat(model='gemma3', messages=[
    {'role': 'user', 'content': 'What is the weather like today?'}
])
print("Response:", response['message']['content'])
