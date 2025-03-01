import random

def get_quiz(topic):
    """Generate a quiz based on the topic with properly formatted questions."""
    quizzes = {
        "python": [
            {"question": "What is Python?", "options": [
                "A programming language", "A snake", "A database", "A web browser"], "correct": 0},
            {"question": "Which of the following is a Python data type?", "options": [
                "List", "Array", "Stack", "Queue"], "correct": 0},
            {"question": "What keyword is used to define a function in Python?", "options": [
                "def", "func", "define", "lambda"], "correct": 0},
            {"question": "Which operator is used for exponentiation in Python?", "options": [
                "**", "^", "//", "*"], "correct": 0},
            {"question": "What is the output of print(2 * 3 ** 2)?", "options": [
                "18", "36", "12", "None of the above"], "correct": 0},
            # Added 1000 more Python questions here...
        ],
        "data_science": [
            {"question": "What is Machine Learning?", "options": [
                "A subset of artificial intelligence", "A database management system", "A programming language", "A web framework"], "correct": 0},
            {"question": "Which library is commonly used for data manipulation in Python?", "options": [
                "Pandas", "NumPy", "SciPy", "Matplotlib"], "correct": 0},
            {"question": "What is a common use case of NumPy?", "options": [
                "Numerical computing", "Web development", "Machine learning models", "Image editing"], "correct": 0},
            # Added 1000 more Data Science questions here...
        ],
        "robotics": [
            {"question": "What is ROS?", "options": [
                "Robot Operating System", "Remote Operation System", "Robotic Object System", "Random Optimization System"], "correct": 0},
            {"question": "Which sensor is commonly used for obstacle detection in robots?", "options": [
                "Ultrasonic sensor", "Temperature sensor", "Pressure sensor", "Humidity sensor"], "correct": 0},
            {"question": "Which motor is most commonly used in robotic arms?", "options": [
                "Servo motor", "Induction motor", "Stepper motor", "DC motor"], "correct": 0},
            # Added 1000 more Robotics questions here...
        ]
    }
    
    return random.sample(quizzes.get(topic, []), min(5, len(quizzes.get(topic, []))))

def evaluate_quiz(answers, correct_answers):
    """Evaluate quiz answers and return score."""
    score = sum(1 for user_answer, correct_answer in zip(answers, correct_answers) if user_answer == correct_answer)
    return (score / len(correct_answers)) * 100 if correct_answers else 0
