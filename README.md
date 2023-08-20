# Comments Search API

This project implements a RESTful API that allows you to search and filter comments from a REST API based on various criteria. The API interacts with an external API to retrieve comments and applies filtering based on author, date range, likes, replies, and text content.

## Prerequisites

- Python 3.7 or higher
- Flask
- Requests

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/rakesh-kumar-18/comments-API.git
   ```

2. Navigate to the project directory:

   ```bash
   cd comments-API
   ```
   
3. Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```
   
## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```
   
2. Open your web browser and navigate to http://127.0.0.1:5000/search.

3. Use the API by appending query parameters to the URL. For example:

   ```arduino
   http://127.0.0.1:5000/search?search_author=AuthorName&at_from=01-01-2023&at_to=01-02-2023&like_from=0&like_to=5&reply_from=0&reply_to=5&search_text=economic
   ```
   
   Replace the parameters with your desired search criteria.

## API Endpoint

### GET /search

- `search_author`: Search comments by author's name.
- `at_from` and `at_to`: Search comments within a date range (format: dd-mm-yyyy).
- `like_from` and `like_to`: Search comments with a specific number of likes.
- `reply_from` and `reply_to`: Search comments with a specific number of replies.
- `search_text`: Search comments containing a specific text.
