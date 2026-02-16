#uvicorn main:app
#uvicorn main:app --reload

# Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


# Custom Function Imports
from functions.database import store_messges, reset_messages
from functions.openai_requests import convert_audio_to_text, get_chatgpt_response
from functions.text_to_speech import convert_text_to_speech


# Initiate App
app = FastAPI()


# CORs - Origins
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
]


# CORs Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# check Health
@app.get("/health")
async def check_health():
    return {"message": "Healthy"}


# Reset messages
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}


# Get audio
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
   
   # Get saved audio
   #audio_input = open("voice.mp3", "rb")

   # Save file from Frontend
   with open(file.filename, "wb") as buffer:
      buffer.write(file.file.read())
      
   audio_input = open(file.filename, "rb")

   # Decode Audio
   message_decoded = convert_audio_to_text(audio_input)
   
   # Guard: Ensure Message Decoded
   if not message_decoded:
       return HTTPException(status_code=400, detail="Failed to decode audio.")
   
   # Get ChatGPT Response
   chat_response = get_chatgpt_response(message_decoded)

   # Guard: Ensure Message Decoded
   if not chat_response:
       return HTTPException(status_code=400, detail="Failed to get ChatGPT response.")

   # Store Messages
   store_messges(message_decoded, chat_response)

   # Convert chat response to audio
   audio_output = convert_text_to_speech(chat_response)
   
   # Guard: Ensure Audio Output
   if not audio_output:
      return HTTPException(status_code=400, detail="Failed to get ElevenLabs audio response.")
   
   # Create a generator that yeilds chunks of data
   def iterfile():
      yield audio_output
      
   # Return audio file
   return StreamingResponse(iterfile(), media_type="application/octet-stream")