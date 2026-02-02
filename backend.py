
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="dist", static_url_path="")
CORS(app)

MICROSOFT_LOGIN_URL =     "https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize?client_id=c44b4083-3bb0-49c1-b47d-974e53cbdf3c&scope=https%3A%2F%2Fmanagement.core.windows.net%2F%2F.default%20openid%20profile%20offline_access&redirect_uri=https%3A%2F%2Fportal.azure.com%2Fauth%2Flogin%2F&client-request-id=019c0178-3287-705e-a195-6c98d603ca2f&response_mode=fragment&client_info=1&nonce=019c0178-3289-7f3f-9251-67159a41edfc&state=eyJpZCI6IjAxOWMwMTc4LTMyODgtNzJiNS1iZjkzLTdlMTU3ODM5NGEwNiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.21.0&response_type=code&code_challenge=dKE0Kyq-SHQMnqTZmzbQDYPmXYBuhC2JBaOMQVGDHXo&code_challenge_method=S256&site_id=501430&instance_aware=true&sso_reload=true"



# --------------------
# API ROUTES
# --------------------

@app.route("/api/auth/login", methods=["GET"])
def login():
    return jsonify({"auth_url": MICROSOFT_LOGIN_URL})

@app.route("/api/auth/verify", methods=["GET"])
def verify():
    return jsonify({
        "user": {
            "name": "Demo User",
            "email": "demo@optum.com",
            "role": "analyst"
        },
        "permissions": {
            "can_modify_agents": True,
            "max_queries_per_day": 100
        }
    })

@app.route("/api/auth/logout", methods=["POST"])
def logout():
    return jsonify({"success": True})

@app.route("/api/chat", methods=["POST"])
def chat():
    return jsonify({
        "success": True,
        "response": "Gunicorn backend connected.",
        "visualization": None
    })

# --------------------
# FRONTEND ROUTES
# --------------------

@app.route("/")
@app.route("/<path:path>")
def serve_frontend(path=""):
    if path != "" and os.path.exists(os.path.join("dist", path)):
        return send_from_directory("dist", path)
    return send_from_directory("dist", "index.html")
