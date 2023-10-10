#!/usr/bin/python3
"""Recursive function to query the Reddit API and count keyword occurrences in hot articles."""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively counts keyword occurrences in hot articles' titles from a given subreddit.

    :param subreddit: The name of the subreddit to query.
    :param word_list: A list of keywords to count.
    :param after: A token to specify the starting point for pagination.
    :param counts: A dictionary to store the counts of each keyword.
    """
    if counts is None:
        counts = {}

    if not word_list:
        # Sort and print the counts
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    if not subreddit:
        print("Invalid subreddit or no posts match.")
        return

    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    headers = {'User-Agent': 'MyAPI/1.0 (by /u/bdov_)'}

    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        print(f"Invalid subreddit: {subreddit}")
        return

    data = response.json().get("data")
    after = data.get("after")

    for post in data.get("children"):
        title = post.get("data").get("title").lower()
        for word in word_list:
            if title.count(f" {word.lower()} ") > 0:
                counts[word] = counts.get(word, 0) + title.count(f" {word.lower()} ")

    count_words(subreddit, word_list, after, counts)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, word_list)
