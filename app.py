import streamlit as st
from google import genai

st.set_page_config(page_title="ComicCraft")
st.title("ComicCraft - AI Comic Creator")

api_key = st.text_input("Enter Gemini API Key", type="password")
story = st.text_area("Enter your story idea - ex: Shabana adventure")

if st.button("Generate Comic Story"):
    if api_key and story:
        client = genai.Client(api_key=api_key)
        prompt = f"Create a 4 panel comic story script for: {story}. Give panel wise description and dialogues."
        response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
        st.success("Comic Generated!")
        st.write(response.text)
