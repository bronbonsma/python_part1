
from flask import Flask,json
import requests

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
if __name__ == "__main__":
    app.run()


