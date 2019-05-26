import React from 'react';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import SearchAppBar from './SearchAppBar';
import EnhancedTable from './EnhancedTable';
import './App.css';


const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#FFB300'
    },
  },
});

class App extends React.Component {

  render() {
    return (
      <MuiThemeProvider theme={theme}>
      <div className="App">
        <SearchAppBar />
        <EnhancedTable />
      </div>
      </MuiThemeProvider>
    );
  }

}

export default App;
