We made a Flask web app that talks to a PostgreSQL database, and we run both using Docker Compose.

flask-postgres-app/
│
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Flask image build instructions
├── docker-compose.yml # Orchestration for Flask + Postgres

Flask App (Python)
•	Runs a web server.
•	Uses psycopg2 to connect to Postgres.

PostgreSQL (Database)
•	Stores data (in our case, user names).
•	Runs as a separate container.

Docker Compose
•	Starts both containers (Flask and Postgres).
•	Makes sure Flask can find the database by service name (host="db").

 
•	Flask = frontend logic (routes)
•	Postgres = backend storage (data)
•	Docker Compose = manager that runs both together


Getting Started

Step 1: Clone the repository
git clone <your-repo-url>
cd flask-postgres-app

Step 2: Build and run docker-compose
docker-compose up –build

Step 3: Output
Flask app runs on http://localhost:5000
