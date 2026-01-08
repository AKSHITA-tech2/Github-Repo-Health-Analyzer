# GitHub Repo Health Analyzer 🩺

A lightweight tool that analyzes the **health of a GitHub repository** using public signals such as activity, maintenance, and documentation quality.

Built to demonstrate **GitHub API usage, backend engineering with FastAPI, and clean frontend integration**.

---

## 🚀 Features

- Analyze any public GitHub repository via URL
- Fetch core repository metrics:
  - ⭐ Stars
  - 🍴 Forks
  - 🐛 Open issues
- README quality scoring (rule-based and explainable)
- Health status indicator: **Healthy / Moderate / Needs Attention**
- REST API built with FastAPI
- Minimal, professional dashboard UI

---

## 🧠 README Scoring Logic

The README score is calculated out of **100**, based on:

- **Content length** (sufficient descriptive detail)
- **Presence of key sections**:
  - Overview / Description
  - Installation
  - Usage
  - Features
  - License
  - Contributing
- **Links or badges** (documentation richness)

This approach avoids black-box ML and keeps the evaluation **transparent and interview-friendly**.

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- GitHub REST API

### Frontend
- HTML
- CSS
- Vanilla JavaScript

---
## 📸 Screenshot of Analysis
<img width="988" height="273" alt="image" src="https://github.com/user-attachments/assets/b449c3d5-0e2f-434e-9b3a-84368f721117" />
<img width="1611" height="503" alt="image" src="https://github.com/user-attachments/assets/597333a1-8cc4-4a6d-9ae8-5bb6fb40817a" />


