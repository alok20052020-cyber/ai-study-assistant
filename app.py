import streamlit as st
from google import genai

st.set_page_config(page_title="AI Study Assistant", page_icon="📚")

st.title("📚 AI Study Assistant")
st.write("Namaste! Apne sawal poochho aur AI se jawab pao.")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)

    topic = st.selectbox(
        "Subject chuno",
        ["Python", "Computer Science", "Maths", "English", "Science"]
    )

    question = st.text_area("Apna sawal likho")

    if st.button("AI se jawab pao"):
        if question.strip():
            with st.spinner("AI jawab taiyar kar raha hai..."):
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=f"Answer this {topic} question in simple Hindi or Hinglish, in 3-5 short sentences. Be direct and concise: {question}",
                )
            st.subheader("AI ka jawab")
            st.write(response.text)
        else:
            st.warning("Pehle apna sawal likho.")
except Exception as e:
   
    st.error(f"Error: {e}")