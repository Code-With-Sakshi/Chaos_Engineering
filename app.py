
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

app = Flask(__name__)


# ---------------- DATABASE CONNECTION ----------------

def get_db():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )


# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Count visitors currently inside
    cursor.execute("""
        SELECT COUNT(*) AS count
        FROM visitors
        WHERE status = 'Inside'
    """)
    inside_count = cursor.fetchone()["count"]

    # Count today's visitors
    cursor.execute("""
        SELECT COUNT(*) AS count
        FROM visitors
        WHERE DATE(entry_time) = CURDATE()
    """)
    today_count = cursor.fetchone()["count"]

    cursor.close()
    db.close()

    return render_template(
        "index.html",
        inside_count=inside_count,
        today_count=today_count
    )


# ---------------- ADD VISITOR ----------------

@app.route("/add_visitor", methods=["POST"])
def add_visitor():

    visitor_name = request.form["visitor_name"].strip()
    wing = request.form["wing"].strip().upper()
    flat_number = request.form["flat_number"].strip()
    phone = request.form["phone"].strip()

    # Name validation
    if not visitor_name:
        return "Visitor name is required."

    # Wing validation
    if wing not in ["A", "B"]:
        return "Wing must be A or B."

    # Flat number validation
    try:
        flat_number = int(flat_number)
    except ValueError:
        return "Flat number must be a number."

    if flat_number < 1 or flat_number > 40:
        return "Flat number must be between 1 and 40."

    # Phone validation
    if not phone.isdigit():
        return "Phone number must contain only digits."

    if len(phone) not in [10, 12]:
        return "Phone number must be 10 or 12 digits."

    # Insert visitor
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO visitors
        (visitor_name, wing, flat_number, phone, status)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        visitor_name,
        wing,
        flat_number,
        phone,
        "Inside"
    ))

    db.commit()

    cursor.close()
    db.close()

    return redirect(url_for("home"))


# ---------------- VISITOR LIST ----------------

@app.route("/visitors")
def visitors():

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM visitors
        ORDER BY entry_time DESC
    """)

    visitors = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "visitors.html",
        visitors=visitors
    )


# ---------------- SEARCH BY FLAT ----------------

@app.route("/search", methods=["GET", "POST"])
def search():

    visitors = []
    searched = False
    error = None

    if request.method == "POST":

        flat_number = request.form["flat_number"].strip()
        searched = True

        try:
            flat_number = int(flat_number)
        except ValueError:
            error = "Flat number must be a number."
            return render_template(
                "search.html",
                visitors=visitors,
                searched=searched,
                error=error
            )

        if flat_number < 1 or flat_number > 40:
            error = "Flat number must be between 1 and 40."

            return render_template(
                "search.html",
                visitors=visitors,
                searched=searched,
                error=error
            )

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM visitors
            WHERE flat_number = %s
            ORDER BY entry_time DESC
        """, (flat_number,))

        visitors = cursor.fetchall()

        cursor.close()
        db.close()

    return render_template(
        "search.html",
        visitors=visitors,
        searched=searched,
        error=error
    )


# ---------------- EXIT VISITOR ----------------

@app.route("/exit/<int:visitor_id>")
def exit_visitor(visitor_id):

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        UPDATE visitors
        SET exit_time = CURRENT_TIMESTAMP,
            status = 'Exit'
        WHERE id = %s
        AND status = 'Inside'
    """, (visitor_id,))

    db.commit()

    cursor.close()
    db.close()

    return redirect(url_for("visitors"))


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(debug=True)