mod types;

fn main() {
    hello_world();
    tell_number(43);
    human_id("John", 18, 132);

    let _x: i32 = {
        let price: i32 = 5;
        let qty: i32 = 5;
        price * qty
    };
    println!("Result is:{:?}", _x);
    println!("BMI={:.2}", calculate_bmi(1.84, 80.4));
}
fn hello_world() {
    println!("Hello, world!");
}

fn tell_number(number: i8) {
    println!("Tell number! {}", number );
}

fn human_id(name: &str, age: i8, height: i16) {
    println!("Human id: My name is: {}, My name is: {}, My height is: {}", name, age, height );

}

fn calculate_bmi(height: f32, weight: f32) -> f32 {

    weight / (height * height)
}

