import streamlit as st
from frontend.services.api_service import generate_questions


def render_quiz_form(reset_quiz_callback):
    st.markdown("<h3 style='margin-bottom: 1.5rem;'>🧠 Generate a Quiz</h3>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([2, 2, 1.5, 1.5])

    with col1:
        subject = st.selectbox(
            "Select Subject",
            [
                "Machine Learning",
                "Deep Learning",
                "Natural Language Processing",
                "Computer Vision",
                "Generative AI",
                "Large Language Models",
                "Prompt Engineering"
            ]
        )

    with col2:
        topic = st.text_input("Enter Topic", placeholder="e.g. Transformers")

    with col3:
        level = st.selectbox("Select Level", ["Beginner", "Intermediate", "Advanced"])

    with col4:
        num_questions = st.number_input("Questions", min_value=1, max_value=20, value=5)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Balanced Button Layout
    btn_col1, btn_col2 = st.columns(2, gap="medium")

    with btn_col1:
        if st.button("🚀 Generate Questions", use_container_width=True, type="primary"):
            if not topic.strip():
                st.warning("Please enter a topic.")
            else:
                with st.spinner("Generating questions..."):
                    data = generate_questions(subject, topic, level, int(num_questions))

                if data.get("status") == "success":
                    st.session_state.questions = data["data"]
                    st.session_state.quiz_generated = True
                    st.session_state.result = None
                    st.session_state.user_answers = {}  # Reset answers for new quiz
                    st.session_state.subject = subject
                    st.session_state.topic = topic
                    st.session_state.level = level
                    st.session_state.current_page = "quiz"
                    st.success("Questions generated successfully.")
                    st.rerun()
                else:
                    st.error(data.get("message", "Failed to generate questions."))

    with btn_col2:
        if st.button("🔄 Restart Quiz", use_container_width=True):
            reset_quiz_callback()
            st.rerun()