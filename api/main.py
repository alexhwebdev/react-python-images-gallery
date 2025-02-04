import os                         # Used for .env.local
import requests                   # Allows Requests is a simple, yet elegant, HTTP library.
from flask import Flask, request  # In Flask, we can access query params using request obj
from dotenv import load_dotenv    #
from flask_cors import CORS       # https://pypi.org/project/Flask-Cors/ : Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.

load_dotenv(dotenv_path="./.env.local")
# print("os.environ ", os.environ)  # UNSPLASH_KEY should be visible with load_dotenv and relative path added

UNSPLASH_URL="https://api.unsplash.com/photos/random"
UNSPLASH_KEY=os.environ.get("UNSPLASH_KEY", "")
DEBUG=bool(os.environ.get("DEBUG", True))   # If no DEBUG env in .env.local, set to True

if not UNSPLASH_KEY:
  raise EnvironmentError("Please create .env.local file and insert there UNSPLASH_KEY")

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = DEBUG

@app.route("/new-image")            # Decorator function : route - registers function
def new_image():
  word = request.args.get("query")  # query : ?query=car
  # return {"word": word}             # if you return dictionary, 'content-type' will be JSON
  headers = {
    "Accept-Version": "v1",
    "Authorization": "Client-ID " + UNSPLASH_KEY
  }
  params = {"query": word}
  print("----------> params ", params)
  response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)

  # print(response.json())
  # return {"word": word}
  data = response.json()
  return {"data": data}
  # return data

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5050)








# from flask import Flask
# from other_module import fn_from_other_module

# # print(__name__)
# # fn_from_other_module()

# app = Flask(__name__)

# # Decorator function : route - registers function
# @app.route("/")
# def hello():
#     return "Hello, World!"

# # def hello():
# #     return "Hello, World!"
# # app.route("/")(hello)

# if __name__ == "__main__":
#   app.run(host="0.0.0.0", port=5050)
