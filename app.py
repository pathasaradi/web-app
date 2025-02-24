from flask import Flask, jsonify, render_template
import psycopg2
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Retrieve database credentials from environment variables.
# For production, consider using AWS Secrets Manager or Parameter Store.
DB_HOST = os.getenv("DB_HOST", "your-rds-endpoint")
DB_NAME = os.getenv("DB_NAME", "your-database")
DB_USER = os.getenv("DB_USER", "your-username")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your-password")

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM sample_table;")
        rows = cur.fetchall()
        return jsonify(rows)
    except Exception as e:
        print(f"Query error: {e}")
        return jsonify({"error": "Query failed"}), 500
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    # For production, use gunicorn to run the app.
    app.run(host='0.0.0.0', port=5000, debug=True)
