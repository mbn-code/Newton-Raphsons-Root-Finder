function setup() {
    createCanvas(800, 600);
    background(0);
    noLoop();
}

function draw() {
    background(0);
    fill(255);
    sierpinski(width / 2, height / 2, width / 2);
}

function sierpinski(x, y, d) {
    if (d > 10) {
        sierpinski(x, y, d / 2);
        sierpinski(x - d / 2, y + d / 2, d / 2);
        sierpinski(x + d / 2, y + d / 2, d / 2);
    } else {
        triangle(x, y - d / 2, x - d / 2, y + d / 2, x + d / 2, y + d / 2);
    }
}