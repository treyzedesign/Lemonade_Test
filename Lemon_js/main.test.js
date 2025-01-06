const React = require('react');
const { render, screen } = require('@testing-library/react');
const ItemList = require('./Items');

test('renders correct number of items', () => {
  const items = ['Item 1', 'Item 2', 'Item 3'];
  
  // Render the ItemList component with the items prop
  render(React.createElement(ItemList, { items }));

  // Select all the list items rendered by the component
  const renderedItems = screen.getAllByRole('listitem');
  expect(renderedItems.length).toBe(items.length);
});