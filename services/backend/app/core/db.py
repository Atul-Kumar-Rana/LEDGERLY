from sqlmodel import create_engine, Session
from app.core.config import settings

engine = create_engine(str(settings.DATABASE_URI))

def get_session():
    with Session(engine) as session:
        yield session