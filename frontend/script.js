async function analyzeRepo() {
    const repoUrl = document.getElementById("repoUrl").value;
    const dash = document.getElementById("dashboard");
    const error = document.getElementById("error");
    const badge = document.getElementById("healthBadge");

    dash.classList.add("hidden");
    error.textContent = "";
    badge.className = "badge";

    if (!repoUrl) {
        error.textContent = "Enter a GitHub repository URL";
        return;
    }

    try {
        console.log("Sending to backend:", repoUrl);

        const res = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ repo_url: repoUrl }),
        });

        const data = await res.json();
        console.log("Backend replied:", data);

        if (!res.ok || data.error) {
            throw new Error(data.error || "Request failed");
        }

        document.getElementById("repoName").textContent = data.repository.name;
        document.getElementById("stars").textContent = data.repository.stars;
        document.getElementById("forks").textContent = data.repository.forks;
        document.getElementById("issues").textContent = data.repository.open_issues;

        const score = data.readme_analysis.score;
        document.getElementById("readmeScore").textContent = score;
        document.getElementById("readmeFill").style.width = score + "%";

        if (score >= 75) badge.textContent = "Healthy Repository", badge.classList.add("good");
        else if (score >= 40) badge.textContent = "Moderate Health", badge.classList.add("ok");
        else badge.textContent = "Needs Attention", badge.classList.add("bad");

        dash.classList.remove("hidden");
    } catch (err) {
        console.error("ERROR:", err);
        error.textContent = "Failed to analyze repository";
    }
}
