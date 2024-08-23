from app.auth import auth
from flask import request, jsonify
from app.extensions import db
from app.models.user_profile import UserProfile
from app.email import send_email


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
def confirm(token):
    pass