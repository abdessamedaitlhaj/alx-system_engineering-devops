#!/usr/bin/python3
"""export data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/" + user_id).json()
    todolist = requests.get(f"{url}todos", params={"userId": user_id}).json()

    file_name = user_id + ".JSON"
    with open(file_name, mode='w') as f:
        data = [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get("username")
                    }
                for task in todolist
                ]
        json.dump({user_id: data}, f)
