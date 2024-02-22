const ExcelJS = require('exceljs');
const newtonMethod = require('./newton_rec'); // adjust the path to your newtonMethod function

// Define your functions and their derivatives
const functions = [
    { 
        f: x => x**5+3.5*x**4-2.5*x**3-12.5*x**2+1.5*x+9, 
        fDerivative: x => 5*x**4+14*x**3-7.5*x**2-25*x+1.5 
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
    },
    {
        f: x => x ** 3 - 2,
        fDerivative: x => 3 * x ** 2
    },
    {
        f: x => x ** 4 - 16,
        fDerivative: x => 4 * x ** 3
    },
    {
        f: x => x ** 5 - 32,
        fDerivative: x => 5 * x ** 4
    },
    {
        f: x => x ** 6 - 64,
        fDerivative: x => 6 * x ** 5
    }
];

const x0 = 2;
const epsilon = 1e-10;

// Create a new workbook and worksheet
let workbook = new ExcelJS.Workbook();
let worksheet = workbook.addWorksheet('Benchmark Data');

// Add column headers
worksheet.columns = [
    { header: 'Function', key: 'function' },
    { header: 'Time', key: 'time' }
];

for (let i = 0; i < functions.length; i++) {
    const start = process.hrtime();
    newtonMethod(functions[i].f, functions[i].fDerivative, x0, epsilon);
    const diff = process.hrtime(start);

    // Convert time to milliseconds
    const time = diff[0] * 1e3 + diff[1] * 1e-6;

    // Add row to worksheet
    worksheet.addRow({ function: `Function ${i+1}`, time: time });
}

// Write workbook to file
workbook.xlsx.writeFile('benchmark_data.xlsx')
    .then(() => console.log('Data written to file'))
    .catch(err => console.error(err));