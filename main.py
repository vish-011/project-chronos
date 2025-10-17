import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINIAPIKEY')

def call_gemini_api(fragment_text):
    prompt = f"Reconstruct and complete this old, obscure forum text:\n{fragment_text}\nFull text:"
    
    url = "https://api.google.com/gemini/v1/completions"
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "gemini-1",
        "prompt": prompt,
        "max_tokens": 150
    }

    try:
        response = requests.post(url, headers=headers, json=json_data)
        response.raise_for_status()
        completion = response.json()
        reconstructed_text = completion['choices'][0]['text'].strip()
        return reconstructed_text
    except Exception as e:
        return f"Error calling Gemini API: {e}"

def perform_web_search(query):
    # Placeholder web search API - replace with actual API endpoint & key.
    search_api_url = "https://api.example.com/search"
    params = {
        'q': query,
        'num': 5
    }
    try:
        response = requests.get(search_api_url, params=params)
        response.raise_for_status()
        data = response.json()
        links = [item['link'] for item in data.get('items', [])]
        return links
    except Exception as e:
        return [f"Error performing web search: {e}"]

def generate_report(original_text, reconstructed_text, sources):
    print("\n--- RECONSTRUCTION REPORT ---\n")
    print("Original Fragment:")
    print(original_text)
    print("\nAI-Reconstructed Text:")
    print(reconstructed_text)
    print("\nContextual Sources:")
    if sources:
        for link in sources:
            print(link)
    else:
        print("No sources found.")

if __name__ == "__main__":
    print("Welcome to Project Chronos - The AI Archeologist")
    user_text = input("Enter incomplete or obscure text fragment:\n").strip()
    
    if not user_text:
        print("No input provided. Exiting...")
    else:
        reconstructed = call_gemini_api(user_text)
        sources = perform_web_search(reconstructed)
        generate_report(user_text, reconstructed, sources)
