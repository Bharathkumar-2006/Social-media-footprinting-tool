from instagram_scraper import scrape_instagram
from twitter_scraper import scrape_twitter

def main():
    print("🔍 Social Media Footprinter")
    target = input("Enter target username (without @): ")

    print("\n[1] Instagram")
    print("[2] Twitter")
    print("[3] All")
    choice = input("Choose option: ")

    if choice == "1":
        scrape_instagram(target)
    elif choice == "2":
        scrape_twitter(target)
    elif choice == "3":
        scrape_instagram(target)
        scrape_twitter(target)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
