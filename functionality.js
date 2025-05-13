function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}

function notMyFunction() {
    document.getElementById("ingredient").innerHTML = "<option value='7'>7</option><option value='B'>B</option><option value='C'>C</option>";
}
/*
onclick = function(e){
    console.log("mouse location:", e.clientX, e.clientY)
  }
*/

async function parseIngredients() {
    let response = await fetch('https://gamecobra.github.io/wynncraft-crafter/ingredients.json');
    let data = await response.json(); 
    console.log(data.ingredients[0].name); 
}