const newtonMethod = require('./newton_rec'); // adjust the path to your newtonMethod function

// Define your functions and their derivatives
const functions = [
    {
        f: x => x ** 5 + 3.5 * x ** 4 - 2.5 * x ** 3 - 12.5 * x ** 2 + 1.5 * x + 9,
        fDerivative: x => 5 * x ** 4 + 14 * x ** 3 - 7.5 * x ** 2 - 25 * x + 1.5
    },
    {
        f: x => Math.sin(x),
        fDerivative: x => Math.cos(x)
    },
    {
        f: x => Math.exp(x) - 1,
        fDerivative: x => Math.exp(x)
    },
    {
        f: x => x ** 2 - 4,
        fDerivative: x => 2 * x
    }
];

const x0 = 4;
const epsilon = 1e-10;

for (let i = 0; i < functions.length; i++) {
    console.time(`Function ${i + 1}`);
    newtonMethod(functions[i].f, functions[i].fDerivative, x0, epsilon);
    console.timeEnd(`Function ${i + 1}`);
    console.log("Time for function", i + 1, "is over.");
}