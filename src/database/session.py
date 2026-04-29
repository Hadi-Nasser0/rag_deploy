import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()


# Replace credentials with yours
DATABASE_URL = os.getenv('DATABASE_URL',"postgresql+psycopg2://rag_role:mypassword@localhost/rag_db")

# engine creation
engine = create_engine(DATABASE_URL)

# session class config
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base class for ORM models
Base = declarative_base()

