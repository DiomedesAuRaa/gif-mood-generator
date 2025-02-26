from flask import Flask, request, render_template
import requests
import os
from dotenv import load_dotenv  # Import the load_dotenv function

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("GIPHY_API_KEY")
# Debug: Print the API key to verify it's being loaded
print(f"GIPHY_API_KEY: {API_KEY}")
def get_gif(mood):
    url = f"https://api.giphy.com/v1/gifs/translate?api_key={API_KEY}&s={mood}&rating=g"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        gif_url = data['data']['images']['original']['url']
        return gif_url
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    gif_url = None
    if request.method == "POST":
        mood = request.form.get("mood")
        if mood:
            gif_url = get_gif(mood)
    return render_template("index.html", gif_url=gif_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)