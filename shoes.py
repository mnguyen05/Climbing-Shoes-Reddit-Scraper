import praw
import pandas as pd
import matplotlib.pyplot as plt

reddit = praw.Reddit(

    client_id = "Cx1NYek1zqKDQ4ewT1oDhw",
    client_secret = "iJxjulgdP_5MvUjoo_aw5Bt_fjNoZg",
    user_agent = "climbing by michael"





)

print("Enter climbing shoe names: ")
user_input = input("(MAKE SURE ITS FORMATTED AS: ((Brand Name Shoes), etc.))\n> ")

SHOES = [shoe.strip() for shoe in user_input.split(",") if shoe.strip()]
print(f"\n🧗‍♂️ Tracking {len(SHOES)} shoes:\n- " + "\n- ".join(SHOES))

LIMIT = 100  

posts = []

print("\n⏳ Collecting Reddit posts mentioning these shoes...")
for shoe in SHOES:
    for submission in reddit.subreddit("climbing").search(shoe, limit=LIMIT, sort="top"):
        posts.append({
            "shoe": shoe,
            "title": submission.title,
            "score": submission.score,
            "num_comments": submission.num_comments,
            "url": submission.url
        })

df = pd.DataFrame(posts)
print(f"Collected {len(df)} total posts.\n")

if df.empty:
    print("⚠️ No posts found — try simpler or more common shoe names.")
    exit()

ranking = (
    df.groupby("shoe")
      .agg(
          mentions=("title", "count"),
          avg_score=("score", "mean"),
          total_comments=("num_comments", "sum")
      )
      .sort_values("mentions", ascending=False)
      .reset_index()
)

ranking["popularity_score"] = (
    ranking["mentions"] * 0.6 +
    ranking["avg_score"] * 0.3 +
    ranking["total_comments"] * 0.1
)

ranking = ranking.sort_values("popularity_score", ascending=False).reset_index(drop=True)

print("Most Popular Climbing Shoes on Reddit:\n")
print(ranking[["shoe", "mentions", "avg_score", "total_comments", "popularity_score"]])
print("\n")





# bar chart

print("You will be shown a bar chart of the most talked about climbing shoes on reddit")

plt.figure(figsize=(10, 5))
plt.barh(ranking["shoe"], ranking["popularity_score"], color="orange")
plt.xlabel("Popularity Score")
plt.ylabel("Climbing Shoe")
plt.title("Most Talked-About Climbing Shoes on Reddit")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()





