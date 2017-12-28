import React, {Component} from 'react';
import queryString from 'query-string';

class Graph extends Component {
    
    constructor(props) {
        super(props);
        
        this.state = {
            features: queryString.parse(this.props.features)
        }
    }
    
    render() {
        return (
            <div>
                asdfasdfasdf
            </div>
            )
    }
}

export default Graph;