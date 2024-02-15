import sqlite3

class SQLiteDB:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                description TEXT NOT NULL,
                completed INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    def insert_task(self, description, completed=False):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (description, completed) VALUES (?, ?)
        ''', (description, 1 if completed else 0))
        conn.commit()
        conn.close()

    def get_all_tasks(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM tasks
        ''')
        tasks = cursor.fetchall()
        conn.close()
        return tasks

    def complete_task(self, task_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE tasks SET completed = 1 WHERE id = ?
        ''', (task_id,))
        conn.commit()
        conn.close()

    def delete_task(self, task_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM tasks WHERE id = ?
        ''', (task_id,))
        conn.commit()
        conn.close()
