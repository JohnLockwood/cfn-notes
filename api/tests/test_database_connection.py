from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.model.models import User

from app.model.database import Base
from app.core.config import Config

engine = create_engine(Config().get_connection_string(host="localhost"))

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def test_connection_good():
    assert TestingSessionLocal is not None


def test_can_create_user():

    # Delete if exists
    session = TestingSessionLocal()
    user = session.query(User).filter(User.id == '42').first()
    if user:
        session.delete(user)
    session.commit()

    # Re-create
    session = TestingSessionLocal()
    user = User()
    user.id = "42"
    user.email = 'joe@example.com'
    user.hashed_password = "GohashYourself"
    user.is_active = True
    session.add(user)
    session.commit()
