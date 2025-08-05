from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound,VideoUnavailable
import time
import random

yt_api = YouTubeTranscriptApi()

def get_video_id(url):
    if "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        raise ValueError("Invalid YouTube URL")

# delay time
delayed_time=random.uniform(5.0,10.0)
def fetch_transcript(video_id):
    try:

        transcript = yt_api.fetch(video_id)
        # Collect all text parts into a single string without timestamps
        full_text = " ".join(entry.text.strip() for entry in transcript if entry.text.strip())

        return full_text if full_text else "Transcript is empty or unavailable."
    except NoTranscriptFound:
        return f"Transcript not available for video ID: {video_id}"
    except VideoUnavailable:
        return f"Video with ID {video_id} is unavailable."
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"
    finally:
        time.sleep(delayed_time)
