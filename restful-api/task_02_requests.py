#!/usr/bin/env python3
"""Consuming and processing data from an API using Python"""

import requests
import csv


def fetch_and_print_posts():
    """Search for all JSONplaceholder post and print them"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
        else:
            print("Failed to gather the posts")


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save them to posts.csv
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data_posts = []
        for post in posts:
            data_posts.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames=['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_posts)

        print("Posts have been successfully saved to posts.csv")
    else:
        print("Failed to fetch posts.")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
