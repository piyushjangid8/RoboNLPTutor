import streamlit as st
from utils.tasks import generate_daily_tasks, mark_task_complete
from datetime import datetime
from utils.database_ops import get_session, get_user_progress, add_completed_task

st.set_page_config(page_title="Daily Tasks", page_icon="📚")

# Initialize session state if needed
if 'db_session' not in st.session_state:
    st.session_state.db_session = get_session()
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = get_user_progress(st.session_state.db_session, 1)  # Default user ID 1

st.title("📚 Daily Tasks")

# Get user's current level from session state
user_level = st.session_state.user_progress['current_level']
completed_tasks = st.session_state.user_progress.get('completed_tasks', [])

# Generate daily tasks
daily_tasks = generate_daily_tasks(user_level, completed_tasks)

st.write(f"Your tasks for {datetime.now().strftime('%Y-%m-%d')}:")

for task in daily_tasks:
    with st.container():
        col1, col2 = st.columns([0.8, 0.2])

        with col1:
            st.subheader(task['title'])
            st.write(task['description'])

            # Display resources
            st.write("📑 Resources:")
            for resource in task['resources']:
                st.write(f"- {resource}")

        with col2:
            if task['id'] not in completed_tasks:
                if st.button("Complete", key=f"complete_task_{task['id']}"):
                    completed_tasks = mark_task_complete(task['id'], completed_tasks)
                    # Update database
                    add_completed_task(st.session_state.db_session, 1, task['id'])  # Default user ID 1
                    st.session_state.user_progress['completed_tasks'] = completed_tasks
                    st.rerun()
            else:
                st.write("✅ Completed")

        st.divider()

# Display motivation
st.success("Keep going! You're making great progress! 🚀")