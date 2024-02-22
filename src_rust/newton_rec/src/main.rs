fn newtonRaphson(fx, fdx, x0, epsilon){
    // recursion base case
    fx = fx(x0);
    fpx = fdx(x0);

    if (abs(fx) < epsilon){
        println!("Root is: {}", x0);
        return x0;
    }
    else{
        x1 = x0 - fx/fpx;
        return newtonRaphson(fx, fdx, x1, epsilon);
    }
}


for i in 0..=10 {
    fn main() {
        newtonRaphson(
            |x| x.powi(2) - 2,
            |x| 2*x,
            1.0,
            1e-5
        );
    }
}