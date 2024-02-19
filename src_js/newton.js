/**
 * newton.js
 * 
 * This p5.js sketch visualizes Newton's method for finding roots of a function.
 * Newton's method is an iterative numerical method that starts with an initial guess
 * and improves that guess with each iteration until it converges to a root of the function.
 * 
 * Global Variables:
 * - x: Initial guess for the root of the function.
 * - precision: The desired precision for the root.
 * - maxIterations: The maximum number of iterations to perform.
 * - iterations: The current number of iterations performed.
 * - animate: Boolean to control whether to animate the movement of the guess.
 * - nextX: The next guess for the root.
 * - coefficients: The coefficients of the polynomial function.
 * - scale: The scale of the graph.
 * 
 * Functions:
 * - setup(): Initializes the sketch, creates a canvas, sets the frame rate, generates random coefficients for the polynomial function, and adds a mousePressed event.
 * - draw(): Called continuously by p5.js. It checks if the function has a root, generates a new function if it doesn't, draws the axes, numbers on the axes, the function, and the tangent at the current guess, animates the movement of the guess, and applies Newton's method to find the next guess.
 * - hasRoot(): Checks if the function has a root by evaluating the function at many points in the interval [-2, 2] and checking if the absolute value of the function at any of these points is less than the desired precision.
 * - generateGraph(): Generates a new function by creating a new array of random coefficients. It then checks if the new function has a root and generates a new function if it doesn't.
 * - f(x): Evaluates the polynomial function at a given x value.
 * - df(x): Evaluates the derivative of the polynomial function at a given x value.
 */

let x = 2; // Initial guess
let precision = 0.00001; // Desired precision
let maxIterations = 100; // Maximum number of iterations
let iterations = 0; // Current number of iterations
let animate = false; // Whether to animate the movement of the guess
let nextX; // Next guess
let coefficients; // Coefficients of the polynomial function

function setup() {
  createCanvas(500, 500);
  frameRate(120); // Increase frame rate for smoother animation
  coefficients = new Array(3).fill().map(() => random(-1, 1)); // Generate random coefficients
  // Add mousePressed event to set the initial guess and reset the number of iterations and the animation
  mousePressed = () => {
    x = (mouseX - width / 2) / scale;
    iterations = 0;
    animate = false;
  };
}

let scale = 100; // Scale of the graph

function draw() {
  textSize(16);
  fill('black');

  if (!hasRoot()) {
    generateGraph();
  }

  background(255);
  // Draw axes
  stroke('black');
  line(0, height / 2, width, height / 2); // x-axis
  line(width / 2, 0, width / 2, height); // y-axis
  // Draw numbers on axes
  for (let i = -width / 2 / scale; i <= width / 2 / scale; i++) {
    text(i, i * scale + width / 2, height / 2 + 15);
  }
  for (let i = -height / 2 / scale; i <= height / 2 / scale; i++) {
    text(i, width / 2 + 5, -i * scale + height / 2);
  }
  // Draw function ( polynomial ) 
  for (let x = 0; x < width; x++) {
    let y = f((x - width / 2) / scale);
    point(x, height / 2 - y * scale);
  }
  // Draw tangent
  let y = f(x);
  let slope = df(x);
  stroke('red');
  line(x * scale + width / 2, height / 2 - y * scale, (x - y / slope) * scale + width / 2, height / 2);
  stroke('black');
  // Animate the movement of the guess
  fill('blue');
  ellipse(x * scale + width / 2, height / 2 - f(x) * scale, 10);
  fill('green');
  ellipse(nextX * scale + width / 2, height / 2 - f(nextX) * scale, 10);

  // draw a line from the end of the red line to the x axes to show where it's going to be
  stroke('red');
  line((x - y / slope) * scale + width / 2, height / 2, (x - y / slope) * scale + width / 2, height / 2 - y * scale);
  // Draw the x-axis
  stroke('black');
  line(0, height / 2 - y * scale, (x - y / slope) * scale + width / 2, height / 2 - y * scale);
  // Draw the y-axis
  line((x - y / slope) * scale + width / 2, height / 2 - y * scale, (x - y / slope) * scale + width / 2, height / 2);

  // Draw the x value
  text(x.toFixed(3), (x - y / slope) * scale + width / 2, height / 2 + 15);
  // Draw the y value
  text(y.toFixed(3), 5, (height / 2 - y * scale).toFixed(4));

  // Animate the movement of the guess
  if (animate) {
    x = lerp(x, nextX, 0.01); // Slow down the animation
    if (abs(x - nextX) < 0.01) {
      animate = false;
    }
  } else {
    // Apply Newton's method
    let y = f(x);
    let slope = df(x);
    nextX = x - y / slope;
    animate = true;
    iterations++;
    // Recursive call for next iteration
    if (iterations < maxIterations && abs(x - nextX) >= precision) {
      draw(); // Recursive call to continue the iteration
    }
  }

  text('Iterations: ' + iterations, 10, 30);
  textSize(20);
  fill('black');
  text("x1 = x0 - f(x0)/f'(x0)", 10, 60);
  text("where", 10, 80);
  text("x0 is the initial guess: " + x.toFixed(3), 10, 100);
  text("f(x0) is the value of the function at x0: " + f(x).toFixed(3), 10, 120);
  text("f'(x0) is the derivative of the function at x0: " + df(x).toFixed(3), 10, 140);
  text("x1 is the next guess: " + nextX.toFixed(3), 10, 160);
}

function hasRoot() {
  for (let x = -2; x <= 2; x += 0.01) {
    let y = f(x);
    if (abs(y) < precision) {
      return true;
    }
  }
  return false;
}

function generateGraph() {
  coefficients = new Array(3).fill().map(() => random(-1, 1));
  if (!hasRoot()) {
    generateGraph();
  }
}

// Function for which to find root
function f(x) {
  return coefficients.reduce((sum, a, i) => sum + a * pow(x, i), 0); // Evaluate polynomial at x
}

// Derivative of the function
function df(x) {
  return coefficients.slice(1).reduce((sum, a, i) => sum + (i + 1) * a * pow(x, i), 0); // Evaluate derivative at x
}
