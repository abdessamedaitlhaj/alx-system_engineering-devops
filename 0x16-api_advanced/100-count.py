#!/usr/bin/python3
"""
Prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, count_keys=None, after=None):
    """Prints a sorted count of given keywords"""
    if not subreddit or type(subreddit) is not str:
        return 0

    if not count_keys:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=10"
    headers = {"User-Agent": "GetTenNewPosts/1.0 by /u/abdessamed"}
    params = {"after": after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        for p in posts:
            t = p.get("data").get("title").lower()

            for w in word_list:
                if w.lower() in t:
                    count_keys[w] = count_keys.get(w, 0) + 1

        after = data.get("data").get("after")
        if after:
            recurse(subreddit, word_list, count_keys, after)
        else:
            result = count_keys.keys().sort()
            for k, v in result:
                print(f"{k}: {v}")
    else:
        return None
