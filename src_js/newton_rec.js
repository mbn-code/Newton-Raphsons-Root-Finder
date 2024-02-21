function newtonMethod(f, fDerivative, x0, epsilon) {
  const fx = f(x0);
  const fpx = fDerivative(x0);
  
  if (Math.abs(fx) < epsilon) {
    console.log("Root found:", x0);
    return x0;
  }
  
  const x1 = x0 - fx / fpx;
  
  console.log("Current guess:", x0);
  console.log("New guess:", x1);
  
  return newtonMethod(f, fDerivative, x1, epsilon); // Recursive call
}

newtonMethod(
  x => x**5+3.5*x**4-2.5*x**3-12.5*x**2+1.5*x+9,
  x => 5*x**4+14*x**3-7.5*x**2-25*x+1.5,
  4,
  1e-10
);
