from sqlite_bd import SQLiteDB

class TaskList:
    def __init__(self, db_name):
        self.db = SQLiteDB(db_name)
        self.db.create_table()

    def add_task(self, description):
        self.db.insert_task(description)

    def get_all_tasks(self):
        return self.db.get_all_tasks()

    def complete_task(self, task_id):
        self.db.complete_task(task_id)

    def delete_task(self, task_id):
        self.db.delete_task(task_id)
