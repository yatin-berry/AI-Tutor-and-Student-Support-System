import streamlit as st

def main():
    st.markdown("""
        <style>
        /* Hero Section */
        .hero-container {
            text-align: center;
            padding: 3rem 1rem 1rem 1rem;
            animation: fadeIn 1s ease-out;
        }
        .hero-title {
            font-size: 4.5rem !important;
            font-weight: 800 !important;
            margin-bottom: 8px !important;
            background: linear-gradient(135deg, #ffffff 0%, #a3b1c6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -2px;
        }
        .hero-subtitle {
            font-size: 1.3rem;
            color: #94a3b8;
            margin-top: 0px;
            margin-bottom: 30px;
            font-weight: 400;
        }
        
        /* Value Strip */
        .value-strip {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            gap: 25px;
            background: rgba(255, 255, 255, 0.03);
            padding: 14px 35px;
            border-radius: 50px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            margin: 0 auto;
            width: fit-content;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
            backdrop-filter: blur(10px);
            animation: fadeIn 1.2s ease-out;
        }
        .value-strip span {
            font-size: 0.95rem;
            font-weight: 600;
            color: #cbd5e1;
            display: flex;
            align-items: center;
        }
        
        /* Action Cards container */
        div[data-testid="stHorizontalBlock"]:has(#landing-action-cards) > div[data-testid="column"]:has(.action-card-text) > div[data-testid="stVerticalBlock"] {
            background: rgba(25, 30, 40, 0.5) !important;
            border-radius: 20px !important;
            padding: 24px 16px !important;
            border: 1px solid rgba(255, 255, 255, 0.06) !important;
            backdrop-filter: blur(16px) !important;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
            text-align: center !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15) !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
            animation: slideUp 0.8s ease-out backwards;
            height: 100%;
        }
        
        div[data-testid="stHorizontalBlock"]:has(#landing-action-cards) > div[data-testid="column"]:nth-child(2):has(.action-card-text) > div[data-testid="stVerticalBlock"] { animation-delay: 0.1s; }
        div[data-testid="stHorizontalBlock"]:has(#landing-action-cards) > div[data-testid="column"]:nth-child(3):has(.action-card-text) > div[data-testid="stVerticalBlock"] { animation-delay: 0.2s; }
        div[data-testid="stHorizontalBlock"]:has(#landing-action-cards) > div[data-testid="column"]:nth-child(4):has(.action-card-text) > div[data-testid="stVerticalBlock"] { animation-delay: 0.3s; }

        div[data-testid="stHorizontalBlock"]:has(#landing-action-cards) > div[data-testid="column"]:has(.action-card-text) > div[data-testid="stVerticalBlock"]:hover {
            transform: translateY(-8px) !important;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            background: rgba(35, 40, 50, 0.8) !important;
        }
        
        /* Inside Action Card */
        .action-card-text h2 {
            font-size: 3rem !important;
            margin-bottom: 10px !important;
        }
        .action-card-text h4 {
            font-size: 1.3rem !important;
            color: #f8fafc !important;
            font-weight: 700 !important;
            margin-bottom: 8px !important;
            letter-spacing: -0.5px !important;
        }
        .action-card-text p {
            font-size: 0.95rem !important;
            color: #94a3b8 !important;
            margin-bottom: 25px !important;
            line-height: 1.5 !important;
        }
        
        /* Micro Tagline */
        .micro-tagline {
            text-align: center;
            font-size: 0.9rem;
            color: #64748b;
            margin-top: 5rem;
            font-weight: 500;
            letter-spacing: 0.5px;
            animation: fadeIn 1.5s ease-out;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        </style>
    """, unsafe_allow_html=True)
        
    user = getattr(st.session_state, "user", None)
    email = user["email"] if hasattr(user, "email") else (user.get("email") if isinstance(user, dict) else "Student")
    username = email.split('@')[0].title()
    
    st.markdown(f"""
        <div class="hero-container">
            <h1 class="hero-title">Welcome back, {username}!</h1>
            <p class="hero-subtitle">Ready to continue your learning journey?</p>
            <p style="color: #cbd5e1; max-width: 600px; margin: 0 auto; font-size: 1.05rem; line-height: 1.5; margin-bottom: 20px;">
                Mentra AI is your intelligent platform designed to generate contextual quizzes, simulate technical interviews, and provide deep analytics to identify your weak spots and boost your performance.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Quick Value Strip
    st.markdown("""
        <br>
        <div class='value-strip'>
            <span>🧠 AI-Powered Quiz</span> 
            <span style="color: #475569;">•</span>
            <span>⚡ Instant Feedback</span> 
            <span style="color: #475569;">•</span>
            <span>📊 Progress Tracking</span>
        </div>
        <br><br><br>
        <h3 style='text-align: center; margin-bottom: 2rem; font-weight: 700; color: #f8fafc;'>Choose your path</h3>
    """, unsafe_allow_html=True)

    # Main Action Section
    st.markdown("<div id='landing-action-cards'></div>", unsafe_allow_html=True)
    
    # Using 3 clean columns for the 3 main features
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("<div class='action-card-text'><h2>🧠</h2><h4>Quiz Mode</h4><p>Master any subject with AI-generated questions tailored to your level.</p></div>", unsafe_allow_html=True)
        if st.button("Generate Quiz", key="btn_qz", use_container_width=True, type="secondary"):
            st.session_state.current_page_nav = "Quiz"
            st.rerun()
            
    with col2:
        st.markdown("<div class='action-card-text'><h2>🎤</h2><h4>Interview Mode</h4><p>Train for your dream job with realistic, role-specific mock interviews.</p></div>", unsafe_allow_html=True)
        if st.button("Start Interview", key="btn_in", use_container_width=True, type="secondary"):
            st.session_state.current_page_nav = "Interview"
            st.rerun()
            
    with col3:
        st.markdown("<div class='action-card-text'><h2>📊</h2><h4>Dashboard</h4><p>Analyze your results and identify exactly where to improve.</p></div>", unsafe_allow_html=True)
        if st.button("View Analytics", key="btn_db", use_container_width=True, type="secondary"):
            st.session_state.current_page_nav = "Dashboard"
            st.rerun()

    # Micro Tagline
    st.markdown("<p class='micro-tagline'>✨ Personalized learning powered by Mentra AI</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()