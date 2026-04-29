import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the Base metadata and service functions from the project
from src.database.session import Base
from src.api.services import create_query, get_queries, delete_query

@pytest.fixture(scope="function")
def db():
    """Provide an isolated in‑memory SQLite session for each test.

    The fixture creates the tables defined in ``Base`` (which includes
    ``QueryRecord``), yields a SQLAlchemy session, and then closes it.
    """
    test_engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(test_engine)
    TestSession = sessionmaker(bind=test_engine)
    session = TestSession()
    yield session
    session.close()

def test_crud(db):
    # Create
    rec = create_query(db, "Q1", "A1")
    assert rec.id is not None

    # Read
    rows = get_queries(db)
    assert len(rows) == 1
    assert rows[0].question == "Q1"

    # Delete
    assert delete_query(db, rec.id) is True
    assert get_queries(db) == []
