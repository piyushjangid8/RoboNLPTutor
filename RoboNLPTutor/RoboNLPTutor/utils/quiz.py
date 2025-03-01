import random

def generate_quizzes():
    """Generate a large set of quizzes dynamically for each topic."""
    quizzes = {
        "python": [],
        "data_science": [],
        "robotics": []
    }
    
    for i in range(1, 334):  # Approx. 333 questions per topic
        quizzes["python"].append({
            "question": f"Python Question {i}",
            "options": [f"Option {j}" for j in range(1, 5)],
            "correct": random.randint(0, 3)
        })
        
        quizzes["data_science"].append({
            "question": f"Data Science Question {i}",
            "options": [f"Option {j}" for j in range(1, 5)],
            "correct": random.randint(0, 3)
        })
        
        quizzes["robotics"].append({
            "question": f"Robotics Question {i}",
            "options": [f"Option {j}" for j in range(1, 5)],
            "correct": random.randint(0, 3)
        })
    
    return quizzes

def get_quiz(topic):
    """Generate a quiz based on the topic"""
    quizzes = generate_quizzes()
    
    if topic not in quizzes:
        return f"Topic '{topic}' not found. Available topics: {', '.join(quizzes.keys())}"
    
    questions = quizzes[topic]
    return random.sample(questions, min(5, len(questions)))

def evaluate_quiz(answers, correct_answers):
    """Evaluate quiz answers and return score"""
    if len(answers) != len(correct_answers):
        return "Error: Mismatch in the number of answers provided."
    
    score = sum(1 for user_answer, correct_answer in zip(answers, correct_answers) if user_answer == correct_answer)
    
    return {
        "score": score,
        "percentage": (score / len(correct_answers)) * 100
    }
