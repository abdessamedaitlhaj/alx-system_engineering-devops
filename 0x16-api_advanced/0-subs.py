#!/usr/bin/python3
"""
Returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscriber of a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    #headers = {"User-Agent": "GetSubscribers/1.0 by /u/abdessamed"}
    headers = {'User-Agent': 'android:com.example.myredditapp:v1.2.3 (by /u/kemitche)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json()
            return data["data"]["subscribers"]
        except KeyError:
            return 0
    else:
        return 0
