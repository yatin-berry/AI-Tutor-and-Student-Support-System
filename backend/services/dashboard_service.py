from backend.services.db_services import (
    get_all_attempts,
    get_recent_attempts,
    get_all_interviews,
    get_recent_interviews
)


def get_dashboard_data(user_id: str):
    quiz_attempts = get_all_attempts(user_id)
    interview_attempts = get_all_interviews(user_id)

    recent_quiz = get_recent_attempts(user_id)
    recent_interviews = get_recent_interviews(user_id)

    total_quiz = len(quiz_attempts)
    total_interviews = len(interview_attempts)

    # 🔹 QUIZ METRICS
    total_score_sum = sum(item.get("total_score", 0) for item in quiz_attempts)
    accuracy_sum = sum(item.get("accuracy", 0) for item in quiz_attempts)

    avg_score = round(total_score_sum / total_quiz, 2) if total_quiz else 0
    avg_accuracy = round(accuracy_sum / total_quiz, 2) if total_quiz else 0

    # 🔹 SUBJECT-WISE STATS
    subject_map = {}

    for item in quiz_attempts:
        subject = item.get("subject", "Unknown")

        if subject not in subject_map:
            subject_map[subject] = {
                "subject": subject,
                "attempts": 0,
                "score_sum": 0,
                "accuracy_sum": 0
            }

        subject_map[subject]["attempts"] += 1
        subject_map[subject]["score_sum"] += item.get("total_score", 0)
        subject_map[subject]["accuracy_sum"] += item.get("accuracy", 0)

    subject_stats = []

    for subject, data in subject_map.items():
        attempts = data["attempts"]

        subject_stats.append({
            "subject": subject,
            "attempts": attempts,
            "average_score": round(data["score_sum"] / attempts, 2),
            "average_accuracy": round(data["accuracy_sum"] / attempts, 2)
        })

    subject_stats = sorted(subject_stats, key=lambda x: x["attempts"], reverse=True)

    # 🔹 INTERVIEW METRICS
    interview_score_sum = sum(item.get("average_score", 0) for item in interview_attempts)
    avg_interview_score = round(interview_score_sum / total_interviews, 2) if total_interviews else 0

    # 🔹 ROLE-WISE STATS
    role_map = {}

    for item in interview_attempts:
        role = item.get("role", "Unknown")

        if role not in role_map:
            role_map[role] = {
                "role": role,
                "attempts": 0,
                "score_sum": 0
            }

        role_map[role]["attempts"] += 1
        role_map[role]["score_sum"] += item.get("average_score", 0)

    role_stats = []

    for role, data in role_map.items():
        attempts = data["attempts"]

        role_stats.append({
            "role": role,
            "attempts": attempts,
            "average_score": round(data["score_sum"] / attempts, 2)
        })

    role_stats = sorted(role_stats, key=lambda x: x["attempts"], reverse=True)

    return {
        "total_quiz_attempts": total_quiz,
        "average_quiz_score": avg_score,
        "average_accuracy": avg_accuracy,

        "subject_stats": subject_stats,

        "total_interviews": total_interviews,
        "average_interview_score": avg_interview_score,
        "role_stats": role_stats,

        "recent_quiz": recent_quiz,
        "recent_interviews": recent_interviews
    }