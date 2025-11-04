# 🚀 Docker Swarm Load Balancing Project

This project demonstrates how to deploy a **scalable web application** using **Docker Swarm** and **Nginx** for **load balancing**.  
It uses a simple **Flask** (or Node.js) application running in multiple replicas, and an **Nginx reverse proxy** to distribute incoming traffic across them.

---

## 🧠 Overview

When multiple users access the same web app, running just one container may not handle all requests efficiently.  
To fix this, we use **Docker Swarm** to run multiple containers (replicas) of the app and **Nginx** to distribute traffic evenly among them.

**Architecture:**

Client → Nginx (Load Balancer) → Multiple Flask App Containers

---

## ⚙️ Tech Stack

- **Docker Swarm** — Container orchestration and scaling  
- **Nginx** — Reverse proxy & load balancer  
- **Flask** — Web application framework  
- **Docker Hub** — Image registry (for `bala336/myapp:v1`)

---

## 🏗️ Project Structure

```bash

swarm-loadbalancer/
│
├── docker-compose.yml # Swarm deployment file
├── nginx.conf # Nginx reverse proxy configuration
└── app/
├── app.py # Flask app code
├── requirements.txt
└── Dockerfile


---

## 🚀 Steps to Deploy

1️⃣ Build and Push the App Image

cd app/
docker build -t bala336/myapp:v1 .
docker push bala336/myapp:v1

2️⃣ Initialize Docker Swarm

docker swarm init

3️⃣ Deploy the Stack

docker stack deploy -c docker-compose.yml myapp

4️⃣ Verify Services

docker service ls
docker service ps myapp_web

Expected output:

ID             NAME          MODE         REPLICAS   IMAGE                 PORTS
abcd1234xyz    myapp_nginx   replicated   1/1        nginx:latest          *:80->80/tcp
efgh5678uvw    myapp_web     replicated   3/3        bala336/myapp:v1

🌐 Access the Application
Open your browser and go to:

http://localhost

🧹 Clean Up

docker stack rm myapp
docker swarm leave --force

💡 Key Learnings

Docker Swarm simplifies container scaling and orchestration
Nginx effectively load balances requests between multiple containers
You can achieve high availability and fault tolerance with minimal setup

🧑‍💻 Author

Balakrishnan T (Bala336)
DevOps Engineer | Cloud Enthusiast
