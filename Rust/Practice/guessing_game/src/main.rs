//LEFT OFF AT PG 36

extern crate rand;

use std::io;
use rand::Rng;
use std::cmp::Ordering;
// import standard library

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1,
101);

    println!("The secret number is: {}", secret_number)
;

    println!("Please input your guess.");

    let mut guess = String::new();
    // allows the variable guess to be mutable with "mut"

    io::stdin().read_line(&mut guess)
    // uses the std library for io input
    .expect("Failed to read line");

    println!("You guessed: {}", guess);

    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
}
