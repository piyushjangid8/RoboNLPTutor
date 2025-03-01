from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from datetime import datetime
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Get database URL
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
     # Fallback for development - SQLite
    logger.warning("DATABASE_URL not found, using SQLite database")
    DATABASE_URL = 'sqlite:///app.db'

logger.info(f"Connecting to database: {DATABASE_URL}")

# Create database engine
engine = create_engine(DATABASE_URL)

# Create all tables if they don't exist
try:
    logger.info("Checking if database tables exist...")
    from sqlalchemy import inspect
    inspector = inspect(engine)
    if not inspector.has_table('users'):
        logger.info("Tables don't exist. Creating database tables...")
        Base.metadata.create_all(engine)
        logger.info("Database tables created successfully")
except Exception as e:
    logger.error(f"Error checking/creating database tables: {str(e)}")

# Create declarative base
Base = declarative_base()

def init_db():
    """Initialize the database by creating all tables"""
    Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    level = Column(String)
    progress = Column(Float, default=0.0)
    last_active = Column(DateTime, default=datetime.now)

    # Relationships
    completed_tasks = relationship("CompletedTask", back_populates="user")
    quiz_scores = relationship("QuizScore", back_populates="user")
    notes = relationship("Note", back_populates="user")

class CompletedTask(Base):
    __tablename__ = 'completed_tasks'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    task_id = Column(String)
    completed_at = Column(DateTime, default=datetime.now)

    # Relationship
    user = relationship("User", back_populates="completed_tasks")

class QuizScore(Base):
    __tablename__ = 'quiz_scores'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    topic = Column(String)
    score = Column(Float)
    taken_at = Column(DateTime, default=datetime.now)

    # Relationship
    user = relationship("User", back_populates="quiz_scores")

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    content = Column(Text)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    # Relationship
    user = relationship("User", back_populates="notes")

def init_db():
    """Initialize the database tables"""
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")
        raise

def get_session():
    """Get a new database session"""
    try:
        session = Session()
        session.execute(text("SELECT 1"))  # Test the connection using SQLAlchemy text()
        return session
    except Exception as e:
        logger.error(f"Error creating database session: {str(e)}")
        raise