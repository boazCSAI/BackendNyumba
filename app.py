from flask import Flask
from flask_cors import CORS
from routes.feedback_route import feedback_bp
from model.feedback import create_table

app = Flask(__name__)
CORS(app)  # allows GitHub Pages to talk to backend


@app.route("/")
def home():
    return "Backend is running OK"


app.register_blueprint(feedback_bp)

create_table()

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # get Render port or default 5000
    app.run(host="0.0.0.0", port=port, debug=True)
