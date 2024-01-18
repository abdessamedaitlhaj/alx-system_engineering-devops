#!/usr/bin/python3
"""
Returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers"""

    if not subreddit or type(subreddit) is not str:
        return (0)
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {"User-Agent": "GetSubBot/1.0 by /u/abdessamed"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        my_data = response.json()
        return my_data["data"]["subscribers"]
    else:
        return 0
