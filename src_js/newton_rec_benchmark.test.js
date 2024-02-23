const ExcelJS = require('exceljs');
const newtonMethod = require('./newton_rec'); // adjust the path to your newtonMethod function

// Define your functions and their derivatives
const functions = [
    { 
        name: 'x^5+3.5x^4-2.5x^3-12.5x^2+1.5x+9',
        f: x => x**5+3.5*x**4-2.5*x**3-12.5*x**2+1.5*x+9, 
        fDerivative: x => 5*x**4+14*x**3-7.5*x**2-25*x+1.5 
    },
    {
        name: 'sin(x)',
        f: x => Math.sin(x),
        fDerivative: x => Math.cos(x)
    },
    {
        name: 'cos(x)',
        f: x => Math.exp(x) - 1,
        fDerivative: x => Math.exp(x)
    },
    {
        name: 'x^2 - 4',
        f: x => x ** 2 - 4,
        fDerivative: x => 2 * x
    },
    {
        name: 'x^3 - 2',
        f: x => x ** 3 - 2,
        fDerivative: x => 3 * x ** 2
    },
    {
        name: 'x^4 - 16',
        f: x => x ** 4 - 16,
        fDerivative: x => 4 * x ** 3
    },
    {
        name: 'x^5 - 32',
        f: x => x ** 5 - 32,
        fDerivative: x => 5 * x ** 4
    },
    {
        name: 'x^6 - 64',
        f: x => x ** 6 - 64,
        fDerivative: x => 6 * x ** 5
    }
];

const initialGuesses = [-4, 4]; // Array of initial guesses
const epsilon = 1e-10;
const numRuns = 10; // Number of runs

// Create a new workbook and worksheet
let workbook = new ExcelJS.Workbook();
let worksheet = workbook.addWorksheet('Benchmark Data');

// Add column headers
worksheet.columns = [
  { header: 'Function', key: 'function' },
  { header: 'Initial Guess', key: 'initial_guess' }, // New column for initial guess
  { header: 'Time', key: 'time' },
];

for (let i = 0; i < functions.length; i++) {
  for (let j = 0; j < numRuns; j++) {
    for (let k = 0; k < initialGuesses.length; k++) { // Loop over initial guesses
      const x0 = initialGuesses[k];
      const start = process.hrtime();
      const iterations = newtonMethod(functions[i].f, functions[i].fDerivative, x0, epsilon); // Assume newtonMethod returns the number of iterations
      const diff = process.hrtime(start);

      // Convert time to milliseconds
      const time = diff[0] * 1e3 + diff[1] * 1e-6;

      // Add row to worksheet
      worksheet.addRow({ function: functions[i].name, initial_guess: x0, time: time }); // Add initial guess to the row
    }
  }
}

// Write workbook to file
workbook.xlsx.writeFile('../src_python/benchmark_data_javascript.xlsx')
  .then(() => console.log('Data written to file'))
  .catch(err => console.error(err));