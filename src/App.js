
import './App.css';
import Layout from './component/Layout/Layout';
import { BrowserRouter as Router, Navigate, Route, Routes } from 'react-router-dom';
//import Navbar from './component/navbar/Navbar';
import CustomRoutes from './component/route/routes';



function App() {
  return (
    <div className="App">
      
      <Router basename={process.env.PUBLIC_URL}>
            <Routes>
              <Route path="/*" element={<CustomRoutes />} />
            </Routes>
        </Router>
              
    </div>
  );
}

export default App;
