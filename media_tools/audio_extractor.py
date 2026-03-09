
import os
from moviepy.editor import VideoFileClip

def extract_audio():
    print("\n" + "="*40)
    print("   SCRIPT SAVANT: LOCAL AUDIO EXTRACTOR")
    print("="*40)

    # 1. Get User Input
    video_path = input("\n🎥 Enter the path to the local video file: ").strip('"')
    
    if not os.path.exists(video_path):
        print("❌ Error: Video file not found! Please check the path.")
        return

    # 2. Select Output Format
    print("\nSupported Output Formats: MP3, WAV")
    target_ext = input("🎵 Enter target audio format (mp3/wav): ").lower().replace(".", "")

    if target_ext not in ['mp3', 'wav']:
        print("❌ Error: Unsupported format. Defaulting to mp3.")
        target_ext = 'mp3'

    # 3. Setup Output Path
    base_name = os.path.splitext(video_path)[0]
    output_path = f"{base_name}_extracted.{target_ext}"

    try:
        print(f"\n🔄 Extracting audio to {target_ext.upper()}... this may take a moment.")
        
        # Load the video
        video = VideoFileClip(video_path)
        audio = video.audio
        
        if audio is None:
            print("\n❌ Error: No audio track found in this video!")
            video.close()
            return

        # Write the audio file (logger=None hides the messy progress bars in the terminal)
        if target_ext == 'wav':
            audio.write_audiofile(output_path, codec='pcm_s16le', logger=None)
        else:
            audio.write_audiofile(output_path, logger=None)
            
        # Free up system memory
        audio.close()
        video.close()
        
        print(f"\n✅ SUCCESS! Audio saved as: {output_path}")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    extract_audio()
