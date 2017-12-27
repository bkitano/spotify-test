import React, {Component} from 'react';
import queryString from 'query-string';
import spotifyWebAPI from 'spotify-web-api-node';

import {Card, CardText, CardHeader} from 'material-ui/Card';

class Dashboard extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            a: 1
        };
    }
    
    componentDidMount() {
        
        const tokenString = window.location.href.split('/')[4];
        var tokens = queryString.parse(tokenString);
        
        console.log(tokens);
        
        if(tokens !== null && localStorage.state == tokens.state) {
            localStorage.setItem('token', tokens.access_token);
        }
        
        // Working with the spotify api
        
        var Spotify = new spotifyWebAPI();
        
        Spotify.setAccessToken(tokens.access_token);
        
        Spotify.getArtistAlbums('43ZHCT0cAZBISjO8DG9PnE')
            .then(function(data) {
            console.log('Artist albums', data.body);
            }, function(err) {
            console.error(err);
            });
    }
    
    render() {
        
        return (
            <div>
                <Card>
                    <CardHeader>
                        Token
                    </CardHeader>
                    <CardText>
                        {localStorage.getItem('token')}
                    </CardText>
                </Card>
            </div>
            );
    }
    
}

export default Dashboard;