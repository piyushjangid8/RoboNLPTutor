from datetime import datetime

def load_user_progress():
    """Load user progress from session state"""
    return {
        "completed": 0,
        "current_level": "Beginner",
        "completed_tasks": [],
        "quiz_scores": [],
        "notes": [],
        "last_active": datetime.now().strftime("%Y-%m-%d")
    }

def update_progress(completed_tasks, quiz_scores):
    """Update user progress"""
    # Calculate overall progress
    total_tasks = 100  # Example total
    completed_percentage = (len(completed_tasks) / total_tasks) * 100

    # Determine level based on progress
    current_level = "Beginner"
    if completed_percentage >= 75:
        current_level = "Advanced"
    elif completed_percentage >= 50:
        current_level = "Intermediate"

    return {
        "completed": completed_percentage,
        "current_level": current_level,
        "completed_tasks": completed_tasks,
        "quiz_scores": quiz_scores,
        "last_active": datetime.now().strftime("%Y-%m-%d")
    }