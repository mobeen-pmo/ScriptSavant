import os
import whisper
import warnings

# Suppress some common warning messages from the Whisper library
warnings.filterwarnings("ignore", category=UserWarning)

def transcribe_audio():
    print("\n" + "="*50)
    print("   SCRIPT SAVANT: AI MEETING TRANSCRIBER")
    print("="*50)

    audio_path = input("\n🎙️ Enter the path to the audio file (e.g., meeting.mp3): ").strip('"')
    
    if not os.path.exists(audio_path):
        print("❌ Error: Audio file not found!")
        return

    print("\n⏳ Loading the AI model... (This may take a few seconds on the first run)")
    try:
        # Load the base model. Options: tiny, base, small, medium, large
        model = whisper.load_model("base")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return

    print(f"🔄 Transcribing '{os.path.basename(audio_path)}'...")
    print("This will take a moment depending on the length of the audio.")
    
    try:
        # Perform the transcription
        result = model.transcribe(audio_path)
        transcript_text = result["text"].strip()
        
        # Save to a text file
        output_file = os.path.splitext(audio_path)[0] + "_transcript.txt"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"--- AI TRANSCRIPT FOR: {os.path.basename(audio_path)} ---\n\n")
            f.write(transcript_text)
            
        print(f"\n✅ SUCCESS! Transcription complete.")
        print(f"📄 Saved to: {output_file}")
        
    except Exception as e:
        print(f"\n❌ ERROR during transcription: {e}")

if __name__ == "__main__":
    transcribe_audio()
