## Project Structure

flask-docker-app/

│
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image instructions
├── README.md # Project documentation

Setup & Run Locally

1. Clone the repository

git clone <your-repo-url>
cd flask-docker-app

2. Build the Docker image

docker build -t flask-app:1.0 .

3. Run the Docker container

docker run -d -p 5000:5000 flask-app:1.0

4. Open your browser and go to:

http://localhost:5000

Finally, you should see the output.
