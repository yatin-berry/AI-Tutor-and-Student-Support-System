import streamlit as st
from frontend.services.api_service import login, signup

def render_auth():
    st.markdown("""
        <style>
        /* Strict structural override to style the Streamlit column as a card */
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:nth-child(2) > div[data-testid="stVerticalBlock"] {
            padding: 35px !important;
            background: rgba(25, 30, 40, 0.6) !important;
            backdrop-filter: blur(12px) !important;
            border-radius: 20px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4) !important;
        }
        
        /* Strip the default borders off Streamlit forms so our card background shines */
        [data-testid="stForm"] {
            border: none !important;
            padding: 0 !important;
            background: transparent !important;
        }
        
        /* Center the Login / Sign Up Tabs */
        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            justify-content: center !important;
            gap: 20px !important;
            margin-bottom: 10px !important;
        }

        .auth-header {
            text-align: center;
            margin-top: 5vh;
            margin-bottom: 2vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            animation: fadeIn 1s ease-out;
        }
        .auth-title {
            font-size: 3rem !important;
            font-weight: 800 !important;
            background: linear-gradient(135deg, #ffffff 0%, #a3b1c6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0 !important;
            text-align: center;
        }
        .auth-subtitle {
            font-size: 1.2rem;
            color: #94a3b8;
            margin-top: -10px;
            font-weight: 500;
            text-align: center;
        }
        .auth-desc {
            color: #cbd5e1;
            font-size: 0.95rem;
            max-width: 600px;
            margin: 15px auto 40px auto;
            line-height: 1.5;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header section
    st.markdown("""
        <div class="auth-header">
            <h1 class="auth-title">Mentra AI</h1>
            <p class="auth-subtitle">Your AI Tutor for Smart Learning & Interview Prep</p>
            <p class="auth-desc">An intelligent platform designed to generate contextual quizzes, simulate technical interviews, and provide deep analytics to identify your weak spots.</p>
        </div>
    """, unsafe_allow_html=True)

    # Centered authentication card
    _, col_auth, _ = st.columns([1, 1.5, 1], vertical_alignment="center", gap="large")

    with col_auth:
        st.markdown("<div id='auth-card-marker'></div>", unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["Login", "Sign Up"])

        with tab1:
            with st.form("login_form"):
                st.subheader("Login to your account")
                email = st.text_input("Email", key="login_email")
                password = st.text_input("Password", type="password", key="login_password")
                submitted = st.form_submit_button("Login", type="primary", use_container_width=True)

                if submitted:
                    if not email or not password:
                        st.error("Please enter email and password.")
                    else:
                        with st.spinner("Logging in..."):
                            res = login(email, password)
                            if "status" in res and res["status"] == "success":
                                st.session_state.user = res["session"]["user"]
                                st.session_state.access_token = res["session"]["access_token"]
                                st.session_state.current_page_nav = "Home"
                                st.rerun()
                            else:
                                st.error(res.get("detail", "Login failed"))

        with tab2:
            with st.form("signup_form"):
                st.subheader("Create a new account")
                new_email = st.text_input("Email", key="signup_email")
                new_password = st.text_input("Password", type="password", key="signup_password")
                confirm_password = st.text_input("Confirm Password", type="password")
                submitted = st.form_submit_button("Sign Up", type="primary", use_container_width=True)

                if submitted:
                    if not new_email or not new_password:
                        st.error("Please enter email and password.")
                    elif new_password != confirm_password:
                        st.error("Passwords do not match.")
                    else:
                        with st.spinner("Creating account..."):
                            res = signup(new_email, new_password)
                            if "status" in res and res["status"] == "success":
                                st.success("Account created successfully! You can now log in.")
                            else:
                                st.error(res.get("detail", "Signup failed"))
