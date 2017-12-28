import React, {Component} from 'react';
import queryString from 'query-string';
import ReactAudioPlayer from 'react-audio-player';

import {Card, CardMedia, CardTitle} from 'material-ui/Card';

import Player from './Player';

class Song extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            total: this.props.totalString,
            play: false
        }
    }
    
     onToggle(e) {
        this.setState({play: !this.state.play});
        if(this.state.play) {
            this.audio.pause();
        } else {
            this.audio.play();
        }
    }
    
    render() {
        
        var style_imageOne = {
            'position': 'absolute',
            'z-index': '0'
        }
        
        var style_imageTwo = {
            'position': 'absolute',
            'width': '100px',
            'z-index': '1'
        }
        
        var style_container = {
            'position': 'relative'
        }

        var total = queryString.parse(this.state.total);
        var parsedTotal = {};
        parsedTotal.features = queryString.parse(total.features);
        parsedTotal.track = queryString.parse(total.track);
        
        return (
            <div style={style_container}>
                <div style={style_imageOne} onClick={e => this.onToggle(e)} className={!this.state.play ? "icon ion-play" : "icon ion-pause"} />
                <img style={style_imageTwo} src={parsedTotal.track.album_artwork} alt="" />
                <audio src={this.props.preview_url} ref={(audio) => { this.audio = audio }}/>
            </div>
            )
    }
}

export default Song;