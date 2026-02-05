from flask import Blueprint, request, jsonify
from model.feedback import get_db

feedback_bp = Blueprint("feedback", __name__)

@feedback_bp.route("/feedback", methods=["POST"])
def submit_feedback():
    data = request.json

    db = get_db()
    db.execute(
        "INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)",
        (data.get("name"), data.get("email"), data.get("message"))
    )
    db.commit()
    db.close()

    return jsonify({"status": "success"}), 201


@feedback_bp.route("/feedback", methods=["GET"])
def read_feedback():
    db = get_db()
    data = db.execute("SELECT * FROM feedback").fetchall()
    db.close()

    return jsonify(data)
