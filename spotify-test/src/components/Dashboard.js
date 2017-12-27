import React, {Component} from 'react';
import queryString from 'query-string';
import spotifyWebAPI from 'spotify-web-api-node';

import {Card, CardHeader, CardTitle} from 'material-ui/Card';

class Dashboard extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            tracks: []
        };
    }
    
    componentDidMount() {
        
        const tokenString = window.location.href.split('/')[4];
        var tokens = queryString.parse(tokenString);
        
        if(tokens !== null && localStorage.state === tokens.state) {
            localStorage.setItem('token', tokens.access_token);
        
            // Working with the spotify api
            
            var Spotify = new spotifyWebAPI();
            
            Spotify.setAccessToken(tokens.access_token);
            
            // Get the authenticated user
            Spotify.getMe().then( data => {
                
                this.setState({name: data.body.display_name});
                
            }, function(err) {
                console.log('Something went wrong!', err);
            });
            
            Spotify.getMyTopTracks({limit: 10, time_range: 'long_term'}).then( data => {

                data.body.items.map( item => {
                    
                    var track = {
                        name: item.name,
                        album: item.album.name,
                        artist: item.artists[0].name,
                        album_artwork: item.album.images[1].url
                    };
                    
                    this.state.tracks.push(track);

                    return null;
                });
                
            }, function(err) {
                console.log(err);
            })
            
        }
    }
    
    render() {
        
        return (
            <div>
                <Card>
                <CardTitle title={this.state.name.split(" ")[0] + "\'s top tracks"} />
                {this.state.tracks.map( track => {
                    return (
                        <Card>
                            <CardHeader 
                                title={track.name}
                                subtitle={track.artist}
                                avatar={track.album_artwork} />
                        </Card>
                    );
                })}
                </Card>
            </div>
            );
    }
    
}

export default Dashboard;