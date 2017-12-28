import React, {Component} from 'react';
import queryString from 'query-string';

import {Card, CardMedia, CardTitle} from 'material-ui/Card';

class Song extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
            total: this.props.totalString
        }
    }
    
    render() {
        
        var total = queryString.parse(this.state.total);
        var parsedTotal = {};
        parsedTotal.features = queryString.parse(total.features);
        parsedTotal.track = queryString.parse(total.track);
        
        return (
            <Card>
                <CardMedia
                  overlay={<CardTitle title={parsedTotal.track.name} 
                  subtitle={parsedTotal.track.artist} 
                  />}
                >
                  <img src={parsedTotal.track.album_artwork} alt="" />
                </CardMedia>
            </Card>
            )
    }
}

export default Song;