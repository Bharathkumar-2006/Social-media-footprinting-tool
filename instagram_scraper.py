import instaloader
import json
import pandas as pd

def scrape_instagram(username):
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        data = {
            "username": profile.username,
            "full_name": profile.full_name,
            "bio": profile.biography,
            "followers": profile.followers,
            "following": profile.followees,
            "posts": profile.mediacount,
            "external_url": profile.external_url,
            "is_verified": profile.is_verified
        }

        
        with open(f"data/{username}_instagram.json", "w") as f:
            json.dump(data, f, indent=4)

       
        df = pd.DataFrame([data])
        df.to_csv(f"output/csvs/{username}_instagram.csv", index=False)

        print(f"[✔] Instagram data for '{username}' saved.")
    except Exception as e:
        print(f"[!] Error scraping Instagram: {e}")

