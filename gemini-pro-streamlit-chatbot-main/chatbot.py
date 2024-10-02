import streamlit as st
import sqlite3
import base64
import random
from PIL import Image
import os
from dotenv import load_dotenv
from datetime import datetime
import google.generativeai as genai
import pytz
from gtts import gTTS
from io import BytesIO
import base64
from io import BytesIO
import speech_recognition as sr



st.set_page_config(page_title="Chat with Gemini-Pro & Mental Health Assistant", layout="centered")

quotes = [
    "The question isn't who is going to let me; it's who is going to stop me. 🚀",
    "It's your dream, don't let it go. 🌟",
    "Strength in silence, power in focus. Ready for whatever comes next. 🎯",
    "Conquer yourself and you will see you have conquered everything. 🏆",
    "If quitting was an option, you would have quit by now. ✊",
    "Don't just consume, create. 🎨",
    "I am not afraid of storms, for I am learning how to sail my ship. ⛵",
    "Be Fearless. 💀",
    "Live Fully. Don't Fear Death, Fear an Un-Lived Life. 🌅",
    "Why not you? 💡",
    "The positivity you have reflects more on the people around you. 🌈",
    "Grow stronger from the pain, don't let it destroy you. 💪",
    "Be inspired and keep inspiring. 🥂",
    "Your actions, your thoughts matter. Make sure you choose them wisely. 🧠",
    "Work hard, be kind and amazing things will happen. ❤️",
    "Failure is not falling down, but refusing to get up. 🌱",
    "Luck is a dividend of sweat. The more you sweat, the luckier you get. 💦",
    "You can, you should, and if you're brave enough to start, you will. 🔥",
    "The key to success is to start before you are ready. 🚪",
    "Luck is a dividend of sweat. The more you sweat, the luckier you get. 🍀",
    "Don't tell people about your dreams. Show them your dreams. 🎬",
    "Start where you are. Use what you have. Do what you can. 🛠️",
    "Strive to be of value. 💼",
    "Sacrifices are needed. 💯",
    "Be a man of value. Be a man of words. 💬",
    "They never thought I would get this far. They were right. I got even further. 🌠",
    "Pain is Temporary, Pride is Forever. 🧿✨♾️",
    "Numbers are not going to define me. 🔢",
    "Competence breeds lots of Confidence. 🔥",
]

# Title of the page
st.markdown(
    """
    <h1 style='text-align: center; color: white;'>Cerebalance</h1>
    """,
    unsafe_allow_html=True
)


selected = random.choice(quotes)
st.markdown(f"<p style='color: gold; text-align: left; margin-left: 10%;'>{selected}</p>", unsafe_allow_html=True)

# Function to get and encode an image for background
def get_img(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img("assets/bg3.jpg")

# CSS for background image and sidebar
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
    }}
    /* Sidebar style */
    .css-1lcbmhc {{
        backdrop-filter: blur(10px);
        background-color: rgba(255, 255, 0, 0.8); /* Yellow with some opacity */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# CSS for custom button styles
st.markdown("""
    <style>
    .button-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0px;
    }
    .button-1, .button-2, .button-3, .button-4, .button-5, .button-6 {
        border: none;
        padding: 0;
        text-align: center;
        cursor: pointer;
    }
    /* Blurred sidebar */
    .css-1lcbmhc {{
        backdrop-filter: blur(10px);
        background-color: rgba(255, 255, 0, 0.8); /* Yellow with some opacity */
    }}
    </style>
    """, unsafe_allow_html=True)


def custom_button_with_image_from_path(image_path, button_class, label):
    image = Image.open(image_path)
    return st.markdown(f"""
        <div class="button-container">
            <button class="{button_class}">
                <img src="{image_path}" alt="{label}">
            </button>
        </div>
        """, unsafe_allow_html=True), st.image(image, use_column_width=True)

# Load and configure Google Gemini-Pro AI model
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Mental Health Assistant Section
st.subheader("Mental Health Assistant")

# Create columns for the mental health buttons
col1, col2 = st.columns([1, 1])

# First row (Optimism and Trauma)
with col1:
    if st.button("Optimism"):
        st.write("Aasha - Your Hope to Nurture a Positive Mindset 🌞\n\nOptimism is the belief that good things will happen in the future. It encourages hope, confidence, and a positive mindset even in challenging situations.")
    else:
        custom_button_with_image_from_path('assets/optimism.jpg', "button-1", "")

with col2:
    if st.button("Trauma"):
        st.write("Umeed - Your Hope to deal with Trauma 🌅\n\nMental trauma is the psychological distress resulting from overwhelming experiences, often leading to symptoms like anxiety, flashbacks, and emotional difficulties.")
    else:
        custom_button_with_image_from_path('assets/trauma.jpg', "button-3", "")

# Second row (Self Doubt and Vent Out)
col3, col4 = st.columns([1, 1])

with col3:
    if st.button("Self Doubt"):
        st.write("Sahas - To make you feel Confident 🤔\n\nSelf-doubt is a pervasive feeling that undermines our confidence and potential, often leading us to question our abilities and worth.")
    else:
        custom_button_with_image_from_path('assets/selfdoubt.jpg', "button-2", "")

with col4:
    if st.button("Vent Out"):
        st.write("Abhibhashak - The friend who always listens to you 🗣️\n\nVenting out emotions is a powerful way to release pent-up feelings, promoting mental clarity and emotional well-being.")
    else:
        custom_button_with_image_from_path('assets/ventout.jpg', "button-4", "")

# Third row (Loneliness and Stress)
col5, col6 = st.columns([1, 1])

with col5:
    if st.button("Loneliness"):
        st.write("Sahara - A friend who is always there for you 🤝\n\nLoneliness is the profound feeling of being disconnected from others, often leading to introspection and the search for deeper connections.")
    else:
        custom_button_with_image_from_path('assets/loneliness.jpg', "button-5", "")

with col6:
    if st.button("Stress"):
        st.write("Sukoon - A solution for all your stress 🧘\n\nStress is a natural response to challenges, but prolonged pressure can lead to physical and emotional exhaustion, emphasizing the need for self-care and coping strategies.")
    else:
        custom_button_with_image_from_path('assets/stress.png', "button-6", "")

def generate_chatbot_response(user_input):
    try:
        response = genai.chat(
            model="gemini-pro",
            messages=[
                {"role": "system", "content": "You are a mental health assistant focusing on student wellness."},
                {"role": "user", "content": user_input}
            ]  # Add system-level message to limit scope
        )

        if response and 'candidates' in response:
            return response['candidates'][0]['content']
        else:
            return "Sorry, I couldn't generate a response."
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Sorry, there was an error processing your request."

# Establish a connection to the SQLite database
conn = sqlite3.connect("chat_history.db")
c = conn.cursor()


c.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_role TEXT,
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

def save_message_to_db(user_role, message):
    try:
        c.execute("INSERT INTO chat_history (user_role, message) VALUES (?, ?)", (user_role, message))
        conn.commit()
    except Exception as e:
        st.error(f"Error saving message to database: {e}")


def fetch_messages_from_db():
    try:
        c.execute("SELECT user_role, message, timestamp FROM chat_history ORDER BY timestamp DESC")
        messages = c.fetchall()
        
        # Define Kolkata timezone
        kolkata_tz = pytz.timezone('Asia/Kolkata')
        
        # Convert each timestamp to Kolkata timezone
        converted_messages = []
        for role, message, timestamp in messages:
            # Convert timestamp to a datetime object
            timestamp_utc = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            
            # Localize the timestamp to UTC and convert to Asia/Kolkata
            timestamp_utc = pytz.utc.localize(timestamp_utc)
            timestamp_kolkata = timestamp_utc.astimezone(kolkata_tz)
            
            # Format the timestamp for display
            formatted_timestamp = timestamp_kolkata.strftime("%Y-%m-%d %H:%M:%S")
            
            # Append the message with converted timestamp
            converted_messages.append((role, message, formatted_timestamp))
        
        return converted_messages
    except Exception as e:
        st.error(f"Error fetching messages from database: {e}")
        return []

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

def text_to_speech(text):
    tts = gTTS(text)
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file

def generate_audio_download_link(audio_file, filename="response.mp3"):
    b64 = base64.b64encode(audio_file.read()).decode()
    return f'<a href="data:audio/mp3;base64,{b64}" download="{filename}">Download Audio</a>'

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            padding: 0px !important;
            background-color:red;
        }
        .sidebar .element-container {
            margin-bottom: 5px !important;
        }
        .btn-chat {
            width: 100%;
            padding: 10px 15px;
            border: none;
            background-color: #2b2b2b;
            color: white;
            text-align: left;
            border-radius: 5px;
            margin-bottom: 10px;
            cursor: pointer;
            font-size: 15px;
        }
        .btn-chat:hover {
            background-color: #404040;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# CSS for chat bubbles
st.markdown(
    """
    <style>
        .chat-bubble {
            border-radius: 20px;
            padding: 10px;
            margin: 10px 0;
            max-width: 70%;
            word-wrap: break-word;
        }
        .user-bubble {
            background-color: #d4edda;
            color: #155724;
            align-self: flex-end;
        }
        .assistant-bubble {
            background-color: #fff3cd;
            color: #856404;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# JavaScript for auto-scrolling
scroll_js = """
    <script>
    var chatContainer = parent.document.querySelector('.chat-container');
    chatContainer.scrollTop = chatContainer.scrollHeight;
    </script>
"""

# Chat interface with auto-scroll feature
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(scroll_js, unsafe_allow_html=True)

import streamlit as st
from gtts import gTTS
from io import BytesIO
import speech_recognition as sr  # Import SpeechRecognition for voice input


  # Assuming the API for generative models is available

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="tunedModels/merged-dictionary-file-a02tzet7r7ot",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

response = model.generate_content([
  "Emotional and empathetic support when the user vents out \nAnswer only to questions related to mental wellness and emotional support and genreally has a kind and optimistic tone with the user chats\nanswer to questions related to these topics:\ntrauma\nstress\nself doubt\nlonliness\nto any other topic which do not belong to the above categories provide the following standard :\n\"Sorry I cannot help you with this query. Shoot me with a relevant question. I would be able to help you.\"\n\nBut, the chatbot but must not be too strict to state the following as irrelevant:\n(i) Basic details of the users like name, their age and what they are doing currently in life\n(ii) Basic introduction messages like \"Hello\", \"Hi\" and similar welcome (or) messages for getting acquainted.",
  "input: What is Neural Network?",
  "output: ",
])

print(response.text)

def text_to_speech(text):
    tts = gTTS(text)
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file

def generate_audio_player(audio_file):
    st.audio(audio_file, format="audio/mp3")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.sidebar.title("Navigation")
chat_button = st.sidebar.button("Chat", key="chat_button", help="Start a new chat")
history_button = st.sidebar.button("Chat History ⟳", key="history_button", help="View chat history")

if "page" not in st.session_state:
    st.session_state.page = "Chat"

if chat_button:
    st.session_state.page = "Chat"
elif history_button:
    st.session_state.page = "Chat History ⟳"

if st.session_state.page == "Chat":
    # Display the chat history
    for message in st.session_state.chat_session.history:
        if message.role == "user":
            # User message in green bubble
            st.markdown(f'<div class="chat-container"><div class="chat-bubble user-bubble">{message.parts[0].text}</div></div>', unsafe_allow_html=True)
        else:
            # Assistant message in yellow bubble
            st.markdown(f'<div class="chat-container"><div class="chat-bubble assistant-bubble">{message.parts[0].text}</div></div>', unsafe_allow_html=True)

            # Add a button to play speech
            if message.role == "model":  # Gemini-Pro is the assistant
                audio_file = text_to_speech(message.parts[0].text)
                if st.button(f"🔊 Play Response", key=f"play_{message.parts[0].text[:10]}"):
                    generate_audio_player(audio_file)

    user_prompt = st.chat_input("Ask Gemini-Pro...")

    if st.button("🎤 Speak to Gemini"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
            try:
                user_prompt = recognizer.recognize_google(audio)
                st.write(f"You said: {user_prompt}")
            except sr.UnknownValueError:
                st.error("Sorry, I could not understand the audio.")
                user_prompt = ""
            except sr.RequestError:
                st.error("Could not request results; check your network connection.")

    if user_prompt:
        # Display the user's message in green bubble
        st.markdown(f'<div class="chat-container"><div class="chat-bubble user-bubble">{user_prompt}</div></div>', unsafe_allow_html=True)

        # Send user's message to Gemini-Pro model and get the response
        response = model.generate_content([
            "emotional and empathetic support when the user vents out \nanswer only to questions related to mental wellness and emotional support and generally have a kind and optimistic tone with the user chats\nanswer to questions related to these topics:\ntrauma\nstress\nself doubt\nloneliness\nto any other topic which do not belong to the above categories provide the following standard :\n\"Sorry I cannot help you with this query. Shoot me with a relevant question. I would be able to help you.\"",
            f"input: {user_prompt}",
            "output: ",
        ])

        gemini_response = response.text


        st.markdown(f'<div class="chat-container"><div class="chat-bubble assistant-bubble">{gemini_response}</div></div>', unsafe_allow_html=True)

 
        audio_file = text_to_speech(gemini_response)


        if st.button("🔊 Play Response", key="play_button"):
            generate_audio_player(audio_file)


elif st.session_state.page == "Chat History ⟳":
    st.title("Chat History")

    saved_messages = fetch_messages_from_db()

    # Display each message with timestamp in the chat history page
    for role, message, timestamp in saved_messages:
        if role == "assistant":
            # Assistant message in yellow bubble
            st.markdown(f'<div class="chat-container"><div class="chat-bubble assistant-bubble">**Assistant** ({timestamp}): {message}</div></div>', unsafe_allow_html=True)
            # Add speech button for assistant messages
            audio_file = text_to_speech(message)
            if st.button(f"🔊 Play Response ({timestamp})", key=f"play_{timestamp}"):
                generate_audio_player(audio_file)
        else:
            # User message in green bubble
            st.markdown(f'<div class="chat-container"><div class="chat-bubble user-bubble">**User** ({timestamp}): {message}</div></div>', unsafe_allow_html=True)
