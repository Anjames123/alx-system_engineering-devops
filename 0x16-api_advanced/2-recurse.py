#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """ Returns a list of titles of all hot posts on a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    headers = {
        'User-Agent': 'MyAPI/1.0 (by /u/bdov_)'
    }

    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    for post in results.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
