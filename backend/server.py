# ----------------------------------------
# Redis Backend Handler
# Author: Alimate
# Description:
# This module handles all backend operations with Redis,
# including storing and fetching tasks.
# ----------------------------------------

import redis
from datetime import datetime
from time import sleep
from Features.feature import Task

# ⚠️ Redis connection
# Make sure Redis server is running on localhost:6379
R = redis.Redis(host="localhost", port=6379, decode_responses=True)


# 🧠 Fetch and print all saved tasks from Redis
def fetch_tasks():
    print("Fetching tasks ...")
    sleep(2)  # simulating delay (for debugging or UX effect)

    # Get all task IDs stored in Redis list
    task_ids = R.lrange("tasks_id", 0, -1)
    print(task_ids)

    # Loop through each task ID and retrieve full task data
    for tid in task_ids:
        task = R.hgetall(f"task:{tid}")
        print(f"Task ID : {tid}")
        print(f"Title : {task.get('Title')}")
        print(f"Desc : {task.get('Desc')}")
        print(f"Date : {task.get('Date')}")
        print(f"Create at : {task.get('create at')}")
        print("--------------------------------------------------")


# 🟢 Save new task data into Redis
def set_connection(task_data: dict):
    # Generate a unique incremental ID for the new task
    id_session = R.incr("task:id")

    print("processing ...")
    sleep(2)

    try:
        # Save task details as a hash (dictionary-like structure)
        R.hset(f"task:{id_session}", mapping=task_data)
        print("Task added Successfully.")
    except Exception as err:
        print(f"Error is : {err}")
    finally:
        print("done")

    # Push task ID into list to keep track of all tasks
    R.rpush("tasks_id", id_session)
