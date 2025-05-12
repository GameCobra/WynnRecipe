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

async function parseIngredients()
{
    let x = await fetch('https://gamecobra.github.io/wynncraft-crafter/ingredients.json');
    //fetch('https://gamecobra.github.io/wynncraft-crafter/ingredients.json')
    //.then((response) => response.json())
    //.then((json) => obj = json);
    //obj = JSON.parse(response);
    console.log(JSON.parse(x).ingredients[0].name);
}