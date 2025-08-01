# ----------------------------------------
# Task Model & Feature Logic
# Author: Alimate and Zali
# Description:
# Represents a single task object and operations related to it.
# Handles creation, editing, deletion, and reminders (to be implemented).
# ----------------------------------------

import time
from datetime import datetime

# NOTE: GUI should not be imported here ideally (breaks separation of concerns)
from GUI.gui_main import new_task_add  


class Task:
    # Static field to keep creation time consistent for all instances (at class-level)
    current_date_time = datetime.today().ctime()

    def __init__(self, title, desctiption, priority, date, state, create_at):
        self.title = title
        self.description = desctiption
        self.priority = priority
        self.date = date
        self.state = state
        self.create_at = create_at

    def __repr__(self):
        """
        String representation of a Task instance.
        Useful for debugging/logging.
        """
        return f"Task({self.title}, {self.description}, {self.priority}, {self.date}, {self.state}, {self.create_at})"

    def Add_Task(self):
        """
        Create the structure of the task and return it as a dictionary.
        This is what gets stored in the backend (Redis).
        """
        data_structure = {
            "Title": f"{self.title}",
            "Desc": f"{self.description}",
            "Priority": f"{self.priority}",
            "Date": f"{self.date}",
            "state": f"{self.state}",
            "Create at": f"{self.current_date_time}",
        }
        return data_structure

    def Remove_Task(self):
        """
        TODO[Alimate]: Implement logic to remove task from Redis
        """
        pass

    def Edit_Task(self):
        """
        TODO[Alimate]: Implement logic to update task fields
        Possibly requires fetching by ID and re-saving
        """
        pass

    def Reminders(self):
        """
        NOTE: Might be moved to a separate Reminder class/module.
        Purpose: handle notifications, alerts, or scheduled triggers
        """
        pass

    def get_list_of_task(self):
        """
        Fetch all tasks from backend using Redis handler
        NOTE: Import done inside method to avoid circular dependency
        """
        from backend.server import fetch_tasks
        fetch_tasks()
