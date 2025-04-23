import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()  # Load environment variables from .env file

database_url = os.getenv("DB_URL")

engine = create_engine(database_url) 

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
    
def check_password(username, password) :
    with engine.connect() as conn :
        query = text("""
            SELECT password
            FROM user_admin
            WHERE username = :username
        """)
        password_db = conn.execute(query, {'username' : username}).fetchone()
        password_db = password_db[0] 
        if password == password_db : 
            return True
        else :
            return False
        
def change_password_que(username, newPassword) :
    with engine.connect() as conn : 
        query = text("""
            UPDATE user_admin
            SET password = :password
            WHERE username = :username;
        """)
        conn.execute(query, {'username' : username, 'password' : newPassword})
        conn.commit()