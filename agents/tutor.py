import google.generativeai as genai

API_KEY = "AIzaSyCUWtUx-TiixHeGUX0R59aJXIHj8ZZhz4A"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def handle(query):
    try:
        clean_query = query.replace("explain", "").strip()
        mode=input("choose you mode of explaination(short mode or long mode):")
        

        if not clean_query:
            return "Tutor: What would you like me to explain? (Usage: 'explain python')"
        if mode.lower()=="short mode":
            prompt = f"You are a helpful Tutor Agent. Explain this topic simply in 2-3 sentences: {clean_query}"
        else:
            prompt = f"You are a helpful Tutor Agent. Explain this topic in detail like 10-12 lines : {clean_query}"
        
        response = model.generate_content(prompt)
        
        return f"Tutor (AI): {response.text}"

    except Exception as e:
        return f"Tutor: Error connecting to AI. ({e})"