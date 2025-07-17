import requests

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAhw3AEAAAAArV25fxEaAZ5BemgSPSFkRA3oN00%3DpLSlglmsEJ5eNS3z2vNTvcMGoHAMztvLVvGXzCyZjGXl7gEmgT"

def scrape_twitter(username):
    print(f"\n🔎 Enumerating tweets for @{username} via Twitter API...")

    try:
        user_id = get_user_id(username)
        tweets = get_user_tweets(user_id, max_results=10)

        if not tweets:
            print("No tweets found.")
            return

        for i, tweet in enumerate(tweets, 1):
            print(f"\nTweet {i}:")
            print(f"Date     : {tweet['created_at']}")
            print(f"Likes    : {tweet['public_metrics']['like_count']}")
            print(f"Retweets : {tweet['public_metrics']['retweet_count']}")
            print(f"Text     : {tweet['text']}")

    except Exception as e:
        print(f"❌ Error: {e}")


def get_user_id(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]["id"]
    else:
        raise Exception(f"User lookup failed: {response.text}")


def get_user_tweets(user_id, max_results=10):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    params = {
        "max_results": max_results,
        "tweet.fields": "created_at,public_metrics"
    }
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        raise Exception(f"Tweet fetch failed: {response.text}")
