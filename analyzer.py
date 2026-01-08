from github_api import get_repo_info
from metrics.readme import score_readme

print(score_readme("https://github.com/swirlai/swirl-search"))

def main():
    repo_url = input("Enter GitHub repo URL: ").strip()

    try:
        info = get_repo_info(repo_url)
        print("\n📊 Repository Overview\n")
        for key, value in info.items():
            print(f"{key.replace('_', ' ').title():20}: {value}")
    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    main()
