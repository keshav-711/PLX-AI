import json
import os
import google.generativeai as genai

MEMORY_FILE = "memory.json"
API_KEY = "AIzaSyCUWtUx-TiixHeGUX0R59aJXIHj8ZZhz4A"  

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def extract_info_with_ai(user_text):
    prompt = f"""
    Analyze this sentence: "{user_text}"
    
    1. If the user is stating their name, return: NAME: <The Name>
    2. If the user is stating a weak subject, return: WEAK: <The Subject>
    3. If the user is asking who they are, return: QUERY
    4. Otherwise, return: NONE
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except:
        return "NONE"

def handle(query):
    data = load_memory()
    ai_analysis = extract_info_with_ai(query)

    if "NAME:" in ai_analysis:
        new_name = ai_analysis.split("NAME:")[-1].strip()
        data["user_name"] = new_name
        save_memory(data)
        return f"Memory: Understood. I've updated your name to {new_name}."

    elif "WEAK:" in ai_analysis:
        subject = ai_analysis.split("WEAK:")[-1].strip()
        if "weak_subjects" not in data:
            data["weak_subjects"] = []
        data["weak_subjects"].append(subject)
        save_memory(data)
        return f"Memory: Got it. I added {subject} to your weak areas."

    elif "QUERY" in ai_analysis or "who" in query:
        return (f"Memory: You are {data.get('user_name', 'User')}. \n"
                f"   - Weak Areas: {', '.join(data.get('weak_subjects', []))}")

    return "Memory: I didn't catch that. Try telling me your name or weak subjects."