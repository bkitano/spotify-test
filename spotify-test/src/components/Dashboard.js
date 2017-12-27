import React, {Component} from 'react';
import queryString from 'query-string';
import spotifyWebAPI from 'spotify-web-api-node';

import {Card, CardText, CardHeader} from 'material-ui/Card';

class Dashboard extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            name: ''
        };
    }
    
    componentDidMount() {
        
        const tokenString = window.location.href.split('/')[4];
        var tokens = queryString.parse(tokenString);
        
        if(tokens !== null && localStorage.state === tokens.state) {
            localStorage.setItem('token', tokens.access_token);
        }
        
        // Working with the spotify api
        
        var Spotify = new spotifyWebAPI();
        
        Spotify.setAccessToken(tokens.access_token);
        
        // Get the authenticated user
        Spotify.getMe().then( data => {
            
            this.setState({name: data.body.display_name});
            console.log('Some information about the authenticated user', data.body);
            
            
        }, function(err) {
            console.log('Something went wrong!', err);
        });

    }
    
    render() {
        
        return (
            <div>
                <Card>
                    <CardHeader>
                        Info
                    </CardHeader>
                    <CardText>
                        {this.state.name}
                    </CardText>
                </Card>
            </div>
            );
    }
    
}

export default Dashboard;