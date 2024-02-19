# Newton's Method Visualization

## Overview

`newton.js` is a p5.js sketch that visually demonstrates Newton's method for finding roots of a function. Newton's method is an iterative numerical technique used to approximate the roots of a real-valued function.

## Features

- **Interactive Visualization**: Users can interact with the sketch by setting the initial guess for the root of the function by clicking on the canvas.
- **Dynamic Graph**: The sketch dynamically generates and updates the graph of the function and its tangent at the current guess.
- **Animation**: The movement of the guess towards the root is animated, providing a visual representation of Newton's method.
- **Precision Control**: Users can specify the desired precision for the root and the maximum number of iterations to perform.

## Global Variables

- **x**: Initial guess for the root of the function.
- **precision**: The desired precision for the root.
- **maxIterations**: The maximum number of iterations to perform.
- **iterations**: The current number of iterations performed.
- **animate**: Boolean to control whether to animate the movement of the guess.
- **nextX**: The next guess for the root.
- **coefficients**: The coefficients of the polynomial function.
- **scale**: The scale of the graph.

## Functions

- **setup()**: Initializes the sketch, creates a canvas, sets the frame rate, generates random coefficients for the polynomial function, and adds a `mousePressed` event to set the initial guess.
- **draw()**: Called continuously by p5.js. It checks if the function has a root, generates a new function if it doesn't, draws the axes, numbers on the axes, the function, the tangent at the current guess, animates the movement of the guess, and applies Newton's method to find the next guess.
- **hasRoot()**: Checks if the function has a root by evaluating the function at many points in the interval [-2, 2] and checking if the absolute value of the function at any of these points is less than the desired precision.
- **generateGraph()**: Generates a new function by creating a new array of random coefficients. It then checks if the new function has a root and generates a new function if it doesn't.
- **f(x)**: Evaluates the polynomial function at a given x value.
- **df(x)**: Evaluates the derivative of the polynomial function at a given x value.

## Usage

Simply open the `index.html` file in a web browser to view and interact with the visualization. Click on the canvas to set the initial guess for the root of the function.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

This visualization was created using the p5.js library. Special thanks to the p5.js community for their contributions and support.

For any questions or feedback, please contact [author's email].