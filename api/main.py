import os                         # Used for .env.local
import requests                   # Allows Requests is a simple, yet elegant, HTTP library.
from flask import Flask, json, request, jsonify  # In Flask, we can access query params using request obj
from dotenv import load_dotenv    #
from flask_cors import CORS       # https://pypi.org/project/Flask-Cors/ : Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
from mongo_client import mongo_client

gallery = mongo_client.gallery      # db = gallery
images_collection = gallery.images  # collection = images

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

# insert_test_document()

@app.route("/new-image")            # Decorator function : route - registers function
def new_image():
  word = request.args.get("query")  # query : ?query=car
  headers = {
    "Accept-Version": "v1",
    "Authorization": "Client-ID " + UNSPLASH_KEY
  }
  params = {"query": word}
  print("----------> params ", params)
  response = requests.get(
    url=UNSPLASH_URL, 
    headers=headers, 
    params=params
  )
  # print(response.json())
  # return {"word": word}
  data = response.json()
  return {"data": data}  # if you return dictionary, 'content-type' will be JSON
  # return data

@app.route("/images", methods=["GET", "POST"])
def images():
  if request.method == "GET":
    # read images from the database
    images = images_collection.find({})
    return jsonify([img for img in images])
  if request.method == "POST":
    # save image in the database
    # json.loads(request.data)
    image = request.get_json()
    # print("image ", image)                # image  {'id': '123', 'title': 'My images'}
    image["_id"] = image.get("id")
    # print("image['_id'] ", image["_id"])  # image['_id']  123

    result = images_collection.insert_one(image)
    print("result ", result)
    inserted_id = result.inserted_id
    print("inserted_id ", inserted_id)
    return {"inserted_id": inserted_id}
    # return {
    #   "result": result,
    #   "inserted_id": inserted_id
    # }

@app.route("/images/<image_id>", methods=["DELETE"])
def image(image_id):
    if request.method == "DELETE":
        # delete image from the database
        result = images_collection.delete_one({"_id": image_id})
        if not result:
            return {"error": "Image wasn't deleted. Please try again"}, 500
        if result and not result.deleted_count:
            return {"error": "Image not found"}, 404
        return {"deleted_id": image_id}

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
