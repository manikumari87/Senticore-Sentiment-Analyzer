# modern_dashboard_full.py

import streamlit as st
import pandas as pd
import numpy as np
import time
from textblob import TextBlob

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Modern Dashboard",
    page_icon="🚀",
    layout="wide",
)

# ---- SIDEBAR ----
st.sidebar.header("⚙️ Settings")

# Theme selection
theme_choice = st.sidebar.selectbox("Choose Theme:", ["Light 🌞", "Dark 🌙"])
polarity_threshold = st.sidebar.slider("Polarity threshold for Positive:", -1.0, 1.0, 0.0, 0.01)
feedback = st.sidebar.text_area("💬 Share your feedback:")
if feedback:
    st.sidebar.success("Thanks for your feedback! 🙏")

# ---- CSS Styling ----
if theme_choice == "Dark 🌙":
    bg_color = "#111827"
    text_color = "#f9fafb"
    card_bg = "#1f2937"
else:
    bg_color = "#f0f2f6"
    text_color = "#111827"
    card_bg = "#ffffff"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .stTextArea>div>textarea {{
        background-color: {card_bg};
        color: {text_color};
    }}
    .stButton>button {{
        background-color: #4f46e5;
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---- HEADER ----
st.title("🚀 Modern Interactive Dashboard")
st.subheader("Features: Tabs, Sliders, Charts, Sentiment Analyzer, Progress Bar")

# ---- TABS ----
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Text & Markdown", "Input Widgets", "Charts & Data", "Progress", "Sentiment Analyzer"
])

# ---- TAB 1: TEXT ----
with tab1:
    st.header("Text & Markdown")
    st.write("Normal text using `st.write`")
    st.markdown("**Bold**, *Italic*, `Code`")
    st.markdown("> Blockquote example")
    st.latex("a^2 + b^2 = c^2")

# ---- TAB 2: INPUT ----
with tab2:
    st.header("Interactive Widgets")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name")
        age = st.slider("Your Age", 1, 100, 25)
    with col2:
        hobby = st.selectbox("Your Hobby", ["Coding", "Reading", "Gaming", "Music"])
        agree = st.checkbox("I love Streamlit")
    if name and agree:
        st.success(f"Hi {name}, age {age}, who loves {hobby}!")

# ---- TAB 3: CHARTS ----
with tab3:
    st.header("Charts & Data Example")
    data = pd.DataFrame(np.random.randn(20,3), columns=["Feature A", "Feature B", "Feature C"])
    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(data)
    with col2:
        st.line_chart(data)
    st.bar_chart(data)

# ---- TAB 4: PROGRESS ----
with tab4:
    st.header("Progress Example")
    progress = st.progress(0)
    status = st.empty()
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i+1)
        status.text(f"{i+1}% Complete")
    st.success("✅ Completed!")

# ---- TAB 5: SENTIMENT ANALYZER ----
with tab5:
    st.header("Real-Time Sentiment Analysis")
    text = st.text_area("Enter text here:")

    def analyze_sentiment(txt):
        blob = TextBlob(txt)
        polarity = blob.sentiment.polarity

        if polarity >= polarity_threshold:
            sentiment = "Positive 😊"
            color = "#ecfdf5"
            border = "#10b981"
        elif polarity < 0:
            sentiment = "Negative 😞"
            color = "#fef2f2"
            border = "#ef4444"
        else:
            sentiment = "Neutral 😐"
            color = "#f9fafb"
            border = "#6b7280"

        st.markdown(
            f"<div style='background:{color}; border:2px solid {border}; border-radius:12px; padding:20px; margin-top:10px;'>"
            f"<b>Sentiment:</b> {sentiment} | <b>Polarity:</b> {polarity:.2f}</div>",
            unsafe_allow_html=True
        )

    if st.button("Analyze"):
        if text.strip():
            analyze_sentiment(text)
        else:
            st.warning("Enter some text!")

    # Quick example buttons
    st.markdown("#### Example Texts:")
    examples = ["I love this!", "This is bad.", "Neutral feelings.", "Amazing!", "Not sure..."]
    cols = st.columns(len(examples))
    for i, ex in enumerate(examples):
        if cols[i].button(ex):
            analyze_sentiment(ex)

# ---- FOOTER ----
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Full Feature Dashboard")
