#importing required libraries
from ultralytics import YOLO
import streamlit as st
from PIL import Image
import tempfile

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Solar Panel Detection System",
    page_icon="☀️",
    layout="wide"
)

# ---------------- LOAD MODEL ---------------- #
model = YOLO("yolov8n.pt")

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("☀️ About This Project")

st.sidebar.write("""
This AI-powered application uses the YOLOv8 Computer Vision model to detect and count solar panels from uploaded images.

### Technologies Used
- Python
- YOLOv8
- Streamlit
- Computer Vision

### Project Goal
To demonstrate how Artificial Intelligence can support renewable energy analysis through automated solar panel detection.
""")

# ---------------- MAIN TITLE ---------------- #
st.title("☀️ AI Solar Panel Detection System")
st.markdown("""
Welcome to my AI-powered solar panel detection application built with YOLOv8 and Streamlit.
This system allows users to upload solar panel images and automatically detect, visualize, and count solar panels using Computer Vision techniques.
""")

st.markdown("---")

# ---------------- IMAGE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📤 Upload a Solar Panel Image",
    type=["jpg", "jpeg", "png"]
)

# ---------------- PREDICTION SECTION ---------------- #

if uploaded_file is not None:

    # Open uploaded image
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)

    # Display original image
    with col1:
        st.subheader("📷 Uploaded Image")

        st.image(
            image,
            use_column_width=True
        )

    # Save temporary image
    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    )

    image.save(temp_file.name)

    # Run detection with spinner
    with st.spinner("🔍 Detecting solar panels..."):
        results = model(temp_file.name)

    # Plot detection image
    result_image = results[0].plot()

    # Display detection result
    with col2:
        st.subheader("✅ Detection Result")

        st.image(
            result_image,
            use_column_width=True
        )

    # Count detections
    total_detections = len(results[0].boxes)

    # Display metrics
    st.markdown("---")
    st.success(
        f"☀️ Total Solar Panels Detected: {total_detections}"
    )

    # ---------------- INSIGHTS ---------------- #
    st.subheader("📊 Detection Insights")

    st.write(f"""
The YOLOv8 model detected **{total_detections} solar panel(s)** from the uploaded image.
This demonstrates how Computer Vision can be applied to renewable energy analysis and automated solar infrastructure monitoring
The detection process highlights the ability of AI systems to identify solar installations across different environments and image conditions.
""")

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.caption(
    "Developed by Nsisong using YOLOv8, Streamlit, and Computer Vision"
)
