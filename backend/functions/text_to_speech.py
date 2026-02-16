import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Eleven Labs
# Convert text to Speech
def convert_text_to_speech(messag):

    # Define Data (Body)
    body = {
        "text": messag,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }

    # Define voice
    voice_Andreas = "PIGsltMj3gFMR34aFDI3"

    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }

    # Constructing endpoints
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_Andreas}"

    # Send request
    try:
        response = requests.post(endpoint, json=body, headers=headers)

    except Exception as e:
        return
    
    # Handle Response
    if response.status_code == 200:
        return response.content
    else:
        return