from scrapers.gcp.skills_boost import scrape as scrape_gcp_skills
from storage.sqlite import init_db, save_coupons


def main():
    init_db()
    all_results = scrape_gcp_skills()
    print(all_results)
    save_coupons(all_results)


if __name__ == "__main__":
    main()