from flask import Blueprint

auth_views = Blueprint("auth", __name__)

@auth_views.route("/register",methods=["GET"])
def register():
    return "Register"

@auth_views.route("/login",methods=["GET"])
def login():
    return "Login"

@auth_views.route("/absensi",methods=["GET"])
def index():
    return  "Absen"