import streamlit as st
from frontend.services.api_service import submit_quiz


def render_quiz_display():
    if not st.session_state.quiz_generated or not st.session_state.questions:
        st.warning("Please generate a quiz first.")
        return

    if "loading" not in st.session_state:
        st.session_state.loading = False

    st.subheader("Answer the Questions")
    st.markdown("---")

    # Initialize answer state if not exists
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}

    for i, q in enumerate(st.session_state.questions):
        with st.container():
            st.markdown(f"#### Q{i+1}. {q['question']}")
            st.markdown(f"<span style='color: #818cf8; font-size: 0.85rem; font-weight: 500;'>TYPE: {q.get('type', 'mcq').replace('_', ' ').upper()}</span>", unsafe_allow_html=True)
            
            q_type = q.get("type", "mcq")
            # Create a unique persistent key for this specific question
            input_key = f"quiz_q_{i}"

            if q_type in ["mcq", "true_false"]:
                # Get existing value from session_state for persistence
                current_val = st.session_state.user_answers.get(i, None)
                
                # Determine index for st.radio
                radio_index = None
                if current_val in q["options"]:
                    radio_index = q["options"].index(current_val)

                answer = st.radio(
                    "Choose your answer:",
                    q["options"],
                    key=input_key,
                    index=radio_index
                )
                st.session_state.user_answers[i] = answer
            else:
                # Get existing value from session_state for persistence
                current_text = st.session_state.user_answers.get(i, "")
                
                answer = st.text_input(
                    "Write your answer:",
                    value=current_text,
                    key=input_key
                )
                st.session_state.user_answers[i] = answer

            st.markdown("<br>", unsafe_allow_html=True)
            st.divider()

    # Pre-calculate answers list for submission
    final_answers = [st.session_state.user_answers.get(i, "").strip() for i in range(len(st.session_state.questions))]

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Back to Form", use_container_width=True, disabled=st.session_state.loading):
            st.session_state.current_page = "form"
            st.rerun()

    with col2:
        submit_clicked = st.button(
            "Submit Answers",
            type="primary",
            use_container_width=True,
            disabled=st.session_state.loading
        )

        if submit_clicked:
            if any(ans == "" for ans in final_answers):
                st.warning("Please answer all questions before submitting.")
            else:
                st.session_state.loading = True
                with st.spinner("Evaluating your answers..."):
                    result = submit_quiz(
                        st.session_state.subject,
                        st.session_state.topic,
                        st.session_state.level,
                        st.session_state.questions,
                        final_answers
                    )

                st.session_state.loading = False
                st.session_state.result = result
                st.session_state.current_page = "result"
                st.rerun()