from sqlalchemy import create_engine, text
DB_URL = "postgresql+pg8000://postgres:abraham@localhost:5432/postgres"
engine = create_engine(DB_URL) 