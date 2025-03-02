import streamlit as st
import plotly.express as px
import pandas as pd
from models.database import init_db, get_session
import nltk
from utils.chatbot import process_user_input, initialize_chatbot
from utils.progress import load_user_progress
from utils.achievements import check_achievements, get_achievement_stats
from utils.microlearning import get_random_tip, format_tip_markdown
import random
from utils.quiz import get_quiz, evaluate_quiz
import time
import os
# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Initialize database
try:
    init_db()
    # Create session and store in session state
    if 'db_session' not in st.session_state:
        st.session_state.db_session = get_session()
except Exception as e:
    st.error(f"Database error: {str(e)}")
    st.warning("Running in local mode without database persistence.")

# Initialize chatbot
initialize_chatbot()

# Load user progress
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = load_user_progress()

st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        max-width: 100%;
        padding: 1rem 2rem;
    }
    .main-header {
        font-size: 2.2rem;
        color: #1E88E5;
        margin: 1rem 0 2rem 0;
        padding: 0.5rem;
        line-height: 1.4;
        word-wrap: break-word;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        margin: 1rem 0;
        padding: 0.5rem;
    }
    .card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .metric-card {
        text-align: center;
        padding: 1rem;
        border-radius: 8px;
        background: linear-gradient(135deg, #1E88E5, #1565C0);
        color: white;
    }
    .chat-container {
        border-radius: 10px;
        background-color: white;
        padding: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = {
        "completed": 0,
        "current_level": "Beginner",
        "completed_tasks": [],
        "quiz_scores": [],
        "notes": []
    }
if 'achievements' not in st.session_state.user_progress:
    st.session_state.user_progress['achievements'] = []

# Store database session in session_state
if 'db_session' not in st.session_state:
    st.session_state.db_session = get_session()

# Main title with custom styling
st.markdown('<div class="main-header">🤖 AI Learning Assistant for Data Science & Robotics</div>', unsafe_allow_html=True)

# Sidebar with progress overview
with st.sidebar:
    st.markdown('<div class="sub-header">Learning Journey</div>', unsafe_allow_html=True)
    progress = st.session_state.user_progress

    # Ensure progress['completed'] is an integer and within 0-100
    completed = int(progress['completed'])
    remaining = 100 - completed

    # Create a DataFrame for the progress chart
    df = pd.DataFrame({
        'Status': ['Completed', 'Remaining'],
        'Value': [completed, remaining]
    })

    # Create progress chart with custom colors
    fig = px.pie(
        df,
        values='Value',
        names='Status',
        title='Overall Progress',
        color_discrete_sequence=['#1E88E5', '#E3F2FD']
    )
    fig.update_layout(
        title_font_size=20,
        showlegend=True,
        legend_orientation="h",
        margin=dict(t=40, b=40)
    )
    st.plotly_chart(fig, use_container_width=True)

    # Metrics in custom styled cards
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <h3>Progress</h3>
                <h2>{progress['completed']}%</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <h3>Level</h3>
                <h2>{progress['current_level']}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Daily Tip
    st.markdown("### 💡 Tip of the Day")
    daily_tip = get_random_tip()
    if daily_tip:
        st.markdown(format_tip_markdown(daily_tip), unsafe_allow_html=True)

# Check for new achievements
new_achievements = check_achievements(st.session_state.user_progress)

# Add this after the sidebar metrics
if new_achievements:
    st.sidebar.markdown("### 🎉 New Achievements!")
    for achievement in new_achievements:
        st.sidebar.markdown(f"""
        <div style="padding: 1rem; background-color: #E3F2FD; border-radius: 10px; margin-bottom: 0.5rem;">
            <span style="font-size: 1.5rem;">{achievement['emoji']}</span>
            <strong>{achievement['title']}</strong>
            <p>{achievement['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Add achievement stats
achievement_stats = get_achievement_stats(st.session_state.user_progress)
st.sidebar.markdown("### 🏆 Achievements")
st.sidebar.progress(achievement_stats['percent_complete'] / 100)
st.sidebar.markdown(f"{achievement_stats['total_earned']}/{achievement_stats['total_available']} Unlocked")

# Main chat interface
st.markdown('<div class="sub-header">Chat with AI Assistant</div>', unsafe_allow_html=True)

# Chat interface with custom styling
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"], avatar="🤖" if message["role"] == "assistant" else "👤"):
            st.write(message["content"])
    st.markdown('</div>', unsafe_allow_html=True)

# User input
user_input = st.chat_input("Ask me anything about Data Science and Robotics!")
if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get bot response
    response = process_user_input(user_input)

    # Add bot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Force refresh
    st.rerun()

# Quick actions section
st.markdown('<div class="sub-header">Quick Actions</div>', unsafe_allow_html=True)

# Action cards with custom styling
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>📚 Daily Tasks</h3>
            <p>Start your learning journey with today's tasks</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Start Learning", key="tasks_btn"):
        st.switch_page("pages/2_Daily_Tasks.py")

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>📝 Knowledge Check</h3>
            <p>Test your understanding with interactive quizzes</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Take Quiz", key="quiz_btn"):
        st.switch_page("pages/3_Quiz.py")

with col3:
    st.markdown(
        """
        <div class="card">
            <h3>📊 Learning Path</h3>
            <p>View your personalized learning roadmap</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("View Roadmap", key="roadmap_btn"):
        st.switch_page("pages/1_Roadmap.py")

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
                    time.sleep(1)  # Add delay to simulate increased response time
        else:
            display_final_result()

if __name__ == "__main__":
    main()

# Add React install option
if st.button("Install React"):
    os.system("npm install react react-dom")
    st.success("React has been installed successfully!")

# GitHub authentication setting
st.session_state.github = {
    "gitAuthentication": True
}