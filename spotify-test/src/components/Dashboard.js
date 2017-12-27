import React, {Component} from 'react';
import queryString from 'query-string';
import spotifyWebAPI from 'spotify-web-api-node';

import {Card, CardHeader, CardTitle, CardMedia, CardText} from 'material-ui/Card';

function randomString(length) {
  var text = "";
  var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  for (var i = 0; i < length; i++)
    text += possible.charAt(Math.floor(Math.random() * possible.length));

  return text;
}

class Dashboard extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            totals: []
        };
    }
    
    componentDidMount() {
        
        const tokenString = window.location.href.split('/')[4];
        var tokens = queryString.parse(tokenString);
        
        if( tokens !== null && 
        localStorage.state === tokens.state /* && 
        parseInt(localStorage.getItem('token_exp')) > Date.now() */ ) {
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
            
            Spotify.getMyTopTracks({limit: 10, time_range: 'long_term'}).then( trackData => {
                
                var tracks = trackData.body.items.map( item => {
                    
                    var track = {
                        id: item.id,
                        name: item.name,
                        album: item.album.name,
                        artist: item.artists[0].name,
                        album_artwork: item.album.images[0].url,
                    }
                        
                    return track;
                }); 
                
                return tracks;
            }, function(err) {
                console.log(err);
            })
            .then( tracks => { 
                
                var trackIds = tracks.map( track => { return track.id });
                
                Spotify.getAudioFeaturesForTracks(trackIds).then( features => {
                    
                    var totals = [];

                    for(var i = 0; i < features.body.audio_features.length; i++) {
                        
                        var total = {
                            track: tracks[i],
                            feature: features.body.audio_features[i]
                        }
                        
                        totals.push(total);
                    }

                    this.setState({totals: totals});
                });
            })
            
        } // end of if checking for good tokens
    }
    
    render() {
        console.log(this.state.totals);
        
        var styles = {
            'margin' : '10px',
            'width' : '300px'
        };
        
        return (
            <div>
                <Card>
                    <CardTitle title={this.state.name.split(" ")[0] + "'s top tracks"} />
                    {this.state.totals.map( total => {
                        return (
                            <div style={styles} key={randomString(5)}>
                                <Card>
                                    <CardMedia
                                      overlay={<CardTitle title={total.track.name} 
                                      subtitle={total.track.artist} 
                                      />}
                                    >
                                      <img src={total.track.album_artwork} alt="" />
                                    </CardMedia>
                                </Card>
                            </div>
                        );
                    })}
                </Card>
            </div>
            );
    }
    
}

export default Dashboard;