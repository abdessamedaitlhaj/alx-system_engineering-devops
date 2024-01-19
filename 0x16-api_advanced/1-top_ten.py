#!/usr/bin/python3
"""
Returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Return top 10 new post for a given subreddit"""
    if not subreddit or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=10"
    headers = {"User-Agent": "GetTenNewPosts/1.0 by /u/abdessamed"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for p in posts:
            print(p["data"]["title"])
    else:
        print(None)
