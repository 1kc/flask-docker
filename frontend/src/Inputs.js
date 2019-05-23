import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import IconButton from '@material-ui/core/IconButton';
import AddCircle from '@material-ui/icons/AddCircle';
import axios from 'axios'

const styles = theme => ({
  input: {
    margin: theme.spacing.unit,
  },
});

// function Inputs(props) {

class Inputs extends React.Component {

  state = {
    l_value: '0',
    harmful: 'No',
    photo: 'photo.jpg',
  };

  handleChange = name => event => {
    this.setState({ [name]: event.target.value });
  };

  handleClick = event => {
    let data = {
      harmful: (this.state.harmful === 'True' ? true : false),
      l_value: parseFloat(this.state.l_value),
      photo: this.state.photo,

    }
    axios
      .post('/api/sample', data)
      .then(function (response) {
          //handle success
          console.log(response);
      })
      .catch(function (response) {
          //handle error
          console.log(response);
    });

    // TODO: fix this, this is bad
    window.location.reload()
  };

  render() {

    const { classes } = this.props;

    return (
      <div>
        <Input
          placeholder="L Value"
          className={classes.input}
          inputProps={{
            'aria-label': 'Description',
          }}
          onChange={this.handleChange('l_value')}
        />


        <Input
          placeholder="Detected Harmful"
          className={classes.input}
          inputProps={{
            'aria-label': 'Description',
          }}
          onChange={this.handleChange('harmful')}
        />

        <Input
          placeholder="Photo URL"
          className={classes.input}
          inputProps={{
            'aria-label': 'Description',
          }}
          onChange={this.handleChange('photo')}
        />

        <IconButton color="primary" 
          onClick={this.handleClick}
        >
          <AddCircle />
        </IconButton>

      </div>
    );
    }
}

export default withStyles(styles)(Inputs);
