import streamlit as st


def render_result_display():
    if not st.session_state.result:
        st.warning("Please submit a quiz first.")
        return

    result = st.session_state.result

    if result.get("status") != "success":
        st.error(result.get("message", "Failed to evaluate quiz."))
        return

    # 🔹 HEADER
    st.subheader("Step 3: Quiz Result")

    st.markdown("## Final Performance")

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric("Total Score", result.get("total_score", 0))

    with metric2:
        st.metric("Total Questions", result.get("total_questions", 0))

    with metric3:
        st.metric("Accuracy", f"{result.get('accuracy', 0)}%")

    # 🔹 SUMMARY
    if result.get("summary"):
        st.markdown("---")
        st.info(result["summary"])

    # 🔹 DETAILED RESULTS
    st.markdown("---")
    st.markdown("## Detailed Evaluation")

    for i, item in enumerate(result.get("results", [])):
        score = item.get("score", 0)

        st.markdown("---")

        st.markdown(f"### Q{i+1}. {item['question']}")

        # 🔹 STATUS BADGE
        if score == 1:
            st.success("Correct")
        elif score == 0.5:
            st.warning("Partially Correct")
        else:
            st.error("Needs Improvement")

        # 🔹 ANSWERS
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Your Answer:**")
            st.write(item["user_answer"])

        with col2:
            st.markdown("**Correct Answer:**")
            st.write(item["correct_answer"])

        st.caption(f"Score: {score}")

        # 🔹 FEEDBACK + EXPLANATION
        with st.expander("Feedback", expanded=True):
            st.write(item["feedback"])

        with st.expander("Explanation", expanded=False):
            st.write(item.get("explanation", "No explanation available"))

    # 🔹 WEAK AREAS
    weak_areas = result.get("weak_areas", [])
    suggestions = result.get("suggestions", [])

    if weak_areas:
        st.markdown("---")
        st.subheader("Weak Areas")

        for area in weak_areas:
            st.write(f"- {area}")

    # 🔹 SUGGESTIONS
    if suggestions:
        st.subheader("Suggestions")

        for suggestion in suggestions:
            st.write(f"- {suggestion}")

    # 🔹 ACTION BUTTONS
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Go to Dashboard", use_container_width=True):
            st.session_state.current_page_nav = "Dashboard"
            st.rerun()

    with col2:
        if st.button("Start New Quiz", type="primary", use_container_width=True):
            st.session_state.questions = []
            st.session_state.quiz_generated = False
            st.session_state.result = None
            st.session_state.current_page = "form"

            for key in list(st.session_state.keys()):
                if key.startswith("q_"):
                    del st.session_state[key]

            st.rerun()