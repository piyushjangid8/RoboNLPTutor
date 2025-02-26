import streamlit as st
from utils.achievements import get_achievement_stats, ACHIEVEMENTS

st.set_page_config(
    page_title="Achievements",
    page_icon="🏆",
    layout="wide"
)

# Custom CSS for achievements page
st.markdown("""
<style>
    .achievement-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .achievement-title {
        font-size: 1.3rem;
        color: #1E88E5;
        margin-bottom: 0.5rem;
    }
    .achievement-emoji {
        font-size: 2rem;
        margin-right: 1rem;
    }
    .achievement-locked {
        opacity: 0.5;
    }
    .achievement-stats {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #1E88E5, #1565C0);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🏆 Achievements")

# Initialize user progress if needed
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = {
        "completed": 0,
        "current_level": "Beginner",
        "completed_tasks": [],
        "quiz_scores": [],
        "notes": [],
        "achievements": []
    }

# Get achievement statistics
stats = get_achievement_stats(st.session_state.user_progress)

# Display achievement stats
st.markdown(f"""
<div class="achievement-stats">
    <h2>Achievement Progress</h2>
    <h3>{stats['total_earned']} / {stats['total_available']} Unlocked</h3>
    <div style="width: 100%; background-color: rgba(255,255,255,0.2); border-radius: 5px;">
        <div style="width: {stats['percent_complete']}%; height: 10px; background-color: white; border-radius: 5px;"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# Display achievements
earned_achievements = {a['id'] for a in st.session_state.user_progress.get('achievements', [])}

for achievement_id, achievement in ACHIEVEMENTS.items():
    is_earned = achievement_id in earned_achievements
    achievement_class = "" if is_earned else "achievement-locked"
    
    st.markdown(f"""
    <div class="achievement-card {achievement_class}">
        <div style="display: flex; align-items: center;">
            <span class="achievement-emoji">{achievement['emoji']}</span>
            <div>
                <div class="achievement-title">{achievement['title']}</div>
                <div>{achievement['description']}</div>
                <div style="color: #666; font-size: 0.9rem; margin-top: 0.5rem;">
                    {'🎉 Unlocked!' if is_earned else '🔒 Locked'}
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Add a fun message at the bottom
st.markdown("""
<div style="text-align: center; margin-top: 2rem; padding: 1rem; background-color: #E3F2FD; border-radius: 10px;">
    <h3 style="color: #1565C0;">Keep Learning! 🚀</h3>
    <p>Every achievement unlocked is a step forward in your journey!</p>
</div>
""", unsafe_allow_html=True)
