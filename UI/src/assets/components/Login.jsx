const Login = ({handleChangeAuth})=>{
    return(
        <div class="container">
            <div class="form-box">
              <a href="#"><i class="fa-solid fa-house"></i></a>
              <h1 id="title">Log in</h1>

              <form>
                <div class="input-group">
                  <div class="input-field" id="nameField">
                    <i class="fa-solid fa-user"></i>
                    <input type="text" placeholder="Username" />
                  </div>

                  <div class="input-field">
                    <i class="fa-solid fa-lock"></i>
                    <input type="password" placeholder="Password" />
                  </div>

                  <p><a href="#">Forgot Password?</a></p>
                </div>

                <div class="btn-field">
                  <button type="button" id="signupBtn" class="disable" onClick={handleChangeAuth}>Sign up</button>
                  <button type="button" id="signinBtn" onClick={handleChangeAuth}>
                    Log in
                  </button>
                </div>
              </form>
            </div>
        </div>
    )
}
export default Login