# ------------------------------
# Project Main file
# Author: Alimate and Zali and Jaber
# Description:
# Main entry point of the TODO app.
# Coordinates the GUI, feature logic, and backend Redis database.
# ------------------------------

from backend.server import fetch_tasks, set_connection
from GUI.gui_main import new_task_add, root, show_all_tasks
from Features.feature import Task


# This function is triggered when the "Add Task" button is clicked from the GUI
# It receives a dictionary of task data from the form, creates a Task object,
# and sends it to Redis for storage.
def on_add_task(data_form_gui):
    task = Task(
        title=data_form_gui['Title'],
        desctiption=data_form_gui['Description'],
        priority=data_form_gui['Priority'],
        date=data_form_gui['Date'],
        state='Pending',
        create_at=Task.current_date_time
    )

    # Generate dictionary structure of the task (ready to be saved)
    task_struct_dict = task.Add_Task()
    print('Task Created:', task_struct_dict)

    # Save to Redis
    set_connection(task_struct_dict)


# ------------------------------
# App initialization
# ------------------------------

# Setup GUI components and pass the logic handler (callback)
new_task_add(root, on_add_callback=on_add_task)

# Optional - render all existing tasks in the UI (if needed)
show_all_tasks(root)

# Start the main event loop of the GUI
root.mainloop()
