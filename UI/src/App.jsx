// App.js
import { Routes, Route } from 'react-router-dom';
import Auth from './components/Auth';
 
const App = () => {
   return (
      <>
         <Routes>
            <Route path="/login" element={<Auth inputAuth={true}/>} />
            <Route path="/signup" element={<Auth inputAuth={false}/>} />
            {/* <Route path="/home" element={<Home />} />
            <Route path="/" element={<Home />} />
            <Route path="/profile/:id" element={<Profile userId={id}/>} />
            <Route path="/group/:id" element={<Group group={id}/>} /> 
            Muốn lấy id trong component thì chỉ cần thêm lệnh import { useParams } from "react-router-dom"; 
                                                        cùng với let {id} = useParams() là oke
            */}
            
            
         </Routes>
      </>
   );
};
 
export default App;