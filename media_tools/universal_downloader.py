import yt_dlp
import os

def get_user_choice():
    print("\n--- Select Format ---")
    print("1. 🎬 MP4 (Highest Quality Video)")
    print("2. 🎵 MP3 (Audio Only)")
    choice = input("\nEnter choice (1 or 2): ")
    return choice

def run_downloader():
    print("\n" + "="*40)
    print("      SCRIPT SAVANT: UNIVERSAL DOWNLOADER")
    print("="*40)
    
    url = input("\n🔗 Paste the Video or Playlist URL: ")
    choice = get_user_choice()
    
    # Setup Paths
    base_dir = os.path.join(os.getcwd(), 'downloads')
    sub_dir = 'video' if choice == '1' else 'audio'
    save_path = os.path.join(base_dir, sub_dir)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Base Configuration
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'noplaylist': False,
    }

    # Apply Format Specifics
    if choice == '2':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts['format'] = 'bestvideo+bestaudio/best'

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n🚀 ScriptSavant is working... downloading to downloads/{sub_dir}")
            ydl.download([url])
            print(f"\n✅ SUCCESS: Task completed.")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    run_downloader()
