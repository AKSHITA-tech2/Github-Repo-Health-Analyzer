import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_BASE = "https://api.github.com"
TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json"
}

if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def parse_repo_url(repo_url: str):
    """
    https://github.com/owner/repo -> (owner, repo)
    """
    try:
        parts = repo_url.rstrip("/").split("/")
        owner = parts[-2]
        repo = parts[-1]
        return owner, repo
    except Exception:
        raise ValueError("Invalid GitHub repo URL")


def get_repo_info(repo_url: str):
    owner, repo = parse_repo_url(repo_url)

    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code}")

    data = response.json()

    return {
        "name": data["full_name"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "open_issues": data["open_issues_count"],
        "default_branch": data["default_branch"],
        "created_at": data["created_at"],
        "updated_at": data["updated_at"]
    }
