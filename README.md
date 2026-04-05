# 🚀 API Automation Framework — FastAPI + Pytest + Allure

![CI Status](https://github.com/PragatiNangare/API-Automation-Framework-using-FastAPI-Pytest/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-7.x-orange?logo=pytest&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-Report-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A complete **API automation testing framework** built using **FastAPI**, **Pytest**, and **Allure**, with support for CRUD operations, dynamic API chaining, structured logging, and CI/CD via GitHub Actions.

---

## 📑 Table of Contents

- [About the Project](#-about-the-project)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Run the FastAPI Server](#run-the-fastapi-server)
  - [Run the Tests](#run-the-tests)
  - [Generate Allure Report](#generate-allure-report)
- [API Endpoints](#-api-endpoints)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Allure Report](#-allure-report)
- [Author](#-author)

---

## 📌 About the Project

This project demonstrates a **production-style API test automation framework** designed around best practices in software testing. It includes:

- A **live FastAPI server** serving RESTful CRUD endpoints for a `users` resource
- **Pytest-based test suite** that exercises all API operations (GET, POST, PUT, DELETE)
- **Dynamic API chaining** — test flows where one test's response feeds into the next
- **Allure reporting** for rich, visual HTML test reports
- **GitHub Actions CI/CD** that runs the tests automatically on every push and publishes the Allure report to GitHub Pages

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| **FastAPI** | REST API server (System Under Test) |
| **Pytest** | Test runner and assertions |
| **Requests / HTTPX** | HTTP client for API calls |
| **Allure-Pytest** | Test reporting plugin |
| **Uvicorn** | ASGI server to run FastAPI |
| **GitHub Actions** | CI/CD pipeline automation |
| **GitHub Pages** | Allure report hosting |

---

## 📁 Project Structure

```
API-Automation-Framework-using-FastAPI-Pytest/
│
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD pipeline
│
├── data/
│   └── test_data.json          # Externalized test data
│
├── utils/
│   └── helpers.py              # Utility/helper functions
│
├── allure-results/             # Raw Allure results (generated at runtime)
│
├── base_api.py                 # Base API class with reusable HTTP methods
├── config.py                   # Configuration (base URL, headers, env settings)
├── main.py                     # FastAPI application (System Under Test)
├── test_api.py                 # Pytest test cases
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## ⚡ Getting Started

### Prerequisites

- Python **3.11+**
- pip
- Java **8+** (required for Allure CLI)
- [Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline) installed locally (for local report generation)

---

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/PragatiNangare/API-Automation-Framework-using-FastAPI-Pytest.git
cd API-Automation-Framework-using-FastAPI-Pytest
```

**2. Create and activate a virtual environment (recommended)**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

### Run the FastAPI Server

Start the server locally before running tests:

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be live at: **http://localhost:8000**

Interactive API docs (Swagger UI): **http://localhost:8000/docs**

---

### Run the Tests

Make sure the FastAPI server is running, then in a **separate terminal**:

```bash
# Run all tests
python -m pytest test_api.py -v

# Run with Allure results output
python -m pytest test_api.py -v --alluredir=allure-results --tb=short
```

---

### Generate Allure Report

After running the tests:

```bash
# Generate the HTML report
allure generate allure-results --clean -o allure-report

# Open in browser
allure open allure-report
```

---

## 🔗 API Endpoints

The FastAPI app exposes the following CRUD endpoints for the `/users` resource:

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/users` | Get all users |
| `GET` | `/users/{user_id}` | Get a user by ID |
| `POST` | `/users` | Create a new user |
| `PUT` | `/users/{user_id}` | Update an existing user |
| `DELETE` | `/users/{user_id}` | Delete a user by ID |

**Sample Request — Create User**

```json
POST /users
{
  "name": "Pragati",
  "job": "QA Engineer"
}
```

**Sample Response**

```json
{
  "id": 3,
  "name": "Pragati",
  "job": "QA Engineer"
}
```

---

## ⚙️ CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs automatically on every **push** or **pull request** to `main`.

### Pipeline Stages

```
Checkout Code
     ↓
Set up Python 3.11
     ↓
Install Dependencies
     ↓
Start FastAPI Server (background)
     ↓
Run Pytest + Generate Allure Results
     ↓
Install Allure CLI
     ↓
Generate Allure HTML Report
     ↓
Upload Report as Artifact
     ↓
Deploy Report to GitHub Pages
```

### Trigger the Pipeline Manually

You can also trigger a run manually from the **Actions** tab in GitHub using the `workflow_dispatch` trigger.

### Required Setup (one-time)

1. Go to **Settings → Actions → General → Workflow permissions**
   → Select **"Read and write permissions"** → Save

2. Go to **Settings → Pages**
   → Source: **Deploy from a branch** → Branch: `gh-pages` → Save

3. *(If 403 errors persist)* Create a Personal Access Token (PAT) with `repo` scope
   → Add it as a repository secret named `GH_PAT`
   → Replace `github_token` with `personal_token: ${{ secrets.GH_PAT }}` in `ci.yml`

---

## 📊 Allure Report

The Allure report is automatically published to GitHub Pages after every successful push to `main`.

🔗 **Live Report:** [https://pragatingangare.github.io/API-Automation-Framework-using-FastAPI-Pytest/](https://pragatingangare.github.io/API-Automation-Framework-using-FastAPI-Pytest/)

The report includes:
- ✅ Test pass/fail status per endpoint
- 📋 Request and response details per test
- 📈 Test execution timeline
- 🏷️ Categorized test suites

---

## 👩‍💻 Author

**Pragati Nangare**

QA Engineer | API & Automation Testing

[![GitHub](https://img.shields.io/badge/GitHub-PragatiNangare-181717?logo=github)](https://github.com/PragatiNangare)

---

> 💡 *This framework was built to demonstrate real-world API automation skills including test design, CI/CD integration, and reporting — applicable to enterprise QA environments.*
