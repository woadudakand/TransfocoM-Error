import React from 'react'
import Header from '../Header/Header'
import Navigation from '../navlist/Navigation'
import CustomRoutes from '../route/routes';
import classes from './Layout.module.css';

const Layout = () => {



  return (
    <>
    <Header/>
    <div className={classes['left-panel']}><Navigation /></div>
      <div className={classes['right-panel']}>
      <main className={classes.main}>
        
      </main>
      </div>
    </>
  )
}

export default Layout
