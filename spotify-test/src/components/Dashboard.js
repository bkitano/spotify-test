import React, {Component} from 'react';
import queryString from 'query-string';

class Dashboard extends Component {
    
    render() {
        
        const tokenString = window.location.href.split('/')[4];
        var tokens = queryString.parse(tokenString);
        console.log(tokens);
        
        return (
            <div>
                Logged In
            </div>
            );
    }
    
}

export default Dashboard;