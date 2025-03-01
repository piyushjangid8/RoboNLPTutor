import streamlit as st
from utils.quiz import get_quiz, evaluate_quiz
from datetime import datetime

st.set_page_config(page_title="Quizzes", page_icon="📝")

# Initialize session state if needed
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = {
        "completed": 0,
        "current_level": "Beginner",
        "completed_tasks": [],
        "quiz_scores": [],
        "notes": []
    }

st.title("📝 Knowledge Check")

# Quiz topic selection
topic = st.selectbox(
    "Select a topic for your quiz:",
    ["python", "data_science", "robotics"]
)

if 'current_quiz' not in st.session_state or st.session_state.quiz_submitted:
    st.session_state.current_quiz = get_quiz(topic)
    st.session_state.user_answers = [None] * len(st.session_state.current_quiz)
    st.session_state.quiz_submitted = False

if not st.session_state.quiz_submitted:
    # Display questions
    for i, question in enumerate(st.session_state.current_quiz):
        st.write(f"\n**Question {i+1}: {question['question']}**")

        answer = st.radio(
            f"Select your answer for question {i+1}:",
            question['options'],
            index=None,
            key=f"q_{i}"
        )

        if answer is not None:
            st.session_state.user_answers[i] = question['options'].index(answer)

    if st.button("Submit Quiz"):
        if None in st.session_state.user_answers:
            st.warning("Please answer all questions before submitting.")
        else:
            # Calculate score
            correct_answers = [q['correct'] for q in st.session_state.current_quiz]
            score = evaluate_quiz(st.session_state.user_answers, correct_answers)

            # Ensure score is a float
            try:
                score = float(score)
            except (ValueError, TypeError):
                score = 0.0

            # Store score in session state
            if 'quiz_scores' not in st.session_state.user_progress:
                st.session_state.user_progress['quiz_scores'] = []
            st.session_state.user_progress['quiz_scores'].append({
                'topic': topic,
                'score': score,  # Store as float directly
                'date': datetime.now().strftime("%Y-%m-%d")
            })

            st.session_state.quiz_submitted = True
            st.rerun()
else:
    # Display results
    st.header("Quiz Results")
    
    if st.session_state.user_progress['quiz_scores']:
        last_score = st.session_state.user_progress['quiz_scores'][-1].get('score', 0)
        try:
            score = float(last_score)  # Ensure it's a float
        except (ValueError, TypeError):
            score = 0.0
        st.write(f"Your score: {score:.1f}%")
    else:
        st.warning("No quiz scores available yet.")
        score = 0.0

    if score >= 80:
        st.success("Excellent work! 🎉")
    elif score >= 60:
        st.info("Good job! Keep practicing! 📚")
    else:
        st.warning("You might want to review this topic again. 📖")

    if st.button("Take Another Quiz"):
        st.session_state.current_quiz = get_quiz(topic)
        st.session_state.user_answers = [None] * len(st.session_state.current_quiz)
        st.session_state.quiz_submitted = False
        st.rerun()
