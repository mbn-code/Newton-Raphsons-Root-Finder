fn newton_raphson(f: fn(f64) -> f64, f_prime: fn(f64) -> f64, x: f64, epsilon: f64) -> f64 {
    let fx = f(x);
    if fx.abs() < epsilon {
        return x;
    }
    let fpx = f_prime(x);
    let next_x = x - fx / fpx;
    newton_raphson(f, f_prime, next_x, epsilon)
}

fn main() {
    
    let f = |x: f64| x.powi(5) + 3.5 * x.powi(4) - 2.5 * x.powi(3) - 12.5 * x.powi(2) + 1.5 * x + 9.0;
    let f_prime = |x: f64| 5.0 * x.powi(4) + 14.0 * x.powi(3) - 7.5 * x.powi(2) - 25.0 * x + 1.5;

    // Set the initial guess and epsilon
    let initial_guess = 4.0;
    let epsilon = 0.0001;

    // Call the Newton-Raphson method
    let root = newton_raphson(f, f_prime, initial_guess, epsilon);

    println!("Root: {}", root);
}
