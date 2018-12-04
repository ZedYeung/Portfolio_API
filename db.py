from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

DB_URI = 'sqlite:///investments.db'
engine = create_engine(DB_URI)

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=engine)
session = scoped_session(Session)