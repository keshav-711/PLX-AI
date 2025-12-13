import google.generativeai as genai

API_KEY = "AIzaSyCdq9z1tFmj0L1Q1oe-OO0IxgDszSRkEM4"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def handle(query):
    try:
        clean_query = query.replace("explain", "").strip()

        if not clean_query:
            return "Tutor: What would you like me to explain? (Usage: 'explain python')"

        prompt = f"You are a helpful Tutor Agent. Explain this topic simply in 2-3 sentences: {clean_query}"
        
        response = model.generate_content(prompt)
        
        return f"Tutor (AI): {response.text}"

    except Exception as e:
        return f"Tutor: Error connecting to AI. ({e})"