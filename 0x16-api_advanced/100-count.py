#!/usr/bin/python3
""" This script is an raddit api..."""

import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """this count all words"""

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for z in range(len(word_list)):
                    if word_list[z].lower() == word.lower():
                        count[z] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for y in range(len(word_list)):
                for z in range(y + 1, len(word_list)):
                    if word_list[y].lower() == word_list[z].lower():
                        save.append(z)
                        count[y] += count[z]

            for y in range(len(word_list)):
                for z in range(y, len(word_list)):
                    if (count[z] > count[y] or
                            (word_list[y] > word_list[z] and
                             count[z] == count[y])):
                        aux = count[y]
                        count[y] = count[z]
                        count[z] = aux
                        aux = word_list[y]
                        word_list[y] = word_list[z]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (count[y] > 0) and y not in save:
                    print("{}: {}".format(word_list[y].lower(), count[y]))
        else:
            count_words(subreddit, word_list, after, count)
