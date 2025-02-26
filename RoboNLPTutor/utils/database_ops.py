from models.database import User, CompletedTask, QuizScore, Note, get_session
from datetime import datetime

def get_or_create_user(session):
    """Get the current user or create if not exists"""
    user = session.query(User).first()
    if not user:
        user = User(level="Beginner", progress=0.0)
        session.add(user)
        session.commit()
    return user

def update_user_progress(session, user_id, new_progress=None, new_level=None):
    """Update user progress and level"""
    user = session.query(User).get(user_id)
    if new_progress is not None:
        user.progress = new_progress
    if new_level is not None:
        user.level = new_level
    user.last_active = datetime.now()
    session.commit()
    return user

def add_completed_task(session, user_id, task_id):
    """Mark a task as completed"""
    completed_task = CompletedTask(user_id=user_id, task_id=task_id)
    session.add(completed_task)
    session.commit()

def add_quiz_score(session, user_id, topic, score):
    """Add a new quiz score"""
    quiz_score = QuizScore(user_id=user_id, topic=topic, score=score)
    session.add(quiz_score)
    session.commit()

def add_note(session, user_id, title, content, category):
    """Add a new note"""
    note = Note(user_id=user_id, title=title, content=content, category=category)
    session.add(note)
    session.commit()

def get_user_progress(session, user_id):
    """Get complete user progress data"""
    user = session.query(User).get(user_id)
    completed_tasks = [task.task_id for task in user.completed_tasks]
    quiz_scores = [{"topic": score.topic, "score": score.score} for score in user.quiz_scores]
    
    return {
        "completed": user.progress,
        "current_level": user.level,
        "completed_tasks": completed_tasks,
        "quiz_scores": quiz_scores,
        "last_active": user.last_active.strftime("%Y-%m-%d")
    }
