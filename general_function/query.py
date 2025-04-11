from sqlalchemy import create_engine, text
DB_URL = "postgresql+pg8000://postgres:abraham@localhost:5432/postgres"
engine = create_engine(DB_URL)

def log_out_session(id_operation) :
    with engine.connect() as conn:
        query = text(
            "UPDATE operation SET end_time = NOW() WHERE id_operation = :id_operation"
        )
        conn.execute(query, {"id_operation": id_operation})
        conn.commit()