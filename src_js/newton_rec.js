function newtonMethod(f, fPrime, x0, epsilon) {
  const fx = f(x0);
  const fpx = fPrime(x0);
  
  if (Math.abs(fx) < epsilon) {
    return x0;
  }
  
  const x1 = x0 - fx / fpx;
  
  return newtonMethod(f, fPrime, x1, epsilon);
}
