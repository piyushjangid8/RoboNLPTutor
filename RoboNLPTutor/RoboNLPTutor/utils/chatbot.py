import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from data.roadmap_data import ROADMAP_DATA

def initialize_chatbot():
    """Initialize the chatbot with required NLTK downloads"""
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')

def process_user_input(user_input):
    """Process user input and return appropriate response"""
    # Convert to lowercase for processing
    user_input = user_input.lower()
    
    # Basic keyword matching
    if any(word in user_input for word in ['hello', 'hi', 'hey']):
        return "Hello! I'm your AI learning assistant. How can I help you today?"
    
    if 'roadmap' in user_input:
        return "I can help you with the Data Science and Robotics roadmap. The learning path starts with Python basics, then moves to data analysis, machine learning, and finally robotics-specific topics. Would you like to see the detailed roadmap?"
    
    if 'task' in user_input:
        return "I can help you manage your daily learning tasks. Would you like to see today's tasks or create new ones?"
    
    if 'quiz' in user_input:
        return "Ready to test your knowledge? I can provide quizzes on various topics in Data Science and Robotics. Would you like to start a quiz?"
    
    if 'progress' in user_input:
        return "I can show you your learning progress and help you track your achievements. Would you like to see your progress dashboard?"
    
    # Default response
    return "I'm here to help you learn Data Science and Robotics. You can ask me about the roadmap, daily tasks, take quizzes, or check your progress."
