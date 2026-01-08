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
<img width="1250" height="695" alt="image" src="https://github.com/user-attachments/assets/c5036d32-2b58-461a-8cda-66c008308d5d" />
