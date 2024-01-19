#!/usr/bin/python3
"""
Returns a list containing the titles of all hot articles
for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return top 10 new post for a given subreddit"""
    if not subreddit or type(subreddit) is not str:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=10"
    headers = {"User-Agent": "GetTenNewPosts/1.0 by /u/abdessamed"}
    params = {"after": after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        for p in posts:
            hot_list.append(p.get("data").get("title"))

        after = data.get("data").get("after")
        if after:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
