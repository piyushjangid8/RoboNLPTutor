import random

def generate_quiz(topic):
    """Generate a quiz based on the topic"""
    quizzes = {
        "python": [
            {
                "question": "What is Python?",
                "options": [
                    "A programming language",
                    "A snake",
                    "A database",
                    "A web browser"
                ],
                "correct": 0
            },
            # Add more questions
        ],
        "data_science": [
            {
                "question": "What is Machine Learning?",
                "options": [
                    "A subset of artificial intelligence",
                    "A database management system",
                    "A programming language",
                    "A web framework"
                ],
                "correct": 0
            },
            # Add more questions
        ],
        "robotics": [
            {
                "question": "What is ROS?",
                "options": [
                    "Robot Operating System",
                    "Remote Operation System",
                    "Robotic Object System",
                    "Random Optimization System"
                ],
                "correct": 0
            },
            # Add more questions
        ]
    }
    
    return random.sample(quizzes.get(topic, []), min(5, len(quizzes.get(topic, []))))

def evaluate_quiz(answers, correct_answers):
    """Evaluate quiz answers and return score"""
    score = 0
    for user_answer, correct_answer in zip(answers, correct_answers):
        if user_answer == correct_answer:
            score += 1
    return (score / len(correct_answers)) * 100
