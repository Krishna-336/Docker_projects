# 🚀 Custom Docker Image Build & CI/CD Pipeline using GitHub Actions

This project demonstrates how to **automate Docker image builds and deployments** using **GitHub Actions** and **Docker Hub**.  
Every push to the `main` branch triggers a GitHub Actions workflow that builds a Docker image from the app source and pushes it to Docker Hub.

---

## 🧩 Project Overview

**Goal:**  
Automate the build and deployment of a Dockerized application using a CI/CD pipeline.

**Tech Stack:**
- **GitHub Actions** – for CI/CD automation
- **Docker Hub** – to store Docker images
- **Node.js** – as the sample application

---

## 🛠️ Prerequisites

1. **GitHub Account**
2. **Docker Hub Account**
3. **Docker Hub Access Token**
   - Go to [Docker Hub → Account Settings → Security → Access Tokens](https://hub.docker.com/settings/security)
   - Create a new token and save it securely.

## ⚙️ Project Structure
```bash
.
├── app.py / index.js # Application source code
├── requirements.txt / package.json
├── Dockerfile # Docker build instructions
└── .github/
└── workflows/
└── docker.yml # GitHub Actions workflow definition

--- 

## 🚀 Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

2️⃣ Dockerize Your App

Create a Dockerfile for your app.

3️⃣ Create GitHub Actions Workflow

Create .github/workflows/docker.yml

4️⃣ Configure GitHub Secrets

Go to your GitHub repository →
Settings → Secrets and variables → Actions → New repository secret

Add:

DOCKER_USERNAME → Your Docker Hub username

DOCKER_PASSWORD → Your Docker Hub access token

5️⃣ Push Code and Trigger the Workflow
git add .
git commit -m "Setup GitHub Actions for Docker build and push"
git push origin main

Then go to GitHub → Actions tab to see your CI/CD pipeline in action.

📦 Output

After a successful run:

Your Docker image will be available at
docker.io/<your-username>/myapp:latest

You can verify it locally:

docker pull <your-username>/myapp:latest
docker run -d -p 5000:5000 <your-username>/myapp:latest

Access your app at:
👉 http://localhost:5000
