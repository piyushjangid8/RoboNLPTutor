import openai
import random
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_quiz(topic):
    """Generate a quiz based on the topic using OpenAI API."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a quiz with 5 questions on the topic of {topic}. Each question should have 4 options, the correct answer, an explanation for the correct answer, and explanations for the other options.",
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    quiz_data = response.choices[0].text.strip()
    quiz = parse_quiz_data(quiz_data)
    return quiz

def parse_quiz_data(quiz_data):
    """Parse the quiz data from OpenAI API response."""
    questions = quiz_data.split("\n\n")
    quiz = []
    for question in questions:
        lines = question.split("\n")
        q = {
            "question": lines[0],
            "options": [lines[1], lines[2], lines[3], lines[4]],
            "correct": lines[5],
            "explanation": lines[6],
            "other_explanations": lines[7:]
        }
        quiz.append(q)
    return quiz

def evaluate_quiz(answers, correct_answers):
    """Evaluate quiz answers and return score"""
    score = 0
    for user_answer, correct_answer in zip(answers, correct_answers):
        if user_answer == correct_answer:
            score += 1
    return (score / len(correct_answers)) * 100
