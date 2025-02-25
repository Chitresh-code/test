import streamlit as st
import random
import time
import pandas as pd
import plotly.express as px

# Set the page title
st.set_page_config(page_title="Chitresh Loves Shally", page_icon="💖")

# Love Quotes
love_quotes = [
    "You are the peanut butter to my jelly. 💕",
    "Every love story is beautiful, but ours is my favorite. ❤️",
    "You make my heart skip a beat—every single time. 💓",
    "I never knew what love was until I met you. 💖",
    "You are my today and all of my tomorrows. 💞",
    "If I had a flower for every time I thought of you, I could walk in my garden forever. 🌹"
]

# Mood Responses
mood_responses = {
    "🥰 Feeling Loved": "Awww! My love, you deserve ALL the love in the universe! 🌍💖 But guess what? You already have mine, forever and always! 😘",
    "😊 Happy": "Yay! Your happiness is my daily dose of sunshine! ☀️ Keep smiling, my cupcake, because you make my heart do a happy dance! 💃🎶",
    "😴 Sleepy": "Sleepy, huh? 😴 Come rest your head on my shoulder while I whisper how much I love you. 💕 Sweet dreams, my lovebug! 😘💤",
    "🤔 Thinking About You": "Guess what? I'm thinking about you too! 🥰 In fact, you're always running through my mind... rent-free! 😆💖",
    "😢 Sad": "Oh no! Sadness isn't allowed in my queen's kingdom! 👑 Let me send you **1,000 virtual kisses 😘** and a million hugs! 🤗",
    "🤩 Excited": "Excited?! I love this energy! 🎉💃 Let’s bottle it up and celebrate something random—like how ridiculously cute you are! 😍",
    "😡 Angry": "Uh-oh, someone's mad! 😱 But wait... what if I give you a **BIG BEAR HUG 🐻💖**, your favorite treat 🍫, and unlimited cuddles? Still mad? 😏"
}

# Function to display "I Love You" magically
def magical_love_message():
    message = "I Love You 💖"
    animated_text = ""
    for char in message:
        animated_text += char
        st.markdown(f"<h2 style='text-align:center;'>{animated_text}</h2>", unsafe_allow_html=True)
        time.sleep(0.5)
    st.session_state["message_shown"] = True

# Title
st.markdown("<h1 style='text-align: center;'>💖 Here is a Surprise for You 💖</h1>", unsafe_allow_html=True)

# Magical Love Message
st.subheader("✨ Watch the Magic ✨")
if st.button("Reveal Love Message 💘"):
    magical_love_message()

# Click for a Surprise (Only appears after the message is displayed)
if st.session_state.get("message_shown", False):
    st.subheader("🎁 Click for a Surprise!")
    if st.button("Open Gift Box 🎀"):
        selected_quote = random.choice(love_quotes)
        st.success(f"🌸 Surprise Message: **{selected_quote}**")
        st.balloons()

# Mood Selection
st.subheader("💭 How is your current mood?")
mood = st.selectbox("Select your mood:", list(mood_responses.keys()), index=None, placeholder="Choose your mood...")

if mood:
    st.markdown(f"<h3 style='text-align:center;'>{mood_responses[mood]}</h3>", unsafe_allow_html=True)

# --- LOVE CHARTS SECTION --- #
st.markdown("---")
st.subheader("📊 Love Stats – Because Love is Science Too! 😘")

# 1. PIE CHART - "Things I Love About You"
love_features = pd.DataFrame({
    "Feature": ["Smile 😊", "Boobs 🔥", "Eyes 👀", "Hair 💇‍♀️", "Voice 🎶", "Personality 💖", "Cuteness 🥰"],
    "Love Percentage": [30, 25, 15, 10, 8, 7, 5]  # Adjusted love distribution
})
fig_pie_features = px.pie(love_features, names="Feature", values="Love Percentage", 
                           title="Things I Love About You 💕", color_discrete_sequence=px.colors.sequential.Reds)
st.plotly_chart(fig_pie_features)

# 2. BAR CHART - "Love Over Time"
love_growth = pd.DataFrame({
    "Years": ["Day 1", "Year 1", "Year 2", "Forever"],
    "Love Level": [10, 50, 100, 9999]
})
fig_bar = px.bar(love_growth, x="Years", y="Love Level", text="Love Level",
                 title="Love Over Time 📈", color_discrete_sequence=["red"])
st.plotly_chart(fig_bar)

# 3. HEART COMPARISON - "Your Heart vs. Mine"
hearts = pd.DataFrame({"Person": ["Your Heart 💖", "My Heart (Which You Own) 💘"], "Size": [100, 200]})
fig_heart = px.bar(hearts, x="Person", y="Size", text="Size", title="Your Heart vs. Mine 💞",
                   color_discrete_sequence=["pink", "red"])
st.plotly_chart(fig_heart)

# P.S. Message
st.markdown("---")
st.write("P.S. You make my world brighter every single day! 🌎✨")
