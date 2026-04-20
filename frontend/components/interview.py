import streamlit as st
from frontend.services.api_service import start_interview, submit_interview_answer


def render_interview():

    st.title("🎤 AI Interview Mode")
    st.caption("Simulate real interview experience with AI")


    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False

    if "loading" not in st.session_state:
        st.session_state.loading = False


    if not st.session_state.interview_started:
        
        col1, col2, col3 = st.columns([2.5, 2, 1.5])
        
        with col1:
            role = st.text_input("Enter Role", placeholder="e.g. ML Engineer")
        with col2:
            level = st.selectbox("Select Level", ["Beginner", "Intermediate", "Advanced"])
        with col3:
            total_questions = st.number_input("Questions", min_value=1, max_value=10, value=3)

        st.markdown("<br>", unsafe_allow_html=True)
        
        btn_col, _ = st.columns([2, 4])
        with btn_col:
            start_clicked = st.button(
                "🚀 Start Interview",
                use_container_width=True,
                type="primary",
                disabled=st.session_state.loading
            )

        if start_clicked:
            if not role.strip():
                st.warning("Please enter a role")
                return

            st.session_state.loading = True

            with st.spinner("Starting interview..."):
                data = start_interview(role, level, total_questions)

            st.session_state.loading = False

            if data.get("status") == "success":
                st.session_state.interview_started = True
                st.session_state.session_id = data["session_id"]
                st.session_state.current_question = data["question"]
                st.session_state.question_number = data["question_number"]
                st.session_state.is_completed = False
                st.session_state.feedback = None
                st.rerun()

    else:
        if not st.session_state.is_completed:

            st.markdown(f"### Question {st.session_state.question_number}")
            st.info(st.session_state.current_question)

            answer = st.text_area("Your Answer", key=f"ans_{st.session_state.session_id}_{st.session_state.question_number}")

            submit_clicked = st.button(
                "Submit Answer",
                use_container_width=True,
                disabled=st.session_state.loading
            )

            if submit_clicked:
                if not answer.strip():
                    st.warning("Please write your answer")
                    return

                st.session_state.loading = True

                with st.spinner("Evaluating answer..."):
                    data = submit_interview_answer(
                        st.session_state.session_id,
                        answer
                    )

                st.session_state.loading = False

                if data.get("status") == "success":

                    st.session_state.feedback = {
                        "score": data.get("last_score"),
                        "feedback": data.get("last_feedback")
                    }

                    if data.get("is_completed"):
                        st.session_state.is_completed = True
                        st.session_state.results = data.get("results")
                        st.session_state.summary = data.get("final_summary")
                    else:
                        st.session_state.current_question = data.get("question")
                        st.session_state.question_number = data.get("question_number")

                    st.rerun()

        else:
            st.success("Interview Completed")

            summary = st.session_state.summary

            st.subheader("Summary")
            st.write(summary.get("summary"))

            st.subheader("Strengths")
            for s in summary.get("strengths", []):
                st.write(f"- {s}")

            st.subheader("Weaknesses")
            for w in summary.get("weaknesses", []):
                st.write(f"- {w}")

            st.subheader("Suggestions")
            for s in summary.get("suggestions", []):
                st.write(f"- {s}")

            restart_clicked = st.button(
                "Start New Interview",
                use_container_width=True,
                disabled=st.session_state.loading
            )

            if restart_clicked:
                for key in list(st.session_state.keys()):
                    if key.startswith("interview") or key in [
                        "session_id",
                        "current_question",
                        "question_number",
                        "results",
                        "summary",
                        "feedback"
                    ]:
                        del st.session_state[key]

                st.rerun()

    if st.session_state.get("feedback"):
        st.markdown("---")
        st.subheader("Feedback")
        st.write(f"Score: {st.session_state.feedback['score']}")
        st.write(st.session_state.feedback["feedback"])