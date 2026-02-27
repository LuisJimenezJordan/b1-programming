import sqlite3

class UserStore:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    
    def load(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        conn.close()
        
        return [{"id": row[0], "name": row[1], "email": row[2]} for row in rows]
    
    def save(self, users):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for user in users:
            if "id" in user:
                cursor.execute(
                    "UPDATE users SET name = ?, email = ? WHERE id = ?",
                    (user["name"], user["email"], user["id"])
                )
            else:
                cursor.execute(
                    "INSERT INTO users (name, email) VALUES (?, ?)",
                    (user["name"], user["email"])
                )
        
        conn.commit()
        conn.close()
    
    def find_by_id(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {"id": row[0], "name": row[1], "email": row[2]}
        return None
    
    def create_user(self, name, email):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return {"id": user_id, "name": name, "email": email}
    
    def update_user(self, user_id, updated_data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (updated_data["name"], updated_data["email"], user_id)
        )
        rows_affected = cursor.rowcount
        conn.commit()
        conn.close()
        
        return rows_affected > 0
    
    def delete_user(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        rows_affected = cursor.rowcount
        conn.commit()
        conn.close()
        
        return rows_affected > 0