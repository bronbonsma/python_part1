from flask import Flask,json
import requests
from Exercises.BasePost import BasePost

app = Flask(__name__)


@app.route("/posts/<posts_id>")
def get_posts(posts_id):
   post_response = requests.get("https://jsonplaceholder.typicode.com/posts/"+posts_id)
   posts = post_response.json()
   response = app.response_class(
       response=json.dumps(posts),
       status=200,
       mimetype="application/json"
   )

   return response

@app.route("/posts/<userId>/comments")
def get_comments(userId):
   post_response = requests.get("https://jsonplaceholder.typicode.com/posts/"+userId+"/comments")
   posts = post_response.json()

   response = app.response_class(
       response=json.dumps(posts),
       status=200,
       mimetype="application/json"
   )

   return response


@app.route("/posts-by-userId/<userId>")
def get_user(userId):
   post_response = requests.get("https://jsonplaceholder.typicode.com/posts/?userId="+userId)
   posts = post_response.json()

   response = app.response_class(
       response=json.dumps(posts),
       status=200,
       mimetype="application/json"
   )

   return response

@app.route("/posts/<posts_id>")
def get_posts(posts_id):
   post_response = requests.get("https://jsonplaceholder.typicode.com/posts/"+posts_id)
   posts = post_response.json()

   response = app.response_class(
       response=json.dumps(posts),
       status=200,
       mimetype="application/json"
   )

   return response


@app.route("/posts/")
def convert_to_json(posts):
    response = app.response_class(
        response=json.dumps(posts),
        status=200,
        mimetype="application/json"
    )
    return response


if __name__ == "__main__":
    app.run()









