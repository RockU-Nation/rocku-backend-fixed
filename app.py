from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    image = data.get("image")
    artist_id = data.get("artistId")
    
    if not image or not artist_id:
        return jsonify({"error": "Missing image or artist ID"}), 400

    # Mock successful video generation
    return jsonify({
        "videoUrl": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4"
    })
