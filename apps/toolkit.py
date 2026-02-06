import streamlit as st
import yt_dlp
import os
from PIL import Image
import io

# --- Page Configuration ---
st.set_page_config(page_title="ScriptSavant", page_icon="🧙‍♂️", layout="wide")

# --- Custom Styling & Branding ---
st.sidebar.title("🧙‍♂️ ScriptSavant")
st.sidebar.markdown("---")
st.sidebar.info("Developed by **https://github.com/mobeen-pmo/ScriptSavant**")
st.sidebar.markdown("Explore high-performance automation scripts and tools.")

st.title("🚀 ScriptSavant Multi-Tool ")
st.markdown("Automate your digital workflow with ease.")

# --- Tabs for Different Tools ---
tab1, tab2 = st.tabs(["🎥 Video Downloader", "🖼️ Image Converter"])

# --- TAB 1: Video Downloader ---
with tab1:
    st.header("Universal Video Downloader")
    url = st.text_input("Paste URL here (YouTube, Insta, FB, etc.):")
    format_type = st.selectbox("Choose Format:", ["MP4 (Video)", "MP3 (Audio)"])
    
    if st.button("Start Download"):
        if url:
            with st.spinner("Processing..."):
                try:
                    ydl_opts = {
                        'format': 'best' if format_type == "MP4 (Video)" else 'bestaudio/best',
                        'outtmpl': 'downloads/%(title)s.%(ext)s',
                    }
                    if format_type == "MP3 (Audio)":
                        ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}]
                    
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                    st.success(f"Successfully downloaded! Check your 'downloads' folder.")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a valid URL.")

# --- TAB 2: Image Converter ---
with tab2:
    st.header("Universal Image Converter")
    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg", "webp", "bmp"])
    target_format = st.selectbox("Convert to:", ["PNG", "JPG", "WEBP", "BMP"])
    
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Preview", width=300)
        
        if st.button("Convert & Download"):
            buf = io.BytesIO()
            # Handle JPG transparency
            if target_format == "JPG" and img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            save_format = "JPEG" if target_format == "JPG" else target_format
            img.save(buf, format=save_format)
            byte_im = buf.getvalue()
            
            st.download_button(
                label=f"Download {target_format} Image",
                data=byte_im,
                file_name=f"converted_image.{target_format.lower()}",
                mime=f"image/{target_format.lower()}"
            )

st.markdown("---")
st.caption("© 2026 Software Bazaar | Built with Streamlit & Python")
