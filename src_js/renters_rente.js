let fib = [0, 1];  // Fibonacci sequence
let n = 1;  // Index of the current term
let dir = 0;  // Direction of the rectangle (0 = right, 1 = down, 2 = left, 3 = up)

function setup() {
    createCanvas(800, 800);
    frameRate(1);  // Draw one frame per second
}

function draw() {
    background(255);
    translate(width / 2, height / 2);  // Move origin to center of canvas
    rotate(-HALF_PI);  // Rotate coordinate system by -90 degrees
    let x = 0, y = 0;  // Starting position
    for (let i = 0; i < n; i++) {
        rect(x, y, fib[i], fib[i]);
        // Move to the next position
        if (dir % 4 === 0) {
            x += fib[i];
        } else if (dir % 4 === 1) {
            y += fib[i];
            x -= fib[i - 1];
        } else if (dir % 4 === 2) {
            x -= fib[i + 1];
            y -= fib[i - 1];
        } else if (dir % 4 === 3) {
            y -= fib[i + 1];
        }
        dir++;  // Change direction
    }
    // Add the next term to the Fibonacci sequence
    fib.push(fib[n] + fib[n - 1]);
    n++;
}