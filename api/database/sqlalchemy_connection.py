from fastapi import HTTPException
from sqlalchemy.ext.declarative import declarative_base
from api.database.session import Session


def get_session():
    """middleware"""
    session = Session()
    try:
        yield session
    # # # # https://fastapi.tiangolo.com/release-notes/#0740
    except HTTPException:
        session.rollback()
        raise
    finally:
        session.close()


Base = declarative_base()
