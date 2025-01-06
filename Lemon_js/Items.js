const React = require('react');

function ItemList({ items }) {
  return React.createElement(
    'ul',
    null,
    items.map((item, index) =>
      React.createElement('li', { key: index }, item)
    )
  );
}

module.exports = ItemList;