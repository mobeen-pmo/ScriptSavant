import streamlit as st
from PIL import Image
import io

# --- Configuration ---
GITHUB_USERNAME = "mobeen-pmo" 
REPO_URL = f"https://github.com/mobeen-pmo/ScriptSavant"

# --- Page Configuration ---
st.set_page_config(page_title="ScriptSavant", page_icon="🖼️", layout="centered")

# --- Sidebar Branding ---
st.sidebar.title("🧙‍♂️ ScriptSavant")
st.sidebar.markdown("---")
st.sidebar.info(f"Developed by **{GITHUB_USERNAME}**")
st.sidebar.markdown(f"[⭐ Star on GitHub]({REPO_URL})")
st.sidebar.markdown("---")
st.sidebar.info("Explore high-performance automation scripts and tools.")

# --- Main UI ---
st.title("🖼️ Universal Image Converter")
st.markdown("Instantly convert images between formats (PNG, JPG, WEBP, BMP) directly in your browser.")

# --- Image Logic ---
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg", "webp", "bmp"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Preview", use_column_width=True)
    
    st.markdown("### ⚙️ Conversion Settings")
    target_format = st.selectbox("Convert to:", ["PNG", "JPG", "WEBP", "BMP", "ICO"])
    
    if st.button("🚀 Convert Now"):
        with st.spinner("Processing..."):
            buf = io.BytesIO()
            
            # Handle JPG transparency (remove alpha channel)
            if target_format in ["JPG", "BMP"] and image.mode in ("RGBA", "P"):
                image = image.convert("RGB")
            
            # Save logic
            save_format = "JPEG" if target_format == "JPG" else target_format
            image.save(buf, format=save_format)
            byte_im = buf.getvalue()
            
            st.balloons() # Fun effect on success
            st.success("Conversion Successful!")
            
            st.download_button(
                label=f"📥 Download {target_format} Image",
                data=byte_im,
                file_name=f"converted_image.{target_format.lower()}",
                mime=f"image/{target_format.lower()}"
            )

# --- Footer ---
st.markdown("---")
st.caption(f"© 2026 {GITHUB_USERNAME} | Built with Streamlit & Python")
