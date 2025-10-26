import streamlit as st
import re
from collections import Counter

# Heuristic AI detection function
def ai_content_detector(text):
    text = text.strip().lower()
    
    # Average word length
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return "⚠️ Please enter some text."
    avg_word_len = sum(len(word) for word in words) / len(words)
    
    # Sentence length variation
    sentences = re.split(r'[.!?]', text)
    sentence_lengths = [len(s.split()) for s in sentences if len(s.split()) > 0]
    variation = max(sentence_lengths) - min(sentence_lengths) if sentence_lengths else 0
    
    # Repetition check
    word_counts = Counter(words)
    repetitive_score = sum(1 for w, c in word_counts.items() if c > 3)
    
    # Heuristic scoring
    ai_score = 0
    if avg_word_len > 6: ai_score += 1
    if variation < 5: ai_score += 1
    if repetitive_score > 2: ai_score += 1
    
    if ai_score >= 2:
        return "🤖 The text seems to be AI-generated."
    else:
        return "🧍 The text seems to be Human-written."

# --- Streamlit Interface ---
st.title("📝 AI Content Detector")
st.write("Paste any text below to check if it is AI-generated or human-written:")

user_input = st.text_area("Enter text here", height=200)

if st.button("Analyze"):
    result = ai_content_detector(user_input)
    st.markdown(f"### Result: {result}")
