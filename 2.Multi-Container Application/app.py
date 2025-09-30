import psycopg2
from flask import Flask

app = Flask(__name__)

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="mydb",
            user="user",
            password="password",
            host="db"   # <== service name in docker-compose
        )
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        return None

@app.route("/")
def home():
    conn = connect_db()
    if conn:
        conn.close()
        return "✅ Connected to DB!"
    else:
        return "❌ Failed to connect to DB."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

