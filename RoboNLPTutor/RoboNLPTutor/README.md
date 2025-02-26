# AI Learning Assistant for Data Science & Robotics 🤖

## Quick Deploy Guide

1. **Fork on Replit**
   - Visit this project on Replit
   - Click "Fork" to create your own copy
   - Choose "Python" as the language

2. **Environment Setup**
   - Replit will automatically install Python 3.11
   - Required packages will be installed automatically:
     - streamlit
     - nltk
     - plotly
     - sqlalchemy
     - psycopg2-binary
     - python-dotenv

3. **Storage**
   - The application uses Streamlit's session state for data persistence
   - All user progress and achievements are stored locally
   - No database setup required

4. **Running the Application**
   - The app will automatically start and run on port 5000
   - Access via the provided Replit URL

## Project Structure

```
.
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── data/
│   ├── roadmap_data.py  # Learning roadmap data
│   └── microlearning_tips.py  # Daily learning tips
├── pages/
│   ├── 1_Roadmap.py     # Learning roadmap page
│   ├── 2_Daily_Tasks.py # Daily tasks page
│   ├── 3_Quiz.py        # Quiz page
│   ├── 4_Resources.py   # Resources page
│   ├── 5_Notes.py       # Notes page
│   └── 6_Achievements.py # Achievements page
├── utils/
│   ├── achievements.py   # Achievement system
│   ├── chatbot.py       # Chatbot functionality
│   ├── microlearning.py # Microlearning tips system
│   ├── progress.py      # Progress tracking
│   ├── quiz.py          # Quiz functionality
│   ├── roadmap.py       # Roadmap utilities
│   └── tasks.py         # Task management
└── main.py              # Main application file
```

## Features

- 📚 Interactive Learning Interface
- 🤖 AI-powered Learning Assistant
- 📊 Progress Tracking
- 📝 Knowledge Quizzes
- 📋 Daily Tasks Management
- 📓 Personal Learning Notes
- 🛣️ Customized Learning Roadmap
- 🏆 Emoji-Based Achievement Badges
- 💡 Daily Microlearning Tips

## Configuration

1. **Streamlit Config** (`.streamlit/config.toml`):
   ```toml
   [server]
   headless = true
   address = "0.0.0.0"
   port = 5000
   ```

## Achievement System

The application features an engaging achievement system:
- Unlock badges for completing learning milestones
- Track progress with emoji-based visual rewards
- View all achievements in a dedicated dashboard
- Receive notifications for new unlocks

## Microlearning Tips

Daily tips enhance the learning experience:
- Receive contextual programming tips
- Access code examples and best practices
- Follow resource links for deeper learning
- Tips categorized by topic (Python, Data Science, Robotics)

## Usage

1. **Main Dashboard**
   - View overall progress
   - Access the AI learning assistant
   - See daily learning tips
   - Track achievements
   - Navigate to different sections

2. **Learning Roadmap**
   - Follow structured learning path
   - Track progress by topic
   - Mark completed tasks
   - Unlock achievements

3. **Daily Tasks**
   - Get personalized daily tasks
   - Track task completion
   - Access learning resources
   - Earn completion badges

4. **Knowledge Quizzes**
   - Test understanding
   - Track quiz scores
   - Get immediate feedback
   - Unlock quiz achievements

5. **Learning Resources**
   - Access curated resources
   - Find helpful tools
   - Get guided learning materials
   - Follow tip recommendations

6. **Personal Notes**
   - Take and organize notes
   - Categorize learning materials
   - Track learning journey
   - Earn note-taking badges

7. **Achievements Dashboard**
   - View all available badges
   - Track unlocked achievements
   - See progress statistics
   - Get completion rewards

## Development Notes

- The application uses Streamlit for the user interface
- NLTK is used for natural language processing in the chatbot
- Plotly creates interactive visualizations
- Achievement system uses emoji-based rewards
- Local storage through Streamlit's session state
- Microlearning tips provide bite-sized knowledge

## Requirements

- Python 3.11+
- Required Python packages (installed automatically):
  - streamlit
  - nltk
  - plotly
  - python-dotenv