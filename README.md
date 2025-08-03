# SymptoScan
SymptoScan - An interactive Streamlit web app that allows users to upload medical images (like X-rays, MRIs, CT scans, or dermatological photos) and receive a comprehensive AI-generated diagnostic report. Powered by Google’s Gemini Pro 2.5 multimodal model, this assistant mimics a senior radiologist's expertise and provides clinical insights for uploaded scans.

### Features:
- Upload any medical image (.jpg, .jpeg, .png)
- AI-driven diagnostic analysis using Gemini
- Outputs a multi-section diagnostic report:
- Preliminary overview
- Clinical observations
- Differential diagnoses
- Next steps
- Treatment recommendations
- Risk factors
- Physician notes
- Clean UI with collapsible report sections
- Medical disclaimer included

### Tech Stack:
| Technology                   | Purpose                         |
| ---------------------------- | ------------------------------- |
| **Streamlit**                | Frontend web interface          |
| **Google Generative AI SDK** | Interaction with Gemini Pro 2.5 |
| **PIL (Pillow)**             | Image loading and preview       |
| **Python**                   | Backend logic                   |

### Folder Structure:
project-root/ <br>
│ <br>
├── api_key.py     
├── app.py                  
├── requirements.txt    
└── README.md              

### Running the App:
streamlit run app.py
