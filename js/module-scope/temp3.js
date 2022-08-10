(function func() {
  var a = 1;

  function foo() {
    console.log('a in required module = ', a);
  }
})()

a = 2;

foo();

console.log('a in current module = ', a);