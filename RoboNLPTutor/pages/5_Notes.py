import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Notes", page_icon="📝")

# Initialize session state if needed
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = {
        "completed": 0,
        "current_level": "Beginner",
        "completed_tasks": [],
        "quiz_scores": [],
        "notes": []
    }

st.title("📝 Learning Notes")

# Note taking form
with st.form("note_form"):
    note_title = st.text_input("Note Title")
    note_content = st.text_area("Note Content")
    note_category = st.selectbox(
        "Category",
        ["Python", "Data Science", "Robotics", "General"]
    )

    submitted = st.form_submit_button("Save Note")

    if submitted and note_title and note_content:
        # Add note to session state
        if 'notes' not in st.session_state.user_progress:
            st.session_state.user_progress['notes'] = []

        st.session_state.user_progress['notes'].append({
            'title': note_title,
            'content': note_content,
            'category': note_category,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        st.success("Note saved successfully!")

# Display notes
st.header("Your Notes")

# Filter by category
selected_category = st.selectbox(
    "Filter by category",
    ["All"] + ["Python", "Data Science", "Robotics", "General"]
)

# Display filtered notes
for note in reversed(st.session_state.user_progress.get('notes', [])):
    if selected_category == "All" or note['category'] == selected_category:
        with st.expander(f"{note['title']} - {note['created_at']}"):
            st.write(f"**Category:** {note['category']}")
            st.write(note['content'])

# Display empty state
if not st.session_state.user_progress.get('notes', []):
    st.info("No notes yet. Start taking notes to track your learning journey!")