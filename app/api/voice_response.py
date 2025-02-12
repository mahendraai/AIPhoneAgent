from flask import Blueprint, request, jsonify
from datetime import datetime
from app.services.voice_recognition import transcribe_audio
from app.services.nlp_engine import generate_response
from app.services.text_to_speech import text_to_speech
from app.models.call_log import CallLog
from app.utils.database import db

voice_response_bp = Blueprint('voice_response', __name__)

@voice_response_bp.route("/voice_response", methods=['POST'])
def handle_call():
    # Get the audio file from Twilio
    audio_file = request.files['RecordingUrl']
    
    # Transcribe the audio
    transcript = transcribe_audio(audio_file)
    
    # Generate a response using GPT-4
    response_text = generate_response(transcript)
    
    # Convert the response to speech
    output_file = text_to_speech(response_text)
    
    # Log the call in the database
    call_log = CallLog(
        caller_number=request.form['From'],
        transcript=transcript,
        response=response_text
    )
    db.session.add(call_log)
    db.session.commit()
    
    # Return the response to Twilio
    return jsonify({"response": response_text})
