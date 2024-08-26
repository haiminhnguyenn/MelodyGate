const Register = ({handleChangeAuth}) => {
    return(
        <div className="container">
            <div className="form-box">
              <a href="#"><i className="fa-solid fa-house"></i></a>
              <h1 id="title">Sign up</h1>

              <form>
                <div className="input-group">
                  <div className="input-field" id="nameField">
                    <i className="fa-solid fa-user"></i>
                    <input type="text" placeholder="Username" />
                  </div>

                  <div className="input-field">
                    <i className="fa-solid fa-inbox"></i>
                    <input type="email" placeholder="Email" />
                  </div>

                  <div className="input-field">
                    <i className="fa-solid fa-lock"></i>
                    <input type="password" placeholder="Password" />
                  </div>

                </div>

                <div className="btn-field">
                  <button type="button" id="signupBtn">Sign up</button>
                  <button type="button" id="signinBtn" onClick={handleChangeAuth} className="disable">
                    Log in
                  </button>
                </div>
              </form>
            </div>
        </div>
    )
}

export default Register