#!/usr/bin/python3
"""export data in the CSV format"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = json.loads(requests.get(url + "users/" + user_id).text)
    todolist = json.loads(requests.get(
        url + "users/" + user_id + "/todos/").text)

    file_name = user_id + ".csv"
    with open(file_name, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todolist:
            writer.writerow(
                [user_id, user.get("username"),
                    task.get("completed"), task.get("title")]
                    )
