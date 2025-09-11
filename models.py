import sqlite3
from dataclasses import dataclass

@dataclass
class Column:
    id: int
    name: str


class Database:
    def __init__(self, db_name="kanban.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS columns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """)
            #self.conn.execute("""
            #    CREATE TABLE IF NOT EXISTS tasks (
            #        id INTEGER PRIMARY KEY AUTOINCREMENT,
            #        title TEXT NOT NULL,
            #        description TEXT,
            #        column_id INTEGER,
            #        FOREIGN KEY(column_id) REFERENCES columns(id)
            #    )
            #"""
            #)

    def get_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM columns")
        data = cursor.fetchall()
        return [Column(id=row[0], name=row[1]) for row in data]

    def add_column(self, name):
        with self.conn:
            self.conn.execute("INSERT INTO columns (name) VALUES (?)", (name,))

    
    def delete_column(self, column_id):
        with self.conn:
            self.conn.execute("DELETE FROM columns WHERE id = ?", (column_id,))

    #def add_task(self, title, description, column_id):
    #    with self.conn:
    #        self.conn.execute(
    #            "INSERT INTO tasks (title, description, column_id) VALUES (?, ?, ?)",
    #            (title, description, column_id)
    #        )
#
    #def get_tasks(self, column_id):
    #    cursor = self.conn.cursor()
    #    cursor.execute("SELECT * FROM tasks WHERE column_id = ?", (column_id,))
    #    return cursor.fetchall()
#
    #def move_task(self, task_id, new_column_id):
    #    with self.conn:
    #        self.conn.execute(
    #            "UPDATE tasks SET column_id = ? WHERE id = ?",
    #            (new_column_id, task_id)
    #        )
#
    #def delete_task(self, task_id):
    #    with self.conn:
    #        self.conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))