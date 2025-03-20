import streamlit as st
import pandas as pd
import os
import io
from io import BytesIO
import datetime
import random
from streamlit_extras.stylable_container import stylable_container

# Sample daily challenges
daily_challenges = [
    "Reflect on a recent mistake and write what you learned.",
    "Try a new learning strategy for something difficult.",
    "Give positive feedback to someone else.",
    "Identify a fixed mindset thought and reframe it positively.",
    "Write down 3 things you struggled with and how you overcame them."
]

# Function to get today's challenge
def get_daily_challenge():
    today = datetime.date.today()
    index = today.day % len(daily_challenges)  # Change challenge daily
    return daily_challenges[index]

# Growth mindset quotes
motivational_quotes = [
    "Success is not an accident, it’s hard work, perseverance, learning, studying, and sacrifice.",
    "Failure is simply the opportunity to begin again, this time more intelligently.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Growth is never by mere chance; it is the result of forces working together."
]

# Streamlit UI
st.title("Growth Mindset Challenge")
st.write("Welcome! Each day, you'll get a new challenge to help develop a growth mindset.")

# Display daily challenge
st.markdown("<h2 style='display: flex; align-items: center;'><img src='https://img.icons8.com/ios/50/000000/task.png' style='width:24px; margin-right:10px;'/> Today's Challenge</h2>", unsafe_allow_html=True)
st.write(get_daily_challenge())

# User response input
st.markdown("<h2 style='display: flex; align-items: center;'><img src='https://img.icons8.com/ios/50/000000/edit.png' style='width:24px; margin-right:10px;'/> Your Reflection</h2>", unsafe_allow_html=True)
user_response = st.text_area("How did you approach today's challenge? Share your thoughts!")
if st.button("Submit"):
    st.success("Great job! Keep up the learning mindset.")

# Motivational Quote
st.markdown("<h2 style='display: flex; align-items: center;'><img src='https://img.icons8.com/ios/50/000000/idea.png' style='width:24px; margin-right:10px;'/> Growth Mindset Quote</h2>", unsafe_allow_html=True)
st.write(random.choice(motivational_quotes))

# Footer
st.write("---")
st.write("Made with Muhammad Hasnain.")
