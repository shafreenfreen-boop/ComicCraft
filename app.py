import streamlit as st
from google import genai

st.set_page_config(page_title="ComicCraft", page_icon="📚")
st.title("📚 ComicCraft - AI Comic Creator")

# API Key box
api_key = st.text_input("Enter Gemini API Key", type="password", value="")

if not api_key:
    st.warning("Mela API Key ah paste pannu da - Photo la irukura AQ.... key ah")
    st.stop()

# New client - ithu than pudhu key ku work aagum
client = genai.Client(api_key=api_key)

prompt = st.text_area("Enter your story prompt", "A brave fox exploring an enchanted forest")
char_name = st.text_input("Character Name", "Foxy")
setting = st.selectbox("Setting", ["forest", "city", "school", "space", "ocean"])
tone = st.selectbox("Tone", ["dramatic", "funny", "adventurous"])
art_style = st.selectbox("Art Style", ["comic book", "anime", "realistic"])

if st.button("🚀 Generate Comic Story"):
    try:
        with st.spinner("Generating..."):
            # PUDHU MODEL NAME - 2.0-flash
            response = client.models.generate_content(
              model="gemini-1.5-flash"
                contents=f"Create a 5 panel comic outline as JSON for story: {prompt}, character: {char_name}, setting: {setting}, tone: {tone}, art_style: {art_style}. Each panel need title, description, image_prompt, caption, dialogue."
            )
            st.success("✅ Success!")
            st.write(response.text)
            
            # Image generation part kooda add pannalam
            for i in range(1,6):
                st.subheader(f"Panel {i}")
                st.write(f"Art style: {art_style} - {prompt}")
                
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("API Key thappu illa model name thappu. gemini-2.0-flash use pannu")
