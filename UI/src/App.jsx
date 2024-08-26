// App.js
import { Routes, Route } from 'react-router-dom';
import Auth from './Auth';
 
const App = () => {
   return (
      <>
         <Routes>
            <Route path="/login" element={<Auth inputAuth={true}/>} />
            <Route path="/signup" element={<Auth inputAuth={false}/>} />
         </Routes>
      </>
   );
};
 
export default App;