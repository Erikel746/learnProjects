mod types;

fn main() {
    hello_world();
    tell_number(43);
    types::types()
}
fn hello_world() {
    println!("Hello, world!");
}

fn tell_number(number: i8) {
    println!("Tell number! {}", number );
}