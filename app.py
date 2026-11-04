import streamlit as st
import time
from translatepy import Translator
import pyperclip

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍"
)

st.markdown("""
<style>

/* ------------------ PAGE BACKGROUND ------------------ */

.stApp{
    background: linear-gradient(
        135deg,
        #0F172A 0%,
        #1E293B 45%,
        #312E81 100%
    );
}

/* ------------------ HIDE STREAMLIT ------------------ */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* ------------------ MAIN CONTAINER ------------------ */

.block-container{

    max-width:950px;

    margin:auto;

    padding:50px;

    border-radius:30px;

    background:rgba(255,255,255,0.08);

    backdrop-filter:blur(20px);

    border:1px solid rgba(255,255,255,0.12);

    box-shadow:
    0px 15px 40px rgba(0,0,0,0.35);

}

/* ------------------ TITLE ------------------ */

.main-title{

    text-align:center;

    font-size:50px;

    font-family:Georgia, serif;

    font-weight:700;

    letter-spacing:1px;

    margin-bottom:10px;

    background:linear-gradient(
    90deg,
    #FDA4AF,
    #C4B5FD,
    #93C5FD
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* ------------------ SUBTITLE ------------------ */

.subtitle{

    text-align:center;

    color:#E2E8F0;

    font-size:18px;

    margin-bottom:35px;

    font-family:'Segoe UI',sans-serif;
}

/* ------------------ LABELS ------------------ */

label{

    color:white !important;

    font-weight:600 !important;

    font-family:'Segoe UI',sans-serif;
}

/* ------------------ TEXT AREA ------------------ */

.stTextArea textarea{

    background:#111827 !important;

    color:white !important;

    border:2px solid #6366F1 !important;

    border-radius:18px !important;

    padding:15px !important;

    font-size:16px !important;

    box-shadow:
    0 0 15px rgba(99,102,241,.15);

}

/* ------------------ SELECT BOX ------------------ */

div[data-baseweb="select"]{

    background:#111827 !important;

    border-radius:15px !important;

}

/* ------------------ BUTTON ------------------ */

.stButton > button{

    width:100%;

    height:58px;

    border:none;

    border-radius:18px;

    font-size:18px;

    font-weight:700;

    color:white;

    background:linear-gradient(
    90deg,
    #EC4899,
    #8B5CF6,
    #3B82F6
    );

    box-shadow:
    0 8px 25px rgba(139,92,246,.45);

    transition:0.3s ease;
}

.stButton > button:hover{

    transform:translateY(-2px);

    box-shadow:
    0 0 25px rgba(139,92,246,.6);
}

/* ------------------ SUCCESS BOX ------------------ */

.stSuccess{

    border-radius:18px !important;

    background:rgba(255,255,255,0.08) !important;

}

/* ------------------ SIDEBAR ------------------ */

section[data-testid="stSidebar"]{

    background:#0F172A;

}


</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-title">
Language Translation Tool
</div>

<div class="subtitle">
Translate Beyond Boundaries
</div>
""", unsafe_allow_html=True)

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh",
    "Russian": "ru",
    "Arabic": "ar",
    "Italian": "it",
    "Portuguese": "pt",
    "Korean": "ko"
}

source_lang = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Target Language",
    list(languages.keys())
)

text = st.text_area("Enter Text Here")

col1, col2 = st.columns([8,1])

with col1:
    translate_btn = st.button("🚀 Translate")

with col2:
    copy_btn = st.button("📋 Copy")

if copy_btn:
    if "translated_text" in st.session_state:
        st.success("Text Ready to Copy ✅")
        st.code(st.session_state["translated_text"])

if translate_btn:
    if text.strip() == "":
       st.warning("Please enter text")

    elif source_lang == target_lang:
       st.warning("Please select different languages.")

    else:
        try:

            with st.spinner("Translating..."):

               translator = Translator()

               translated = translator.translate(
                  text,
                  languages[target_lang]
               ).result

               st.session_state["translated_text"] = translated
               
            st.success("Translation Completed ✅")

            st.text_area(
               "Translated Text",
                value=translated,
                height=150
            )                                                                                                   

            st.download_button(
                "📥 Download Translation",
                translated,
                file_name="translation.txt",
                mime="text/plain"
            )
        except Exception as e:
          st.error(f"Error: {str(e)}")

        