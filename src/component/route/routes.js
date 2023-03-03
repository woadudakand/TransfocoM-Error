import { lazy, Suspense } from 'react';
import { Route, Routes } from 'react-router-dom';
import LoadingSpinner from '../pages/loading/LoadingSpinner';
import Layout from '../Layout/Layout';

const Dashboard = lazy(() => import('../dashboard/Dashboard'));
const Enquiry = lazy(() => import('../pages/enquiry/Enquiry'));
const Quotation = lazy(() => import('../pages/quotation/Quotation'));


const CustomRoutes = ()=> {
    return (
    <Suspense
        fallback={<LoadingSpinner />}>
        <Routes>
            <Route index element={<Dashboard />}  />
            <Route path='/dashboard' element={<Dashboard />}  />
            <Route path='/enquiry' element={<Enquiry />}  />
            <Route path='/quotation' element={<Quotation />}  />
        </Routes>
    </Suspense>
    )
 
};
export default Layout(CustomRoutes);