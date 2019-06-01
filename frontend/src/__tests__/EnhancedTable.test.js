import React from 'react';
import ReactDOM from 'react-dom';
import EnhancedTable from '../EnhancedTable';

it('EnhancedTable renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<EnhancedTable />, div);
  ReactDOM.unmountComponentAtNode(div);
});
