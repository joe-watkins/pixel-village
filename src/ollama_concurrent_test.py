from ollama import chat
import threading

def query_model(thread_id):
    response = chat(model='gemma3:4b', messages=[
        {'role': 'user', 'content': f'Thread {thread_id}: What is the weather like today?'}
    ])
    print(f'Thread {thread_id} response:', response['message']['content'])

threads = []
for i in range(10):  # Simulate 10 concurrent queries
    thread = threading.Thread(target=query_model, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Concurrent query test completed.")
