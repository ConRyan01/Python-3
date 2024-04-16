import { useState } from 'react';

function MyButton() {

  function handleClick() {
    alert('You Clicked Me!');
  }

  return (
    <button onClick={handleClick}>
      I'm a button
    </button>
  );
}

function Button2() {
  return (
    <button>THIS IS A TEST</button>
  )
}

const user = {
  name: 'Space Marine',
  imageUrl: 'https://images3.alphacoders.com/133/thumbbig-1338125.webp',
};

const products = [
  { title: 'Cabbage', isFruit: false, id: 1 },
  { title: 'Garlic', isFruit: false, id: 2 },
  { title: 'Apple', isFruit: true, id: 3 },
];

export default function MyApp() {

  const listItems = products.map(product =>
    <li
      key={product.id}
    >
      {product.title}
    </li>
  );

  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
      <Button2 />
      <h1>{user.name}</h1>
      <img
        src={user.imageUrl}
        alt={'Photo of ' + user.name}
      />
      <ul>{listItems}</ul>
    </div>
    
  );
}
