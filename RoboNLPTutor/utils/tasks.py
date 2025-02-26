from datetime import datetime, timedelta
import random
from data.roadmap_data import ROADMAP_DATA

def generate_daily_tasks(user_level, completed_tasks):
    """Generate daily tasks based on user's current level"""
    available_tasks = []
    
    # Get tasks from current level
    for stage in ROADMAP_DATA:
        if stage['level'] == user_level:
            for task in stage['tasks']:
                if task['id'] not in completed_tasks:
                    available_tasks.append(task)
    
    # Select 3 random tasks for the day
    daily_tasks = random.sample(available_tasks, min(3, len(available_tasks)))
    return daily_tasks

def mark_task_complete(task_id, completed_tasks):
    """Mark a task as complete"""
    if task_id not in completed_tasks:
        completed_tasks.append(task_id)
    return completed_tasks

def get_task_details(task_id):
    """Get details for a specific task"""
    for stage in ROADMAP_DATA:
        for task in stage['tasks']:
            if task['id'] == task_id:
                return task
    return None
