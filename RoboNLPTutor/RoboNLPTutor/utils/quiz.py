import random

def get_quiz(topic):
    """Generate a quiz based on the topic with properly formatted questions."""
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
                "correct": "A programming language",
                "explanation": "Python is a high-level, interpreted programming language known for its simplicity and readability."
            },
            {
                "question": "Which of the following is a Python data type?",
                "options": [
                    "List",
                    "Array",
                    "Stack",
                    "Queue"
                ],
                "correct": "List",
                "explanation": "List is a built-in data type in Python used to store collections of items."
            },
            # Add more questions here
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
                "correct": "A subset of artificial intelligence",
                "explanation": "Machine Learning is a subset of AI that involves training algorithms to learn patterns from data."
            },
            {
                "question": "Which library is commonly used for data manipulation in Python?",
                "options": [
                    "Pandas",
                    "NumPy",
                    "SciPy",
                    "Matplotlib"
                ],
                "correct": "Pandas",
                "explanation": "Pandas is a powerful library for data manipulation and analysis in Python."
            },
            # Add more questions here
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
                "correct": "Robot Operating System",
                "explanation": "ROS stands for Robot Operating System, which is a flexible framework for writing robot software."
            },
            {
                "question": "Which sensor is commonly used for obstacle detection in robots?",
                "options": [
                    "Ultrasonic sensor",
                    "Temperature sensor",
                    "Pressure sensor",
                    "Humidity sensor"
                ],
                "correct": "Ultrasonic sensor",
                "explanation": "Ultrasonic sensors are commonly used in robots for obstacle detection and distance measurement."
            },
            # Add more questions here
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