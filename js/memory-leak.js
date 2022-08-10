console.log('Node Global Before', global);

function foo() {
  bar = 'text'

  // Process something on 'bar'

  bar = null
}

foo()

console.log('Node Global After', global);

// Anything that's directly referenced as a property of 'global' NodeJS root would 
// never be GCed.

// Solns :

// 1. Use Strict mode of JS
// 2. Use Arrow function (but it isn't the ideal solution)