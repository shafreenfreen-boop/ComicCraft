import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ComicCraft")
st.title("ComicCraft - AI Comic Creator")

api_key = st.text_input("Enter Gemini API Key", type="password")
story = st.text_area("Enter your story idea - ex: Shabana adventure")

if st.button("Generate Comic Story"):
    if api_key and story:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Create a 4 panel comic story script for: {story}. Give panel wise description and dialogues."
        response = model.generate_content(prompt)
        st.success("Comic Generated!")
        st.write(response.text)
    else:
        st.warning("API key and story kuduthiya da?")
