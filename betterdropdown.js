function GetFirstChildWithClass(element, className)
{
    const collection = element.children;
    for (let i = 0; i < collection.length; i++)
    {
        if (collection[i].classList.contains(className))
        {
            return collection[i];
        }
    }
    return null;
}

//Triggers when the document is clicked 
const onDocumentClick = (Event) => {
    //const dropdown = document.getElementById("dropdown");
    //const clickObject = document.getElementById("InputBox");
    
    const collection = document.getElementsByClassName("SearchDropdown");
    for (let i = 0; i < collection.length; i++)
    {
        if (Event.target !== collection[i] && Event.target !== GetFirstChildWithClass(collection[i].parentElement, "IngredientInputBox")) {
            hide(collection[i]);
        }
    }

};

function trueHide()
{
    const collection = document.getElementsByClassName("SearchDropdown");
    //const dropdown = document.getElementById("dropdown");
    for (let i = 0; i < collection.length; i++)
    {
        hide(collection[i]);
    }
}

function hide(element)
{
    if (!element.classList.contains("hide")) {
        element.classList.add("hide");
    }
}

const ShowElement = (element) => {
    element.classList.remove("hide");
};

function textupdate(Event)
{
    //const box = document.getElementById("InputBox");
    //console.log(Event.target.value);
    for (let i = 0; i < Event.target.parentElement.children.length; i++)
    {
        if (Event.target.parentElement.children[i].classList.contains("SearchDropdown"))
        {
            ShowElement(Event.target.parentElement.children[i]);
        }
    }
    if (Event.target.classList.contains("IngredientInputBox") && Event.target.value == "")
    {
        trueHide();
    }
        
}


async function parseIngredients() {
    let response = await fetch('https://gamecobra.github.io/WynnRecipe/ingredients.json');
    let data = await response.json(); 
    return data; 
}

function CreatePropertyInputBox()
{
    const inputBox = document.createElement("input");
    inputBox.id = "InputBox";
    inputBox.classList.add("IngredientInputBox")
    inputBox.addEventListener("mousedown", textupdate);
    inputBox.addEventListener("input", textupdate);
    return inputBox;
}

const inputLocation = document.querySelector("#ItemSelector");

inputLocation.appendChild(CreatePropertyInputBox());

const holder = document.createElement("div");
holder.id = "dropdown";
holder.classList.add("SearchDropdown")
holder.classList.add("structure");

const ings = parseIngredients().then(
response => {

    for (let i = 0; i < response.ingredients.length; i++) {

    const Person = document.createElement("div");
    Person.innerHTML = response.ingredients[i].name;
    Person.classList.remove("hide");
    holder.appendChild(Person);
    }
});


inputLocation.appendChild(holder);



document.getElementById("InputBox").value = "Johnny Bravo";

document.addEventListener("mousedown", onDocumentClick);

