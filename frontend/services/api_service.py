import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"

def get_headers():
    headers = {}
    if "access_token" in st.session_state and st.session_state.access_token:
        headers["Authorization"] = f"Bearer {st.session_state.access_token}"
    return headers

def signup(email, password):
    response = requests.post(f"{BASE_URL}/auth/signup", json={"email": email, "password": password})
    return response.json()

def login(email, password):
    response = requests.post(f"{BASE_URL}/auth/login", json={"email": email, "password": password})
    return response.json()

def generate_questions(subject, topic, level, num_questions=5):
    response = requests.post(
        f"{BASE_URL}/generate-questions",
        json={
            "subject": subject,
            "topic": topic,
            "level": level,
            "num_questions": num_questions
        },
        headers=get_headers()
    )
    return response.json()


def submit_quiz(subject, topic, level, questions, answers):
    response = requests.post(
        f"{BASE_URL}/submit-quiz",
        json={
            "subject": subject,
            "topic": topic,
            "level": level,
            "questions": questions,
            "answers": answers
        },
        headers=get_headers()
    )
    return response.json()

def get_dashboard():
    response = requests.get(f"{BASE_URL}/dashboard", headers=get_headers())
    return response.json()

def start_interview(role, level, total_questions=3):
    response = requests.post(
        f"{BASE_URL}/start-interview",
        json={
            "role": role,
            "level": level,
            "total_questions": total_questions
        },
        headers=get_headers()
    )
    return response.json()


def submit_interview_answer(session_id, answer):
    response = requests.post(
        f"{BASE_URL}/submit-interview-answer",
        json={
            "session_id": session_id,
            "answer": answer
        },
        headers=get_headers()
    )
    return response.json()