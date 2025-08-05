from flask import request, jsonify,Flask
from flask_cors import CORS
from utils.notes import generate_notes
from utils.trns import fetch_transcript, get_video_id
from dotenv import load_dotenv
import markdown


load_dotenv()
app = Flask(__name__)


# This configuration allows all origins, methods, and headers.
# It is the most permissive and best for debugging.
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/generate_notes', methods=['POST'])
def generate_notes_api():
    data = request.get_json()
    url= data.get('youtube_url')
    video_id= get_video_id(url)

    
    
    transcript=fetch_transcript(video_id)
    notes=generate_notes(transcript)
    html_notes=markdown.markdown(notes,extensions=["fenced_code", "tables"])
    # save to mongodb

    return jsonify({"html_notes": html_notes})


if __name__=="__main__":
    app.run() 