from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from github_api import get_repo_info
from metrics.readme import score_readme


app = FastAPI(
    title="GitHub Repo Health Analyzer",
    description="Analyze GitHub repository health using public signals",
    version="1.0.0"
)

# CORS must come AFTER app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Repo Health Analyzer API is running"}


@app.get("/analyze")
def analyze_repo(repo_url: str):
    repo_info = get_repo_info(repo_url)
    readme_score = score_readme(repo_url)

    return {
        "repository": repo_info,
        "readme_analysis": readme_score
    }
