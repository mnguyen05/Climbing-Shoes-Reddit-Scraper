# Climbing-Shoes-Reddit-Scraper

A quick reddit scraping project that measures the popularity of climbing shoes based on Reddit activity and interactions

It uses the Reddit API through PRAW to collect various posts regarding climbing shoes and analyzes how much engagement those posts have

When collecting the data, we aggregate the table by shoes, mentions, avg_score, total_comments, and calculate the popularity score by weighing mentions the most interactions, followed by average score, and total comments

# To use this project:

- create an app on https://old.reddit.com/prefs/apps
- click Create app
- choose Script
- then copy the client_id, client_secret, and set the user_agent to anything INTO:

``` python
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="ClimbScope by /u/yourusername"
)

```


  

