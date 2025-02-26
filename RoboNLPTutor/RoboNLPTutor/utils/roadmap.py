from data.roadmap_data import ROADMAP_DATA

def get_roadmap_stages():
    """Return the complete roadmap stages"""
    return ROADMAP_DATA

def get_stage_details(stage_id):
    """Get details for a specific roadmap stage"""
    for stage in ROADMAP_DATA:
        if stage['id'] == stage_id:
            return stage
    return None

def calculate_stage_progress(stage_id, completed_tasks):
    """Calculate progress for a specific stage"""
    stage = get_stage_details(stage_id)
    if not stage:
        return 0
    
    total_tasks = len(stage['tasks'])
    completed = sum(1 for task in stage['tasks'] if task['id'] in completed_tasks)
    return (completed / total_tasks) * 100
