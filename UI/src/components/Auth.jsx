import { useState } from 'react'
import './Auth.css'
import Register from './sub-components/Register'
import Login from './sub-components/Login'
import 'https://kit.fontawesome.com/4a24fc7d8b.js'
import { useNavigate } from "react-router-dom"

function Auth({inputAuth}) {
  const [auth, setAuth] = useState(inputAuth)
  const navigate = useNavigate();


  const handleChangeAuth = () => {
    let newAuth = !auth
    setAuth(newAuth)
    if (newAuth) {
      navigate('../signup')
    }
    else{
      navigate('../login')
    }
  }

  return (
    <>
      {auth? <Login handleChangeAuth={handleChangeAuth}/> : <Register handleChangeAuth={handleChangeAuth}/>}
    </>
  )
}

export default Auth
