from app.db.session import engine

def test_connection():
    with engine.connect() as conn:
        print("Database connected successfully!")

test_connection()
