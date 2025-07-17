import snscrape.modules.twitter as sntwitter
import pandas as pd

def scrape_twitter_snscrape(username, limit=50):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
        if i >= limit:
            break
        tweets.append({
            "date": tweet.date,
            "content": tweet.content,
            "likes": tweet.likeCount,
            "retweets": tweet.retweetCount
        })

    df = pd.DataFrame(tweets)
    df.to_csv(f"output/csvs/{username}_twitter_snscrape.csv", index=False)
    print(f"[✔] Twitter data for '{username}' saved using snscrape.")
