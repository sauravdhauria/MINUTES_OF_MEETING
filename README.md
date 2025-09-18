📝 AI-Assisted Minutes of Meeting (MoM) Generator
- 🚀 Live Demo: https://minutesofmeetingaisaurav.streamlit.app/
- 📌 Overview

The AI-Powered Minutes of Meeting Generator is a Streamlit-based web application that helps convert raw meeting notes into structured, standardized, and professional minutes of meeting (MoM).
It supports multi-format inputs (PDF, DOCX, Images) and leverages Google Gemini AI for text extraction and structured generation of MoMs. The tool is designed for project managers, students, corporates, and teams to streamline documentation.

- ✨ Key Features
- 📂 Multi-format Input: Upload PDF, DOCX, PNG, JPG, JPEG
- 🔍 OCR Support: Extracts text from handwritten/printed meeting notes
- 🤖 AI-Generated MoMs: Summarized, structured, and standardized format
- 📑 Well-Organized Output:


Title of Meeting
- Agenda
- Attendees
- Date & Place
- Key Discussion Points
- Final Decisions
- Action Items & Deadlines
- Next Meeting Schedule
- Summary (2–3 lines)

- 📥 One-Click Download: Export MoM in .txt (easily transferable to Word/PDF)
- 🎨 User-Friendly UI: Modern Streamlit interface with custom styling

🛠️ Tech Stack
- Frontend: Streamlit
- AI Model: Google Gemini 2.5 Flash Lite (via google.generativeai)
- Text Extraction:
- PDF → pdfextractor
- DOCX → docxextractor
- Images → OCR (imageextractor)
- Backend: Python


