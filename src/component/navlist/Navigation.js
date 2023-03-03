import React from 'react'
import { useState, useEffect } from 'react';
import { Link, useMatch, useResolvedPath, useLocation } from 'react-router-dom';
import classes from './Navigation.module.css';
import navItems from './navdata';
import Footer from './Footer';




const Navigation = () => {

    const [nav, setNav] = useState([]);

    useEffect(() => {

        setNav(navItems)

    },[]);

  return (
    <>
    <nav className={classes.nav}>
    <ul>
      
      {
        nav.map(navItem => {
          return <CustomLink key={navItem.to} to={navItem.to}>{navItem.icon}{navItem.label}</CustomLink>;
        })
      }
    </ul>
  </nav>
  <Footer />
  </>
  )
}

export default Navigation;

const CustomLink = ({ to, children, ...props }) => {
    const { pathname } = useLocation();
    const resolvedPath = useResolvedPath(to);
    let isActive = useMatch({ path: resolvedPath.pathname });
    if (!isActive && pathname.startsWith(to)) {
      isActive = true;
    }
  
    return (<li className={isActive ? classes.active : ''}>
      <Link to={to} {...props}>{children}</Link>
    </li>)
  };