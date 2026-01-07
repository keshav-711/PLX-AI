import google.generativeai as genai

API_KEY = "AIzaSyAgbRSsR8KakRsDgAWBvVCtoOVzmswO6o8"

genai.configure(api_key=API_KEY)

try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error: {e}")