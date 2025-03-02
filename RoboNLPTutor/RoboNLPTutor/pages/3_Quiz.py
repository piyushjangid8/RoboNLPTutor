import streamlit as st
import random
from utils.quiz import get_quiz, evaluate_quiz
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

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

# Initialize session state for quiz
if 'quiz' not in st.session_state:
    st.session_state.quiz = None
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = []
if 'show_explanation' not in st.session_state:
    st.session_state.show_explanation = False

def load_quiz(topic):
    quiz = get_quiz(topic)
    if quiz:
        random.shuffle(quiz)
        for question in quiz:
            random.shuffle(question['options'])
    return quiz

def display_question(question):
    st.markdown(f"### {question['question']}")
    for i, option in enumerate(question['options']):
        if st.button(option, key=f"option_{i}"):
            st.session_state.user_answers.append({
                'question': question['question'],
                'selected': option,
                'correct': question['correct'],
                'explanation': question['explanation'],
                'options': question['options']
            })
            st.session_state.show_explanation = True

def display_explanation(answer):
    st.markdown(f"**Your Answer:** {answer['selected']}")
    if answer['selected'] == answer['correct']:
        st.markdown("**Correct!**")
    else:
        st.markdown(f"**Incorrect!** The correct answer is: {answer['correct']}")
    st.markdown(f"**Explanation:** {answer['explanation']}")
    st.markdown("**Other Options:**")
    for option in answer['options']:
        if option != answer['correct']:
            st.markdown(f"- {option}")

def display_final_result():
    score = evaluate_quiz([ans['selected'] for ans in st.session_state.user_answers],
                          [ans['correct'] for ans in st.session_state.user_answers])
    st.markdown(f"## Your Final Score: {score:.1f}%")
    for answer in st.session_state.user_answers:
        st.markdown(f"### {answer['question']}")
        display_explanation(answer)

# Main quiz logic
def main():
    st.title("Quiz Game")
    topics = ["python", "data_science", "robotics"]
    
    if st.session_state.quiz is None:
        topic = st.selectbox("Select a topic", topics)
        if st.button("Start Quiz"):
            st.session_state.quiz = load_quiz(topic)
            st.session_state.current_question = 0
            st.session_state.user_answers = []
            st.session_state.show_explanation = False
    
    if st.session_state.quiz:
        if st.session_state.current_question < len(st.session_state.quiz):
            question = st.session_state.quiz[st.session_state.current_question]
            if not st.session_state.show_explanation:
                display_question(question)
            else:
                display_explanation(st.session_state.user_answers[-1])
                if st.button("Next Question"):
                    st.session_state.current_question += 1
                    st.session_state.show_explanation = False
        else:
            display_final_result()

if __name__ == "__main__":
    main()
