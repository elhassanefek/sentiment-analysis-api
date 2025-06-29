import os 

import praw 
from app.services.analyze_text import polarity_scores_reborta
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit (
    client_id = os.getenv("REDDIT_CLIENT_ID"),
    client_secret = os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent = os.getenv("REDDIT_USER_AGENT")
)

def fetch_reddit_comments(subreddit_name , count =10) :
    try :
         subreddit = reddit.subreddit(subreddit_name)
         comments = []

         for post in subreddit.hot(limit = count) :
              post.comments.replace_more(limit = 0)
              for comment in post.comments[:count] :
                   comments.append(comment.body)
         return comments[:count]
    except Exception as e :
         raise RuntimeError(f"Error fetching Reddit comments: {str(e)}")
    

def analyze_reddit_subreddit(subreddit_name , count = 10):
     comments = fetch_reddit_comments(subreddit_name ,count)

     results = []
     sentiment_counts = {
          "pos" : 0 , 
          "neu" : 0 ,
          "neg" : 0
     }

     for comment in comments :
          scores = polarity_scores_reborta(comment)
          label = max(scores , key = scores.get)
          sentiment = label.split('_')[-1]
          sentiment_counts[sentiment] += 1

          results.append ({
               "text" : comment ,
               "sentiment" : sentiment
          })
     return {
          "subreddit" : subreddit_name ,
          "summary" : sentiment_counts ,
          "comments" : results
     }