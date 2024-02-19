let x = 2;  // Initial guess
let precision = 0.00001;  // Desired precision
let maxIterations = 100;  // Maximum number of iterations
let iterations = 0;  // Current number of iterations
let animate = false;  // Whether to animate the movement of the guess
let nextX;  // Next guess
let coefficients;  // Coefficients of the polynomial function

function setup() {
    createCanvas(1000, 1000);
    frameRate(240);  // Increase frame rate for smoother animation
    coefficients = new Array(3).fill().map(() => random(-1, 1));  // Generate random coefficients
}

let scale = 100;  // Scale of the graph

function draw() {
    textSize(16);
    fill('black');


    if (!hasRoot()) {
        generateGraph();
    }

    background(255);
    // Draw axes
    stroke('black');
    line(0, height / 2, width, height / 2);  // x-axis
    line(width / 2, 0, width / 2, height);  // y-axis
    // Draw numbers on axes
    for (let i = -width / 2 / scale; i <= width / 2 / scale; i++) {
        text(i, i * scale + width / 2, height / 2 + 15);
    }
    for (let i = -height / 2 / scale; i <= height / 2 / scale; i++) {
        text(i, width / 2 + 5, -i * scale + height / 2);
    }
    // Draw function
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

    // draw a line from the end of the red line to the x axies to show where it's going to be
    stroke('red');
    line((x - y / slope) * scale + width / 2, height / 2, (x - y / slope) * scale + width / 2, height / 2 - y * scale);
    // Draw the x axis
    stroke('black');
    line(0, height / 2 - y * scale, (x - y / slope) * scale + width / 2, height / 2 - y * scale);
    // Draw the y axis
    line((x - y / slope) * scale + width / 2, height / 2 - y * scale, (x - y / slope) * scale + width / 2, height / 2);
   

    // Draw the x value
    text(x.toFixed(5), (x - y / slope) * scale + width / 2, height / 2 + 15);
    // Draw the y value
    text(y.toFixed(5), 5, (height / 2 - y * scale).toFixed(4));
    


    // Animate the movement of the guess
    if (animate) {
        x = lerp(x, nextX, 0.01);  // Slow down the animation
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
    }
    text('Iterations: ' + iterations, 10, 30);
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
}

// Function for which to find root
function f(x) {
    return coefficients.reduce((sum, a, i) => sum + a * pow(x, i), 0);  // Evaluate polynomial at x
}

// Derivative of the function
function df(x) {
    return coefficients.slice(1).reduce((sum, a, i) => sum + (i + 1) * a * pow(x, i), 0);  // Evaluate derivative at x
}