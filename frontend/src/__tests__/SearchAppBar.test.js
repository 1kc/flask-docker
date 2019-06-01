import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/react/cleanup-after-each';
import 'jest-dom/extend-expect';
import SearchAppBar from '../SearchAppBar';


it('Bar renders app name', () => {
  const { getByText } = render(<SearchAppBar />);
  expect(getByText('Grain Analysis')).toBeInTheDocument();
});
