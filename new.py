

import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
from twilio.rest import Client


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


def simple_main():
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
        def teach_bot():
            print("\n🔵 Teaching Mode Activated. Type 'done' to finish.\n")
            training_data = {}
            while True:
                user_input = input("👤 You: ")
                if user_input.lower() == "done":
                    break
                bot_response = input("🤖 Bot Response: ")
                training_data[user_input.lower()] = bot_response

            print("\n✅ Training Complete. Bot is now smarter!")
            return training_data

        def get_gemini_response_with_training(user_input, training_data):
            if user_input.lower() in training_data:
                return training_data[user_input.lower()]
            return get_gemini_response(user_input)

        def integrate_with_twilio():
            account_sid = "your_account_sid"
            auth_token = "your_auth_token"
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                twiml='<Response><Say>Hello, this is your AI assistant!</Say></Response>',
                to="recipient_phone_number",
                from_="your_twilio_phone_number"
            )
            print(f"📞 Call initiated: {call.sid}")

        def main():
            print("\n🔵 AI Call Bot Started. Say 'exit' to stop or 'teach' to train the bot.\n")
            training_data = {}
            while True:
                user_input = listen()
                if user_input:
                    if user_input.lower() == "exit":
                        print("🔴 Stopping the bot...")
                        break
                    elif user_input.lower() == "teach":
                        training_data = teach_bot()
                    elif user_input.lower() == "call":
                        integrate_with_twilio()
                    else:
                        bot_reply = get_gemini_response_with_training(user_input, training_data)
                        respond(bot_reply)

        if __name__ == "__main__":
                    simple_main()