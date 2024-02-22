
function newtonMethod(f, fDerivative, x0, epsilon) {
  const fx = f(x0); // definer vores function ved start punkt x0
  const fpx = fDerivative(x0); 
  
  if (Math.abs(fx) < epsilon) { // hvis den absolutte værdi af fx er mindre end epsilon, så har vi fundet en rod
    console.log("Root found:", x0);
    return x0; // så retunere vi og printer
  }
  
  const x1 = x0 - fx / fpx; // ellers laver vi en ny gæt x1
  // Det gør vi ved at trække fx / fpx fra x0 for at få et nyt gæt x1. Dette nye gæt opnås ved at finde x-afsnittet af tangentlinjen.
  
  console.log("Current guess:", x0);
  console.log("New guess:", x1);
  
  return newtonMethod(f, fDerivative, x1, epsilon); // Recursive call
  // Til sidst laver vi et rekursivt kald til newtonMethod med det nye gæt x1, og gentager processen, indtil vi finder en rod.
}


newtonMethod(
  x => x**5+3.5*x**4-2.5*x**3-12.5*x**2+1.5*x+9,
  x => 5*x**4+14*x**3-7.5*x**2-25*x+1.5,
  4,
  1e-10
);


module.exports = newtonMethod; 

  /*
Newton's method, also known as Newton-Raphson method, is an iterative numerical method used to find the roots of a given function. It is based on the idea of using the tangent line to approximate the root of the function.

The method starts with an initial guess, denoted as x0. It then iteratively refines this guess to get closer to the actual root of the function. Here's how it works:

Evaluate the function f(x) and its derivative f'(x) at the current guess x0.
Calculate the value of f(x0) divided by f'(x0), which gives us the slope of the tangent line at x0.
Subtract this value from x0 to get a new guess x1. This new guess is obtained by finding the x-intercept of the tangent line.
Repeat steps 1-3 until the absolute value of f(x) is less than a specified tolerance (epsilon). This indicates that we have found a root within the desired accuracy.
In the provided code, the newtonMethod function implements this iterative process. It takes four parameters:

f: The function for which we want to find the root.
fDerivative: The derivative of the function.
x0: The initial guess for the root.
epsilon: The tolerance value that determines when to stop iterating.
Inside the function, it calculates the value of the function and its derivative at the current guess (fx and fpx respectively). If the absolute value of fx is less than epsilon, it means a root has been found and the function returns the current guess.

Otherwise, it calculates a new guess x1 by subtracting fx / fpx from x0. It then prints the current guess and the new guess using console.log.

Finally, the function makes a recursive call to newtonMethod with the new guess x1, repeating the process until a root is found.

Note that Newton's method may not always converge to a root, especially if the initial guess is far from the actual root or if the function has multiple roots in the vicinity of the initial guess. It is also important to choose an appropriate tolerance value to balance accuracy and computational efficiency.
*/