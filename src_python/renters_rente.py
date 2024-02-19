import matplotlib.pyplot as plt

def compound_interest_recursive(P, r, n, t):
    if t == 0:
        return P
    else:
        return compound_interest_recursive(P, r, n, t-1) * (1 + r/n)

def compound_interest_iterative(P, r, n, t):
    A = P
    for _ in range(t):
        A *= (1 + r/n)
    return A

def compound_interest_recursive_with_tax_and_inflation(P, r, n, t, tax_rate, inflation_rate):
    if t == 0:
        return P
    else:
        A = compound_interest_recursive_with_tax_and_inflation(P, r, n, t-1, tax_rate, inflation_rate)
        interest = A * r/n
        A += interest * (1 - tax_rate)
        A /= (1 + inflation_rate)
        return A

def compound_interest_iterative_with_tax_and_inflation(P, r, n, t, tax_rate, inflation_rate):
    A = P
    for _ in range(t):
        interest = A * r/n
        A += interest * (1 - tax_rate)
        A /= (1 + inflation_rate)
    return A

def visualize_compound_interest(P, r, n, t, tax_rate, inflation_rate):
    # Calculate the compound interest for each year
    values_recursive = [compound_interest_recursive_with_tax_and_inflation(P, r, n, year, tax_rate, inflation_rate) for year in range(t+1)]
    values_iterative = [compound_interest_iterative_with_tax_and_inflation(P, r, n, year, tax_rate, inflation_rate) for year in range(t+1)]

    # Create a line plot of the compound interest over time
    plt.plot(range(t+1), values_recursive, label='Recursive')
    plt.plot(range(t+1), values_iterative, label='Iterative')

    # Add labels and title
    plt.xlabel('Years')
    plt.ylabel('Amount')
    plt.title('Compound Interest Over Time')
    plt.legend()

    # Show the plot
    plt.show()

# Call the function with example parameters
visualize_compound_interest(1000, 0.05, 1, 10, 0.2, 0.02)