import streamlit as st
from utils.roadmap import get_roadmap_stages, calculate_stage_progress
import plotly.express as px
from utils.database_ops import get_user_progress, get_session

st.set_page_config(
    page_title="Learning Roadmap",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        max-width: 100%;
        padding: 1rem 2rem;
    }
    .roadmap-header {
        font-size: 2.2rem;
        color: #1E88E5;
        margin: 1rem 0 2rem 0;
        padding: 0.5rem;
        line-height: 1.4;
        word-wrap: break-word;
    }
    .stage-card {
        border-radius: 10px;
        background-color: white;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stage-title {
        color: #1E88E5;
        font-size: 1.5rem;
        margin: 0.5rem 0;
        padding: 0.5rem;
        line-height: 1.4;
    }
    .stage-description {
        color: #424242;
        font-size: 1.1rem;
        margin: 0.5rem 0;
        padding: 0.5rem;
    }
    .task-container {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .task-title {
        font-weight: bold;
        color: #1565C0;
        padding: 0.5rem 0;
    }
    .progress-bar {
        height: 10px;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .level-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.9rem;
        margin-left: 1rem;
    }
    .level-beginner {
        background-color: #E3F2FD;
        color: #1565C0;
    }
    .level-intermediate {
        background-color: #E8F5E9;
        color: #2E7D32;
    }
    .level-advanced {
        background-color: #FFF3E0;
        color: #E65100;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state if needed
if 'db_session' not in st.session_state:
    st.session_state.db_session = get_session()
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = get_user_progress(st.session_state.db_session, 1)  # Default user ID 1

st.markdown('<h1 class="roadmap-header">📊 Learning Roadmap</h1>', unsafe_allow_html=True)

# Get roadmap data
roadmap_stages = get_roadmap_stages()

# Display roadmap
for stage in roadmap_stages:
    level_class = f"level-{stage['level'].lower()}"

    st.markdown(f"""
    <div class="stage-card">
        <div class="stage-title">
            {stage['title']}
            <span class="level-badge {level_class}">{stage['level']}</span>
        </div>
        <div class="stage-description">{stage['description']}</div>
    """, unsafe_allow_html=True)

    # Progress bar for stage
    progress = calculate_stage_progress(
        stage['id'], 
        st.session_state.user_progress.get('completed_tasks', [])
    )
    st.progress(progress / 100)
    st.markdown(f"**Progress:** {progress:.1f}%")

    # Tasks in this stage
    st.markdown("### Tasks")
    for task in stage['tasks']:
        task_completed = task['id'] in st.session_state.user_progress.get('completed_tasks', [])

        with st.container():
            st.markdown(f"""
            <div class="task-container">
                <div class="task-title">
                    {'✅' if task_completed else '⭕'} {task['title']}
                </div>
                <p>{task['description']}</p>
            </div>
            """, unsafe_allow_html=True)

            # Resources
            with st.expander("📚 Resources"):
                for resource in task['resources']:
                    st.markdown(f"- {resource}")

            if not task_completed:
                if st.button("Mark Complete", key=f"complete_{task['id']}"):
                    if 'completed_tasks' not in st.session_state.user_progress:
                        st.session_state.user_progress['completed_tasks'] = []
                    st.session_state.user_progress['completed_tasks'].append(task['id'])
                    st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# Add a motivational message at the bottom
st.markdown("""
<div style="text-align: center; margin-top: 2rem; padding: 1rem; background-color: #E3F2FD; border-radius: 10px;">
    <h3 style="color: #1565C0;">Keep Going! 🚀</h3>
    <p>Every step forward is progress towards your goal!</p>
</div>
""", unsafe_allow_html=True)