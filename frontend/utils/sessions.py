import streamlit as st


def initialize_session_state():
    if "questions" not in st.session_state:
        st.session_state.questions = []

    if "quiz_generated" not in st.session_state:
        st.session_state.quiz_generated = False

    if "result" not in st.session_state:
        st.session_state.result = None

    if "current_page" not in st.session_state:
        st.session_state.current_page = "form"
        
    if "user" not in st.session_state:
        st.session_state.user = None
        
    if "access_token" not in st.session_state:
        st.session_state.access_token = None


def reset_quiz():
    st.session_state.questions = []
    st.session_state.quiz_generated = False
    st.session_state.result = None
    st.session_state.current_page = "form"

    for key in list(st.session_state.keys()):
        if key.startswith("q_"):
            del st.session_state[key]
            
def logout_user():
    st.session_state.user = None
    st.session_state.access_token = None
    st.session_state.current_page_nav = "Home"