

import google.generativeai as genai
import speech_recognition as sr
import pyttsx3


genai.configure(api_key="AIzaSyBYblFEYcu_HdQDnrYtlm2lZJJwfZu3gdM")


tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)  


def get_gemini_response(user_input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    return response.text.strip()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)  
        try:
            audio = recognizer.listen(source, timeout=5)  
            text = recognizer.recognize_google(audio)  
            print(f"👤 You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return None
        except sr.RequestError:
            print("❌ Speech Recognition API error")
            return None


def respond(text):
    print(f"🤖 AI: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()


def main():
    print("\n🔵 AI Call Bot Started. Say 'exit' to stop.\n")
    while True:
        user_input = listen()
        if user_input:
            if user_input.lower() == "exit":
                print("🔴 Stopping the bot...")
                break
            
            
            bot_reply = get_gemini_response(user_input)
            
            
            respond(bot_reply)

if __name__ == "__main__":
        main()