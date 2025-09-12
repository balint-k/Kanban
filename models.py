import sqlite3
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str
    column_id: int

@dataclass
class Column:
    id: int
    name: str
    tasks: list


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
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    column_id INTEGER,
                    FOREIGN KEY(column_id) REFERENCES columns(id)
                )
            """
            )

    def get_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM columns")
        columns = cursor.fetchall()
        cursor.execute("SELECT * FROM tasks")
        task = cursor.fetchall()
        columns = [
            Column(
                id=row[0], 
                name=row[1], 
                tasks = [
                    Task(
                        id=taskRow[0], 
                        title=taskRow[1], 
                        description=taskRow[2], 
                        column_id=taskRow[3])
                        for taskRow in task if taskRow[3] == row[0]
                    ]
                   ) for row in columns
                ]
        return columns

    def add_column(self, name: str):
        with self.conn:
            self.conn.execute("INSERT INTO columns (name) VALUES (?)", (name,))

    
    def delete_column(self, column_id: int):
        with self.conn:
            self.conn.execute("DELETE FROM columns WHERE id = ?", (column_id,))
            self.conn.execute("DELETE FROM tasks WHERE column_id = ?", (column_id,))

    def add_task(self, title:str, description:str, column_id:int):
        with self.conn:
            self.conn.execute(
                "INSERT INTO tasks (title, description, column_id) VALUES (?, ?, ?)",
                (title, description, column_id)
            )

    def get_tasks(self, column_id:int):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE column_id = ?", (column_id,))
        return cursor.fetchall()
    
    def move_task(self, task_id, new_column_id:int):
        with self.conn:
            self.conn.execute(
                "UPDATE tasks SET column_id = ? WHERE id = ?",
                (new_column_id, task_id)
            )

    def delete_task(self, task_id:int ):
        with self.conn:
            self.conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))