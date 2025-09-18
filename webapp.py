import google.generativeai as genai
import os
import streamlit as st
from pdfextractor import text_extractor_pdf
from docxextractor import text_extractor
from imageextractor import extract_text_image


# ================== PAGE CONFIG ==================
st.set_page_config(page_title="AI Assisted MoM Generator", page_icon="📝", layout="wide")

# ================== CUSTOM CSS ==================
st.markdown("""
    <style>
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #2c3e50, #4ca1af);
            color: white;
        }
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] h4 {
            color: #f8f9fa !important;
        }

        /* Main title */
        .main-title {
            font-size: 32px !important;
            font-weight: bold;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 15px;
        }

        /* Subtitle */
        .subtitle {
            font-size: 20px !important;
            font-weight: 500;
            color: #28a745;
            text-align: center;
            margin-bottom: 25px;
        }

        /* Tips box */
        .tips-box {
            background: #1e1e1e; /* dark background */
            border-left: 5px solid #17a2b8;
            padding: 12px;
            border-radius: 8px;
            font-size: 15px;
            margin-bottom: 20px;
            color: #f8f9fa;  /* light text */
        }
        .tips-box b {
            color: #00c6ff; /* highlight important words */
        }

        /* Button styling */
        .stButton>button {
            background: linear-gradient(90deg, #007bff, #00c6ff);
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #0056b3, #0099cc);
            transform: scale(1.05);
        }

        /* Download button */
        [data-testid="stDownloadButton"]>button {
            background: #28a745;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 8px 18px;
            transition: 0.3s;
        }
        [data-testid="stDownloadButton"]>button:hover {
            background: #218838;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)


# ================== CONFIGURE MODEL ==================
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-2.5-flash-lite')


# ================== SIDEBAR ==================
st.sidebar.title("📂 UPLOAD YOUR MOM NOTES HERE")
st.sidebar.subheader("Please upload your file in the correct format:")
st.sidebar.info("Supported formats: **PDF, DOCX, PNG, JPG, JPEG**")

user_text = None
user_file = st.sidebar.file_uploader("Upload your file", type=['pdf','docx','png','jpg','jpeg'])
if user_file:
    if user_file.type == 'application/pdf':
        user_text = text_extractor_pdf(user_file)
    elif user_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        user_text = text_extractor(user_file)
    elif user_file.type in ['image/png','image/jpg','image/jpeg']:
        user_text = extract_text_image(user_file)
    else:
        st.sidebar.error('❌ Please upload a correct file format')


# ================== MAIN PAGE ==================
st.markdown('<div class="main-title">📝 MINUTES OF MEETING</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI assisted MoM generator in a standardized format</div>', unsafe_allow_html=True)

tips = """
<div class="tips-box">
<b>💡 Tips to use this app:</b>
<ul>
<li>Upload your meeting notes in the sidebar (Image, PDF or DOCX)</li>
<li>Click on <b>Generate MoM</b> to get standardized minutes of meeting</li>
<li>Download the generated MoM in one click</li>
</ul>
</div>
"""
st.markdown(tips, unsafe_allow_html=True)


# ================== BUTTON TO GENERATE ==================
if st.button('🚀 Generate MoM'):
    if user_text is None:
        st.error('⚠️ No text extracted from file. Please upload again.')
    else:
        with st.spinner('⏳ Processing your data...'):
            prompt = f'''Assume you are expert in creating minutes of meeting.user has provided
            notes of meeting in text formate.using this data you need to create a standardized
            minutes of meeting for the user.
            
            Output must follow word/docx format,strictly 
            title:Title of meeting
            Heading : Meeting Agenda
            subheading : Name of attendees(if attendees name is not there keep it Na)
            subheading:date of meeting and place of meeting (place means name of conference/meeting room if  not provided  keep it online) 
            Body: The body must follow the following sequence of points
            * Key points discussed
            * Highlight any decision that has been fianlised,
            * mention actionable items.
            * Any additional notes.
            * Any deadline that has been discussed.
            * Any next meeting  date that has been discussed.
            * 2 and 3 line of summary.
            * Use bullet points and Highlight or bolt important keywords such the context is clear.
            * Generate the output in such a way that it can be copied and paste in word
            
            The data provided by user is a follows{user_text}'''

            response = model.generate_content([prompt])
            st.success("✅ MoM Generated Successfully!")
            st.write(response.text)

            st.download_button(
                label='📥 Download MoM',
                data=response.text,
                file_name='MOM.txt',
                mime='text/plain'
            )
