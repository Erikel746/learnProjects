pub(crate) fn types() {
    let x: i32 = 2147483647;
    let y: i64 = 9223372036854775807;
    println!("Max Value of 32 is: {}", x);
    println!("Max Value of 64 is:{}", y);

    // Floats
    // f32, f64
    let pi = 3.1415926;
    println!("Pi is: {}", pi);

    //Boolean
    let is_snowing: bool = true;
    println!("Snowing is: {}", is_snowing);

    let letter: &str = "a";
    println!("letter: {}", letter);

    //Compound Data types
    // arrays, tuples, slices, strings

    //Array
    let numbers: [i32; 5] = [1, 2, 3, 4, 5];
    println!("Numbers are: {:?}", numbers);

    let fruits = ["apple", "apple", "banana"];
    println!("fruits are: {}", fruits[1]);

    //Tuples
    let human: (&str, i32, bool) = ("Alice", 43, true);
    println!("human: {}", human.0);
    println!("human: {:?}", human);

    let my_mix_tuple = ("My Tuple", 3.14, true, [1, 2, 3, 4]);
    println!("my_mix_tuple: {:?}", my_mix_tuple);

    //Slices: [1,2,3,4,5]
    let number_slices = &[1, 2, 3, 4, 5];
    println!("number_slices: {:?}", number_slices);

    let  animal_slices :&[&str] = &["Lion", "Elephant", "Tiger"];
    println!("animals_slices: {:?}", animal_slices);

    let books_slices :&[String] = &["IT".to_string(), "KAY".to_string()];
    println!("books_slices: {:?}", books_slices);
}
