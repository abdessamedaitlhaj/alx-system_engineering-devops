#!/usr/bin/python3
"""
Returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Return top 10 new post for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "GetTenNewPosts/1.0 by /u/abdessamed"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for i in range(10):
            print(my_data["data"]["children"][i]["data"]["title"])
    else:
        return 0
