let x = 2;  // Initial guess
let precision = 0.00001;  // Desired precision
let maxIterations = 100;  // Maximum number of iterations
let iterations = 0;  // Current number of iterations
let animate = false;  // Whether to animate the movement of the guess
let nextX;  // Next guess
let coefficients;  // Coefficients of the polynomial function

function setup() {
    createCanvas(500, 500);
    frameRate(240);  // Increase frame rate for smoother animation
    coefficients = new Array(3).fill().map(() => random(-1, 1));  // Generate random coefficients
}

let scale = 100;  // Scale of the graph

function draw() {

    textSize(16);
    fill('black');
    text('Root: ' + x.toFixed(2), 10, 20);

    let hasRoot = false;
    for (let x = -2; x <= 2; x += 0.01) {
        let y = f(x);
        if (abs(y) < precision) {
            hasRoot = true;
            break;
        }
    }

    if (!hasRoot) {
        // If there is no root, generate new random coefficients
        coefficients = new Array(3).fill().map(() => random(-1, 1));
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
    if (animate) {
        x = lerp(x, nextX, 0.05);
        if (abs(x - nextX) < 0.01) {
            animate = false;
        }
    } else {
        // Apply Newton's method
        nextX = x - y / slope;
        animate = true;
        iterations++;
        if (isNaN(y) || !isFinite(y) || abs(y) < precision || iterations > maxIterations) {
            x = random(-2, 2);  // Reset initial guess
            iterations = 0;  // Reset number of iterations
            coefficients = new Array(3).fill().map(() => random(-1, 1));  // Generate new random coefficients
        }
    }
}



// Function for which to find root
function f(x) {
    return coefficients.reduce((sum, a, i) => sum + a * pow(x, i), 0);  // Evaluate polynomial at x
}

// Derivative of the function
function df(x) {
    return coefficients.slice(1).reduce((sum, a, i) => sum + (i + 1) * a * pow(x, i), 0);  // Evaluate derivative at x
}