def newtonMethod(f, fDerivative, x0, epsilon):
    fx = f(x0)  # Definerer vores funktion ved startpunktet x0
    fpx = fDerivative(x0) # Definerer vores afledede funktion ved startpunktet x0

    if abs(fx) < epsilon:  # Hvis den absolutte værdi af fx er mindre end epsilon, så har vi fundet en rod
        print("Rod fundet:", x0)
        return x0  # Så returnerer vi og printer

    x1 = x0 - fx / fpx  # Ellers laver vi et nyt gæt x1
    # Dette gør vi ved at trække fx / fpx fra x0 for at få et nyt gæt x1. Dette nye gæt opnås ved at finde x-afsnittet af tangentlinjen.

    return newtonMethod(f, fDerivative, x1, epsilon)  # Rekursivt kald

# Den givne funktion og dens afledede
def f(x):
    return x**5 + 3.5*x**4 - 2.5*x**3 - 12.5*x**2 + 1.5*x + 9

def fDerivative(x):
    return 5*x**4 + 14*x**3 - 7.5*x**2 - 25*x + 1.5

newtonMethod(f, fDerivative, 4, 1e-10)
