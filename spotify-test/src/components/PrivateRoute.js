import React, {Component} from 'react';
import {Route, Redirect} from 'react-router-dom';

var isAuthenticated = () => {
    if( localStorage.getItem('token') == null || parseInt( localStorage.getItem('token_exp') ) < Date.now() ) {
        return false;
    } else {
        return true;
    }
}

const PrivateRoute = ({ component: Component, ...rest }) => (
  <Route {...rest} render={(props) => (
    isAuthenticated()
      ? <Component {...props} />
      : <Redirect to='/' />
  )} />
)

export default PrivateRoute;