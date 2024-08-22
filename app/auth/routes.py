from app.auth import auth

@auth.route("/register", methods=["GET", "POST"])
def register():
    pass

@auth.route("/login", methods=["GET", "POST"])
def login():
    pass