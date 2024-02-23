import time
import openpyxl
import math
from newton_rec import newtonMethod

# Define your functions and their derivatives
functions = [
    { 
        'name': 'x^5+3.5x^4-2.5x^3-12.5x^2+1.5x+9',
        'f': lambda x: x**5+3.5*x**4-2.5*x**3-12.5*x**2+1.5*x+9, 
        'fDerivative': lambda x: 5*x**4+14*x**3-7.5*x**2-25*x+1.5 
    },
    {
        'name': 'sin(x)',
        'f': lambda x: math.sin(x),
        'fDerivative': lambda x: math.cos(x)
    },
    {
        'name': 'cos(x)',
        'f': lambda x: math.exp(x) - 1,
        'fDerivative': lambda x: math.exp(x)
    },
    {
        'name': 'x^2 - 4',
        'f': lambda x: x ** 2 - 4,
        'fDerivative': lambda x: 2 * x
    },
    {
        'name': 'x^3 - 2',
        'f': lambda x: x ** 3 - 2,
        'fDerivative': lambda x: 3 * x ** 2
    },
    {
        'name': 'x^4 - 16',
        'f': lambda x: x ** 4 - 16,
        'fDerivative': lambda x: 4 * x ** 3
    },
    {
        'name': 'x^5 - 32',
        'f': lambda x: x ** 5 - 32,
        'fDerivative': lambda x: 5 * x ** 4
    },
    {
        'name': 'x^6 - 64',
        'f': lambda x: x ** 6 - 64,
        'fDerivative': lambda x: 6 * x ** 5
    }
]

initialGuesses = [-4, 4] # Array of initial guesses
epsilon = 1e-10
numRuns = 10 # Number of runs

# Create a new workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = 'Benchmark Data'

# Add column headers
worksheet.append(['Function', 'Initial Guess', 'Time'])


for function in functions:
    for _ in range(numRuns):
        for x0 in initialGuesses: # Loop over initial guesses
            start = time.perf_counter()
            iterations = newtonMethod(function['f'], function['fDerivative'], x0, epsilon)
            end = time.perf_counter()
            elapsed_time = end - start

            # Add row to worksheet
            worksheet.append([function['name'], x0, elapsed_time])

# Save workbook to file
workbook.save('benchmark_data_python.xlsx')
print('Data written to file')
