#!/usr/bin/python3
"""Retrieve to do list of a given employee"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = json.loads(requests.get(url + "users/" + user_id).text)
    todolist = json.loads(requests.get(url + "todos/").text)

    count = 0
    t_tasks = 0
    for task in todolist:
        if task.get("completed") and task.get("userId") == user.get("id"):
            count += 1
        if task.get("userId") == user.get("id"):
            t_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), count, t_tasks))
    for task in todolist:
        if task.get("completed") and task.get("userId") == user.get("id"):
            print(f"\t {task.get('title')}")
