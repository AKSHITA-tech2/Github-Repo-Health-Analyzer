import requests
from github_api import HEADERS, parse_repo_url, GITHUB_API_BASE


IMPORTANT_SECTIONS = [
    "installation",
    "usage",
    "features",
    "overview",
    "description",
    "license",
    "contributing"
]


def fetch_readme(repo_url: str) -> str:
    owner, repo = parse_repo_url(repo_url)
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/readme"

    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        return ""

    data = response.json()
    return requests.get(data["download_url"]).text


def score_readme(repo_url: str):
    content = fetch_readme(repo_url)

    if not content:
        return {
            "score": 0,
            "reason": "README not found"
        }

    text = content.lower()
    score = 0
    details = {}

    # Length score
    length = len(content)
    length_score = min(30, length // 10)
    score += length_score
    details["length_score"] = length_score

    # Section score
    section_hits = sum(1 for sec in IMPORTANT_SECTIONS if sec in text)
    section_score = min(50, section_hits * 8)
    score += section_score
    details["section_score"] = section_score

    # Links / badges
    link_score = 20 if "http" in text or "![" in text else 0
    score += link_score
    details["link_score"] = link_score

    return {
        "score": min(score, 100),
        "details": details
    }
