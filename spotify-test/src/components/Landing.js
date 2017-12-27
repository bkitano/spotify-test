import React, { Component } from 'react';
import FlatButton from 'material-ui/FlatButton';

class Landing extends Component {
    
    onClick(e) {
        console.log('clicked');
        if( localStorage.getItem('count') ) {
            const count = localStorage.getItem('count');
            localStorage.setItem('count', count + 1);
        } else {
            localStorage.setItem('count', 1);
        }
        console.log(localStorage.getItem('count'));
    }
    
    render() {
        return (
            <div>
                <FlatButton label="cookie test" onClick={e => this.onClick(e)} />
            </div>
            )
    }
}

export default Landing;