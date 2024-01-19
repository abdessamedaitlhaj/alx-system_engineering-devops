#!/usr/bin/python3
"""
Returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscriber of a given subreddit"""
    if not subreddit:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'GetSubscribers'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get("data").get("subscribers")
        except KeyError:
            return 0
    else:
        return 0
