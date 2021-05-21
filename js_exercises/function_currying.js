function sum(a, b) {
  return parseInt(a) + parseInt(b);
}


function infiniteCall(fn) {
  return function curriedFn(...args) { // gets array with prev arg
    return function (...args2) { // gets the array with later arg
      if(args2.length < 1) return args.reduce(fn); // if there are no later arg then print the final result
      return curriedFn(...args, args2)// if there are args then add it to existing args array
    }
  };
}
console.log(infiniteCall(sum)(2, 4,5)(3)(4, 6)(5)());
