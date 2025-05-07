function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}

function notMyFunction() {
    document.getElementById("demo").innerHTML = "Paragraph NOT changed.";
}

function Person(first = "a", last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
}

const TestPerson = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    eyeColor: "blue"
};

function newPerson()
{
    const mySelf = new Person(last="Too", age=22, eye="green");
    const test = new CreateIngreadientObject();
    test.firstName = "jim";
    document.getElementById("demo").innerHTML = test.firstName;
}

function CreateIngreadientObject() {
    this.firstName;
}