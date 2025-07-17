import streamlit as st
from PIL import Image
from pathlib import Path
import google.generativeai as genai
from api_key import api_key
import re

st.set_page_config(
    page_title="AI Medical Imaging Assistant",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown("""
    <style>
    .report-title {
        font-size: 30px;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .section-header {
        font-size: 20px;
        font-weight: 500;
        margin-top: 25px;
        color: #16a085;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🩺 AI Diagnostic Assistant")
    st.write("Upload a medical image (X-ray, MRI, etc.) for AI-based diagnostic analysis using Gemini.")

st.markdown("<div class='report-title'>Medical Image Diagnostic Report</div>", unsafe_allow_html=True)
uploaded_img = st.file_uploader("Upload a medical image", type=["jpg", "jpeg", "png"])

if uploaded_img:
    img = Image.open(uploaded_img)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    if st.button("🧠 Analyze Image"):
        with st.spinner("Analyzing image. Please wait..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-2.5-pro')

                prompt = """
                You are an advanced AI medical imaging specialist with expertise equivalent to a senior radiologist, trained to evaluate a wide range of diagnostic scans including X-rays, MRIs, CT scans, and medical photographs.  
                Your task is to carefully analyze the uploaded medical image(s) and return a *comprehensive diagnostic report* that includes the following sections:

                ---

                *1. Preliminary Overview:*  
                - Describe what the image likely represents (e.g., body part, scan type).  
                - Mention any quality issues (blurring, obstruction, etc.)

                ---

                *2. Detailed Clinical Observations:*  
                - Identify all visible abnormalities, anomalies, or patterns.  
                - Use standard medical terms and explain when needed.  
                - Point out location-specific findings and any urgent signs.

                ---

                *3. Differential Diagnosis (with reasoning):*  
                - List most likely diagnoses with justifications.  
                - Mention if normal findings are present but need monitoring.

                ---

                *4. Recommended Next Steps:*  
                - Suggest additional scans, blood tests, biopsies, or referrals.  
                - Mention what should be correlated with patient history.

                ---

                *5. General Treatment Recommendations:*  
                - Provide typical treatments for the likely condition.  
                - Include a disclaimer that this is not medical advice.

                ---

                *6. Risk Factors & Warnings:*  
                - Highlight risk factors inferred from the image.  
                - Mention any critical signs requiring immediate action.

                ---

                *7. Notes for Human Physician Review:*  
                - Mention ambiguities or areas needing expert interpretation.  
                - State clearly if image quality is insufficient for confident analysis.

                ---

                Patient Information: 
                """

                response = model.generate_content([prompt, img])
                result = response.text

                for i, section in enumerate(result.split('---')):
                    section = section.strip()
                    if not section:
                        continue

                    if i == 0 and not section.lower().startswith("*1. "):
                        continue

                    raw_header = section.split('\n')[0]
                    header = re.sub(r"[*#]+", "", raw_header)         
                    header = re.sub(r"^\s*\d+[:.)-]?\s*", "", header)  
                    header = header.strip()
                    content = "\n".join(section.split('\n')[1:]).strip()

                    with st.expander(f"📄 {header}"):
                        st.markdown(content)

            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a medical image to begin diagnosis.")
