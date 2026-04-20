import streamlit as st

def main():
    st.markdown("""
        <style>
        .about-header {
            text-align: center;
            margin-top: 2rem;
            margin-bottom: 3rem;
            animation: fadeIn 0.8s ease-out;
        }
        .about-header h1 {
            font-size: 3.5rem !important;
            background: linear-gradient(135deg, #ffffff 0%, #a3b1c6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800 !important;
        }
        .about-header p {
            color: #94a3b8;
            font-size: 1.2rem;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        .about-card {
            background: rgba(25, 30, 40, 0.5);
            border-radius: 20px;
            padding: 30px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(16px);
            margin-bottom: 2rem;
            transition: all 0.3s ease;
            animation: slideUp 0.8s ease-out;
        }
        .about-card:hover {
            transform: translateY(-5px);
            border-color: rgba(255, 255, 255, 0.15);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        .about-card h3 {
            color: #f8fafc;
            margin-bottom: 15px;
            font-size: 1.5rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .about-card p {
            color: #cbd5e1;
            line-height: 1.7;
            font-size: 1.05rem;
        }
        </style>
        
        <div class="about-header">
            <h1>About Us</h1>
            <p>Empowering students to learn smarter, practice better, and ace their interviews using the power of Artificial Intelligence.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("""
            <div class="about-card" style="height: 100%;">
                <h3>🎯 Our Purpose</h3>
                <p>Mentra AI was built with a singular vision: to democratize high-quality, personalized education. We believe that every student deserves a private tutor that adapts to their learning pace, identifies their weak areas, and provides real-time, actionable feedback.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="about-card" style="height: 100%;">
                <h3>🤖 How AI Helps Learning</h3>
                <p>By leveraging advanced language models, our platform can generate contextual quizzes, evaluate subjective answers with granular explanations, and simulate high-pressure technical interviews. It doesn't just grade you—it explains the 'why' behind every correct and incorrect answer.</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
        <div class="about-card">
            <h3>✨ Key Benefits</h3>
            <ul style="color: #cbd5e1; line-height: 1.8; font-size: 1.05rem;">
                <li><b>Personalized Practice:</b> Focus on areas you actually need help with instead of generic questions.</li>
                <li><b>Comprehensive Evaluation:</b> Move beyond multiple-choice. Write real code or essays and get graded accurately.</li>
                <li><b>Continuous Improvement:</b> Track your progress over time through deep analytics and interactive dashboards.</li>
                <li><b>Interview Readiness:</b> Face realistic mock interview scenarios tailored to specific roles like Software Engineer or Data Scientist.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
