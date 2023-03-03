import React from 'react'
import classes from './Header.module.css';
import orignal from '../img/orignal.png';
import { IconButton, Badge, Avatar } from '@mui/material';
import NotificationsIcon from '@mui/icons-material/Notifications';
import { Link } from 'react-router-dom';


const Header = () => {


    return (
    <>
            <header className={classes.header}>
                <div className={classes.head}>
                    <div className={classes.logo}><Link to='/'></Link></div>
                    <div className={classes.quickMenu}>
                        <div>
                            <IconButton size='large' color='inherit' title='Notifications'>
                                <Badge badgeContent={5} color='warning'>
                                    <NotificationsIcon fontSize='30' />
                                </Badge>
                            </IconButton>
                        </div>
                        {/* <Avatar className={classes.avatar} /> */}

                    </div>
                    </div>
                    </header>
                </>

                )
}

                export default Header
