from datetime import datetime

# Achievement definitions with their emoji badges and criteria
ACHIEVEMENTS = {
    "first_login": {
        "title": "First Steps! 👣",
        "description": "Started your learning journey",
        "emoji": "👣",
        "category": "general"
    },
    "quiz_master": {
        "title": "Quiz Master 🎯",
        "description": "Score 100% in any quiz",
        "emoji": "🎯",
        "category": "quiz"
    },
    "note_taker": {
        "title": "Note Keeper 📝",
        "description": "Created your first note",
        "emoji": "📝",
        "category": "notes"
    },
    "task_completer": {
        "title": "Task Champion 🌟",
        "description": "Complete 5 tasks",
        "emoji": "🌟",
        "category": "tasks"
    },
    "roadmap_explorer": {
        "title": "Path Explorer 🗺️",
        "description": "View the complete roadmap",
        "emoji": "🗺️",
        "category": "roadmap"
    },
    "quick_learner": {
        "title": "Quick Learner 🚀",
        "description": "Complete 3 tasks in one day",
        "emoji": "🚀",
        "category": "tasks"
    }
}

def check_achievements(user_progress):
    """Check and award new achievements based on user progress"""
    if 'achievements' not in user_progress:
        user_progress['achievements'] = []

    new_achievements = []
    existing_achievements = [a['id'] for a in user_progress['achievements']]

    # Check each achievement
    if "first_login" not in existing_achievements:
        new_achievements.append(award_achievement("first_login"))

    if (any(score['score'] == 100 for score in user_progress.get('quiz_scores', [])) 
        and "quiz_master" not in existing_achievements):
        new_achievements.append(award_achievement("quiz_master"))

    if user_progress.get('notes', []) and "note_taker" not in existing_achievements:
        new_achievements.append(award_achievement("note_taker"))

    if (len(user_progress.get('completed_tasks', [])) >= 5 
        and "task_completer" not in existing_achievements):
        new_achievements.append(award_achievement("task_completer"))

    # Add new achievements to user progress
    user_progress['achievements'].extend(new_achievements)
    return new_achievements

def award_achievement(achievement_id):
    """Create a new achievement award"""
    achievement = ACHIEVEMENTS[achievement_id].copy()
    achievement['id'] = achievement_id
    achievement['awarded_at'] = datetime.now().strftime("%Y-%m-%d %H:%M")
    return achievement

def get_achievement_stats(user_progress):
    """Get achievement statistics"""
    achievements = user_progress.get('achievements', [])
    total_available = len(ACHIEVEMENTS)
    total_earned = len(achievements)
    return {
        'total_available': total_available,
        'total_earned': total_earned,
        'percent_complete': (total_earned / total_available) * 100 if total_available > 0 else 0
    }
