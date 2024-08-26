const Register = ({handleChangeAuth}) => {
    return(
        <div class="container">
            <div class="form-box">
              <a href="#"><i class="fa-solid fa-house"></i></a>
              <h1 id="title">Sign up</h1>

              <form>
                <div class="input-group">
                  <div class="input-field" id="nameField">
                    <i class="fa-solid fa-user"></i>
                    <input type="text" placeholder="Username" />
                  </div>

                  <div class="input-field">
                    <i class="fa-solid fa-inbox"></i>
                    <input type="email" placeholder="Email" />
                  </div>

                  <div class="input-field">
                    <i class="fa-solid fa-lock"></i>
                    <input type="password" placeholder="Password" />
                  </div>

                </div>

                <div class="btn-field">
                  <button type="button" id="signupBtn">Sign up</button>
                  <button type="button" id="signinBtn" onClick={handleChangeAuth} class="disable">
                    Log in
                  </button>
                </div>
              </form>
            </div>
        </div>
    )
}

export default Register