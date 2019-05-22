import React from 'react';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import SearchAppBar from './SearchAppBar';
import EnhancedTable from './EnhancedTable';
import axios from 'axios'
import './App.css';


const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#FFB300'
    },
  },
});

class App extends React.Component {

  state = {
    sample: []
  };

  componentDidMount() {
    axios
      .get(`/api/sample`)
      .then(response => {
        this.setState((state, props) => ({sample: response.data}));
        /*
        // create an array of contacts only with relevant data
        const newContacts = response.data.map(c => {
          return {
            id: c.id,
            name: c.name
          };
        });

        // create a new "State" object without mutating 
        // the original State object. 
        const newState = Object.assign({}, this.state, {
          contacts: newContacts
        });

        // store the new state object in the component's state
        this.setState(newState);
        */

      })
      .catch(error => console.log(error));
  }

  render() {
    return (
      <MuiThemeProvider theme={theme}>
      <div className="App">
        <SearchAppBar />
        <Grid container spacing={24} justify="center">
  
          <Grid item xs={8}>
            <EnhancedTable sample={this.state.sample}/>
          </Grid>
        </Grid>
      </div>
      </MuiThemeProvider>
    );
  }

}

export default App;
