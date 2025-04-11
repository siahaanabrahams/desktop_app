from sqlalchemy import create_engine, text
DB_URL = "postgresql+pg8000://postgres:abraham@localhost:5432/postgres"
engine = create_engine(DB_URL) 

def create_new_user(username, password, role) :
    with engine.connect() as conn : 
        query = text("""
            INSERT INTO user_admin (username, password, role)
            VALUES (:username, :password, :role)
        """)
        conn.execute(query, {'username' : username, 'password' : password, 'role' : role})
        conn.commit()

def check_username (username) :
    with engine.connect() as conn : 
        query = text("""
            select username
            from user_admin
            where username = :username
        """)    
        result = conn.execute(query, {'username' : username}).fetchone() 
    if result is not None : 
        return True
    else : False

def find_username(username) :
    with engine.connect() as conn : 
        query = text("""
            SELECT username
            FROM user_admin
            WHERE username ILIKE :username
            AND role != 'admin'
        """) 
        result = conn.execute(query, {'username': f"%{username}%"}).fetchall()
    if result :
        return result
    else : 
        return None 