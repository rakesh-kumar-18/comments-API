from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# Base URL of the REST API
BASE_URL = "https://app.ylytic.com/ylytic/test"


# Define a route for the search API
@app.route('/search', methods=['GET'])
def search_comments():
    # Get search parameters from the query string
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('search_text')

    # Convert date strings to datetime objects in a common format
    if at_from:
        at_from = datetime.strptime(at_from, '%d-%m-%Y')

    if at_to:
        at_to = datetime.strptime(at_to, '%d-%m-%Y')

    # Build parameters for the request to the REST API
    params = {
        'search_author': search_author,
        'at_from': at_from,
        'at_to': at_to,
        'like_from': like_from,
        'like_to': like_to,
        'reply_from': reply_from,
        'reply_to': reply_to,
        'search_text': search_text
    }

    # Make a request to the provided REST API
    response = requests.get(BASE_URL, params=params)
    response_data = response.json()

    comments_data = response_data["comments"]

    # Apply filters based on the criteria
    filtered_comments = []

    for comment in comments_data:
        comment_date = datetime.strptime(
            comment['at'], '%a, %d %b %Y %H:%M:%S %Z')

        if at_from and comment_date < at_from:
            continue

        if at_to and comment_date > at_to:
            continue

        if search_author and search_author.lower() not in comment['author'].lower():
            continue

        if like_from is not None and int(comment['like']) < int(like_from):
            continue

        if like_to is not None and int(comment['like']) > int(like_to):
            continue

        if reply_from is not None and int(comment['reply']) < int(reply_from):
            continue

        if reply_to is not None and int(comment['reply']) > int(reply_to):
            continue

        if search_text and search_text.lower() not in comment['text'].lower():
            continue

        filtered_comments.append(comment)

    return jsonify({"comments": filtered_comments})


if __name__ == '__main__':
    app.run(debug=True)
