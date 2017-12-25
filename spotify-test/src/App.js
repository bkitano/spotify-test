import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {
  Route,
  Navlink,
  HashRouter
} from 'react-router-dom';

import Landing from './components/Landing';

class App extends Component {
  render() {
    return (
      <div className="App">
        <HashRouter>
          <MuiThemeProvider>
            <div className='container'>
              <Route path='/' component={Landing} />
            </div>
          </MuiThemeProvider>
        </HashRouter>
      </div>
    );
  }
}

export default App;
