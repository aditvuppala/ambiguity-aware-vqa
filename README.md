# ambiguity-aware-vqa
SURE Application 2026 <br>

Project 11|SURE Starter Task 2026 <br>
Adit Vuppala CoE '29 <br>

This prototype helps blind and low-vision (BLVI) users resolve visual ambiguity through a multi-turn conversational interface. <br>

Tech Stack <br>
- Python 3.14
- Streamlit
- Gemini 2.0 Flash Lite

Setup Instructions: <br>
1. Prerequisites <br>
Python 3.9+: Ensure you have Python installed. <br>
Gemini API Key: Obtain a free API key from Google AI Studio. <br>

- Create folder for this project
- git clone into this folder
- create virtual environment using "python -m venv venv"
# Activate the environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate

run "pip install streamlit google-genai pillow" <br>

make sure to paste your API key to the corresponding section of "eleven.py" <br>
launch the web app using "streamlit run eleven.py" <br>


To connect on mobile: <br>
- ensure you are on same internet as computer.
- when run, terminal will show a "network url". Paste that into mobile browser. 
NOTE: for some reason, mobile connectivity to this app is very iffy. It doesn't work on all wifi networks.
ANOTHER NOTE: Images that are too large will not work. Stick to smaller ones for testing. 

