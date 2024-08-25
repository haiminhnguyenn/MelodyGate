from app.auth import auth
from flask import request, jsonify, current_app as app
from app.extensions import db
from app.models.user_profile import UserProfile
from app.email import send_email
from flask_login import login_required, current_user, login_user, logout_user
from datetime import timedelta
from flask_cors import cross_origin
from itsdangerous import URLSafeTimedSerializer as Serializer


@auth.route("/register", methods=["POST"])
@cross_origin
def register():
    data = request.get_json()
    
    new_user = UserProfile(
        email=data.get("email"),
        password=data.get("password"),
        username=data.get("username")
    )
    
    if new_user.has_existed_email():
        return jsonify({
            "message": "This email has already been registered. If you forgot your password, please use the forgot password feature.",
            "success": False
        }), 400
    
    if new_user.has_existed_username():
        return jsonify({
            "message": "Username already exists. Please choose a different one.",
            "success": False
        }), 400
    
    db.session.add(new_user)
    db.session.commit()
    
    token = new_user.generate_confirmation_token()
    send_email(
        new_user.email, 
        "Confirm Your Account",
        "auth/confirm", 
        user=new_user, 
        token=token
    )
    
    return jsonify({
        "message": "A confirmation email has been sent to you by email.",
        "success": True
    }), 201
    

@auth.route("/confirm/<token>")
@login_required
@cross_origin
def confirm(token):
    if current_user.confirmed:
        return jsonify({
            "message": "This account has been already confirmed. You don't need to confirm anymore.",
            "success": True
        }), 200
    
    if not current_user.confirm(token):
        return jsonify({
            "message": "The confirmation link is invalid or has expired.",
            "success": False
        }), 400
   
    return jsonify({
        "message": "You have confirmed your account. Thanks!",
        "success": True
    }), 200
    

@auth.route("/confirm")
@login_required
@cross_origin
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(
        current_user.email,
        "Confirm Your Account",
        "auth/confirm",
        user=current_user, 
        token=token
    )
    
    return jsonify({
        "message": "A new confirmation email has been sent to you by email.",
        "success": True
    }), 200


@auth.route("/login", methods=["POST"])
@cross_origin
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
            "message": "Log in successfully!",
            "success": True,
            "user": {
                "id": user.id, 
                "email": user.email, 
                "username": user.username, 
                "confirmed": user.confirmed
            }
        }), 200
    
    return jsonify({
        "message": "Invalid username or password.",
        "success": False
    }), 401
    

@auth.route("/logout")
@login_required
@cross_origin
def logout():
    logout_user()
    return jsonify({
        "message": "You have been logged out.",
        "success": True
    }), 200


@auth.route("/password_reset", methods=["POST"])
@cross_origin
def password_reset_request():
    email = request.get_json().get("email")
    user = db.session.execute(
        db.select(UserProfile)
        .where(UserProfile.email == email)
    )
    
    if user is None:
        return jsonify({
            "message": "That address is either invalid, not a verified email or is not associated with a personal user account.",
            "success": False
        }), 404
    
    token = user.generate_reset_token()
    send_email(
        email,
        "Reset Your Password",
        "auth/reset_password",
        user=user,
        token=token
    )
    
    return jsonify({
        "message": "An email with instructions to reset your password has been sent to you",
        "success": True
    }), 200


@auth.route("/password_reset/<token>", methods=["POST"])
@cross_origin
def password_reset(token):
    new_password = request.get_json().get("new_password")
    
    s = Serializer(app.config["SECRET_KEY"])
    
    try:
        user_id = s.loads(token, salt="reset-salt")["reset"]
    except Exception:
        return jsonify({
            "message": "The token is invalid or has expired.",
            "success": False
        }), 400
    
    user = db.session.get(UserProfile, user_id)
    
    if user is None:
        return jsonify({
            "message": "User does not exist.",
            "success": False
        }), 404

    user.reset_password(new_password)
    return jsonify({
        "message": "Your password has been updated.",
        "success": True
    }), 200