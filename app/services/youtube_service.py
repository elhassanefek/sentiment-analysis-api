import os

from googleapiclient.discovery import build 
from app.services.analyze_text import polarity_scores_reborta
import re
from  dotenv import load_dotenv 
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)



def extract_video_id(url_or_id):
    pattern = r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, url_or_id)
    if match:
        return match.group(1)
    if re.match(r"^[a-zA-Z0-9_-]{11}$", url_or_id):
        return url_or_id
    return None




def search_video_by_keyword(keyword):
    response = youtube.search().list(
        part="snippet",
        q=keyword,
        type="video",
        maxResults=1
    ).execute()
    return response["items"][0]["id"]["videoId"]




def fetch_youtube_comments( video_url, count = 10) :
    try :
         video_id = extract_video_id(video_url) 
         if not video_id :
              raise ValueError("Invalid YouTube URL")
         comments = []


         request   = youtube.commentThreads().list(
              part = "snippet" ,
              videoId = video_id ,
              maxResults = min(count , 100) ,
              textFormat = "plainText"
              
         )
         response = request.execute()

         for item in response.get("items" , [])  :
              comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
              comments.append(comment)
         return comments 
    except Exception as e :
         raise RuntimeError(f"Error fetching youtube comments :{str(e)}")
    

    
def analyze_comments(video_url, count):
    comments = fetch_youtube_comments(video_url, count)
    summary = {"pos": 0, "neu": 0, "neg": 0}
    results = []

    for c in comments:
        scores = polarity_scores_reborta(c)
        label = max(scores, key=scores.get)
        sentiment = label.split("_")[-1]
        summary[sentiment] += 1
        results.append({"text": c, "sentiment": sentiment})

    return {
        "video_url": video_url,
        "summary": summary,
        "comments": results
    }


def analyze_comments_for_multiple_videos(keyword, max_videos=3, comments_per_video=10):
    try:
        search_results = youtube.search().list(
            part="snippet",
            q=keyword,
            type="video",
            maxResults=max_videos
        ).execute()

        results = []

        for item in search_results.get("items", []):
            
            video_data = item.get("id", {})
            if video_data.get("kind") != "youtube#video":
                continue  

            video_id = video_data.get("videoId")
            if not video_id:
                continue

            title = item["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"

            try:
                comments = fetch_youtube_comments(video_id, comments_per_video)
            except Exception:
                comments = []

            summary = {"pos": 0, "neu": 0, "neg": 0}
            analyzed_comments = []

            for comment in comments:
                scores = polarity_scores_reborta(comment)
                label = max(scores, key=scores.get)
                sentiment = label.split("_")[-1]
                summary[sentiment] += 1
                analyzed_comments.append({"text": comment, "sentiment": sentiment})

            results.append({
                "video_id": video_id,
                "video_url": video_url,
                "title": title,
                "summary": summary,
                "comments": analyzed_comments
            })

        return results 

    except Exception as e:
        raise RuntimeError(f"Failed to analyze multiple videos: {str(e)}")
