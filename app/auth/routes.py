from app.auth import auth
from flask import request, jsonify
from app.extensions import db
from app.models.user_profile import UserProfile
from app.email import send_email
from flask_login import login_required, current_user, login_user, logout_user
from datetime import timedelta


@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    
    new_user = UserProfile(
        email=data.get("email"),
        password=data.get("password"),
        username=data.get("username")
    )
    
    if new_user.has_existed_email():
        return jsonify({
            "message": "This email has already been registered. If you forgot your password, please use the forgot password feature."
        }), 400
    
    if new_user.has_existed_username():
        return jsonify({
            "message": "Username already exists. Please choose a different one."
        }), 400
    
    db.session.add(new_user)
    db.session.commit()
    
    token = new_user.generate_confirmation_token()
    send_email(
        new_user.email, 
        "Confirm Your Account","auth/confirm", 
        user=new_user, 
        token=token
    )
    
    return jsonify({
        "message": "A confirmation email has been sent."
    }), 201
    

@auth.route("/confirm/<token>")
@login_required
def confirm(token):
    if current_user.confirmed:
        return jsonify({
            "message": "This account has been already confirmed. You don't need to confirm anymore."
        }), 200
    
    if not current_user.confirm(token):
        return jsonify({
            "message": "The confirmation link is invalid or has expired."
        }), 400
   
    return jsonify({
        "message": "You have confirmed your account. Thanks!"
    }), 200


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    identifier = data.get("identifier")
    password = data.get("password")
    
    user = db.session.execute(
        db.select(UserProfile)
        .where(UserProfile.email == identifier or UserProfile.username == identifier)
    ).scalar()
    
    if user is not None and user.verify_password(password):
        login_user(user, remember=data.get("remember"), duration=timedelta(days=30))
        return jsonify({
            "message": "Log in successfully!"
        }), 200
    
    return jsonify({
        "message": "Invalid username or password."
    }), 401
    

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({
        "message": "You have been logged out."
    }), 200