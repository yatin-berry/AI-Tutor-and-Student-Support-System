import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Trigger hot reload for landing.py
from frontend.components.quiz_form import render_quiz_form
from frontend.components.quiz_display import render_quiz_display
from frontend.components.result_display import render_result_display
from frontend.components.dashboard import render_dashboard
from frontend.components.interview import render_interview
from frontend.components.auth import render_auth
from frontend.utils.sessions import initialize_session_state, reset_quiz, logout_user
from frontend.pages.landing import main as render_landing
from frontend.pages.about import main as render_about
from frontend.pages.contact import main as render_contact
from frontend.utils.style_loader import load_custom_css

st.set_page_config(
    page_title="Mentra AI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_custom_css()
initialize_session_state()

if "current_page_nav" not in st.session_state:
    st.session_state.current_page_nav = "Home"

def set_page(page_name):
    st.session_state.current_page_nav = page_name

# --- AUTH-FIRST ROUTING ---
if not getattr(st.session_state, "user", None):
    render_auth()
else:
    # --- FIXED TOP NAVBAR (ONLY VISIBLE IF LOGGED IN) ---
    with st.container():
        col_logo, col_space, col_home, col_quiz, col_interview, col_dash, col_auth = st.columns([2.5, 0.5, 1, 1, 1, 1.2, 1], vertical_alignment="center")
        
        with col_logo:
            st.markdown("<div id='fixed-navbar-target'></div>", unsafe_allow_html=True)
            if st.button("Mentra AI", key="nav_logo_btn", use_container_width=True):
                set_page("Home")
                st.rerun()
                
        with col_home:
            if st.button("Home", type="primary" if st.session_state.current_page_nav == "Home" else "secondary", use_container_width=True):
                set_page("Home")
                st.rerun()
                
        with col_quiz:
            if st.button("Quiz", type="primary" if st.session_state.current_page_nav == "Quiz" else "secondary", use_container_width=True):
                set_page("Quiz")
                st.rerun()
                
        with col_interview:
            if st.button("Interview", type="primary" if st.session_state.current_page_nav == "Interview" else "secondary", use_container_width=True):
                set_page("Interview")
                st.rerun()
                
        with col_dash:
            if st.button("Dashboard", type="primary" if st.session_state.current_page_nav == "Dashboard" else "secondary", use_container_width=True):
                set_page("Dashboard")
                st.rerun()
                
        with col_auth:
            if st.button("Logout", type="secondary", use_container_width=True):
                logout_user()
                st.rerun()

    st.markdown("<div class='main-spacer'></div>", unsafe_allow_html=True)

    selected_page = st.session_state.current_page_nav

    if selected_page == "Home":
        render_landing()

    elif selected_page == "About Us":
        render_about()
        
    elif selected_page == "Contact":
        render_contact()

    elif selected_page == "Dashboard":
        render_dashboard()

    elif selected_page == "Interview":
        render_interview()

    else:
        # Quiz flow (default)
        current_page = st.session_state.get("current_page", "form")

        if current_page == "form":
            render_quiz_form(reset_quiz)
        elif current_page == "quiz":
            render_quiz_display()
        elif current_page == "result":
            render_result_display()