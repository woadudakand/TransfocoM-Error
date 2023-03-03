import { Component, lazy } from 'react';
import { Route, Routes } from 'react-router-dom';
//import LoadingSpinner from '../pages/loading/LoadingSpinner';


const Dashboard = lazy(() => import('../dashboard/Dashboard'));
const Enquiry = lazy(() => import('../pages/enquiry/Enquiry'));
const Quotation = lazy(() => import('../pages/quotation/Quotation'));


const CustomRoutes = ()=> {
return (

<Routes>
<Route path='/dashboard' element={ Component={Dashboard}}  />
<Route path='/enquiry' element={ Component={Enquiry}}  />
<Route path='/quotation' element={ Component={Quotation}}  />
</Routes>


)
 
};
export default CustomRoutes;