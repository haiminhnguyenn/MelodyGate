import { useState } from 'react'
import './App.css'
import Register from './assets/components/Register'
import Login from './assets/components/Login'
import 'https://kit.fontawesome.com/4a24fc7d8b.js'

function App() {
  const [auth, setAuth] = useState(true)

  const handleChangeAuth = () => {
    let newAuth = !auth
    setAuth(newAuth)
  }

  return (
    <>
      {auth? <Login handleChangeAuth={handleChangeAuth}/> : <Register handleChangeAuth={handleChangeAuth}/>}
    </>
  )
}

export default App
