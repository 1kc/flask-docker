import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import Input from '@material-ui/core/Input';
import IconButton from '@material-ui/core/IconButton';
import AddCircle from '@material-ui/icons/AddCircle';

const styles = theme => ({
  input: {
    margin: theme.spacing.unit,
  },
});

// function Inputs(props) {

const Inputs = (props) => {

  const { classes } = props;

  return (
    <form onSubmit={props.handleSubmit}>
      <Input
        type="text"
        placeholder="L Value"
        className={classes.input}
        onChange={props.handleChange('l_value')}
      />


      <Input
        type="text"
        placeholder="Detected Harmful"
        className={classes.input}
        onChange={props.handleChange('harmful')}
      />

      <Input
        type="text"
        placeholder="Photo URL"
        className={classes.input}
        onChange={props.handleChange('photo')}
      />

      <IconButton color="primary" 
        type="submit"
      >
        <AddCircle />
      </IconButton>

    </form>
  );
}

export default withStyles(styles)(Inputs);
