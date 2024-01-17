#!/usr/bin/python3
"""export all reacords of all employees to the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    users = json.loads(requests.get(url + "users/").text)
    todolist = json.loads(requests.get(
        url + "todos/").text)
    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as f:
        data = []
        all_employees = {}
        for user in users:
            all_employees.update({user.get("id"): [
                {
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    }
                for task in todolist
                ]})
        json.dump(all_employees, f)
