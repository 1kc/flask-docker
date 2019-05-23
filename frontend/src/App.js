import React from 'react';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import SearchAppBar from './SearchAppBar';
import EnhancedTable from './EnhancedTable';
import Inputs from './Inputs';
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
      })
      .catch(error => console.log(error));
  }

  render() {
    return (
      <MuiThemeProvider theme={theme}>
      <div className="App">
        <SearchAppBar />
        <Grid container spacing={8} justify="center">


          <Grid item xs={8}>
            <br />
            <Paper>
              <Inputs />
            </Paper>
          </Grid>

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
