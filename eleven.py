'''Adit Vuppala
Project 11: Resolving Ambiguity in Visual Question Answering for Accessibility
aditv@umich.edu
Feb 13th, 2026
UofM CoE
'''

import streamlit as st
from google import genai
from PIL import Image

def michigan_theme():
    st.markdown("""
        <style>
        /* Main background and text */
        .stApp {
            background-color: #00274C; /* UMich Blue */
            color: #FFFFFF;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #FFCB05; /* UMich Maize */
            border-right: 2px solid #00274C;
        }
        
        /* High-contrast text for Maize sidebar */
        [data-testid="stSidebar"] .stText, [data-testid="stSidebar"] label {
            color: #00274C !!important;
            font-weight: bold;
        }

        /* Buttons and inputs */
        .stButton>button {
            background-color: #FFCB05;
            color: #00274C;
            border-radius: 10px;
            border: 2px solid #00274C;
        }
        
        /* Accessibility Note: Increasing font size for readability */
        p, label {
            font-size: 1.1rem !important;
        }
        </style>
    """, unsafe_allow_html=True)

# Replace the string below with your API key from Google AI Studio
API_KEY = ""
client = genai.Client(api_key=API_KEY)
MODEL_NAME = "gemini-flash-latest"

# --- UI Layout ---
michigan_theme()
st.set_page_config(page_title="Accessibility VQA Assistant", layout="centered")
st.title("Project 11: Resolving Ambiguity in Visual Question Answering for Accessibility")
st.markdown("""
This system helps blind and low-vision (BLVI) users resolve ambiguity in visual scenes 
by providing structured descriptions or interactive clarification.
""")

# 2. Sidebar for Interaction Mode [cite: 147-148]
st.sidebar.header("Interaction Settings")
mode = st.sidebar.radio(
    "Choose Interaction Style:",
    ["One Pass", "Iterative"],
    help="One Pass gives all info at once, Iterative asks you to clarify"
)

# 3. Image Input [cite: 133, 135]
uploaded_file = st.file_uploader("Upload an image for analysis...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    # Fixed the 'use_container_width' warning from your terminal logs
    st.image(image, caption="Current View", width='stretch')
    
    # 4. Question Input [cite: 136]
    user_question = st.text_input("Ask a question (e.g., 'What is on the table?'):")

    if user_question:
        try:
            with st.spinner("Analyzing image..."):
                if mode == "Respond in One Pass":
                    # Mode 1: Comprehensive structured response 
                    prompt = (
                        f"The user is blind or low-vision and asked: '{user_question}'. "
                        "Identify all potential objects the user might be referring to. "
                        "Provide a structured response including: 1) What objects are present, "
                        "2) Quantities, 3) Spatial locations (left/right/center), and "
                        "4) Salient attributes like color or text."
                    )
                    
                    response = client.models.generate_content(
                        model=MODEL_NAME,
                        contents=[prompt, image]
                    )
                    
                    st.subheader("Comprehensive Description")
                    st.info(response.text)

                else:
                    # Mode 2: Clarify Iteratively 
                    # Step A: Surfaces ambiguity by listing potential items
                    st.subheader("Clarification Dialogue")
                    
                    initial_prompt = (
                        f"The user asked: '{user_question}'. This is ambiguous. "
                        "List the different objects present in the image that could be the subject "
                        "and ask the user which one they are interested in."
                    )
                    
                    initial_res = client.models.generate_content(
                        model=MODEL_NAME,
                        contents=[initial_prompt, image]
                    )
                    
                    st.write("**Assistant:**", initial_res.text)
                    
                    # Step B: Follow-up interaction
                    follow_up = st.text_input("Type your choice to clarify (e.g., 'The bottle'):")
                    
                    if follow_up:
                        final_prompt = (
                            f"The user has clarified they mean: '{follow_up}'. "
                            "Provide a detailed description of this specific object, including "
                            "its location and visual attributes."
                        )
                        final_res = client.models.generate_content(
                            model=MODEL_NAME,
                            contents=[final_prompt, image]
                        )
                        st.write("**Assistant:**", final_res.text)

        except Exception as e:
            st.error(f"System Error: {e}")
            st.write("Troubleshooting: Ensure your API key is correct and you have an internet connection.")

# --- Footer for Accessibility ---
st.divider()
st.caption("Developed for the Human-AI Lab SURE Starter Tasks 2026.")