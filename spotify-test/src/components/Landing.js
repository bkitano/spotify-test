import React, { Component } from 'react';
import {Card, CardText} from 'material-ui/Card';

class Landing extends Component {
    
    render() {
        return (
            <div>
                <Card>
                    <CardText>
                        Is this thing on?
                    </CardText>
                </Card>
            </div>
            )
    }
}

export default Landing;