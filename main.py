from instagram_scraper import scrape_instagram
from twitter_scraper import scrape_twitter_snscrape
from generic_scraper import scrape_website_title

def main():
    print("🔍 Social Media Footprinter")
    target = input("Enter target username (without @): ")

    print("\n[1] Instagram")
    print("[2] Twitter")
    print("[3] Website Title")
    print("[4] All")
    choice = input("Choose option: ")

    if choice == "1":
        scrape_instagram(target)
    elif choice == "2":
        scrape_twitter_snscrape(target)
    elif choice == "3":
        url = input("Enter URL: ")
        scrape_website_title(url)
    elif choice == "4":
        scrape_instagram(target)
        scrape_twitter_snscrape(target)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
