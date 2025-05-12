function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}

function notMyFunction() {
    document.getElementById("demo").innerHTML = "Paragraph NOT changed.";
}
/*
onclick = function(e){
    console.log("mouse location:", e.clientX, e.clientY)
  }
*/

function parseIngredients()
{
    fetch('https://gamecobra.github.io/wynncraft-crafter/ingredients.json')
    .then((response) => response.json())
    .then((json) => console.log(json));
    //const obj = JSON.parse(text);
}