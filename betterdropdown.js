//Based on: https://medium.com/@kyleducharme/developing-custom-dropdowns-with-vanilla-js-css-in-under-5-minutes-e94a953cee75  
function GetFirstChildWithClass(element, className)
{
    const childrenList = element.children;

    //will find the first element in childrenList with the given class and returns it
    for (let i = 0; i < childrenList.length; i++)
    {
        if (childrenList[i].classList.contains(className))
        {
            return childrenList[i];
        }
    }
    return null;
}

const onDocumentClick = (Event) => {
    //const dropdown = document.getElementById("dropdown");
    //const clickObject = document.getElementById("InputBox");
    
    const collection = document.getElementsByClassName("SearchDropdown");
    for (let i = 0; i < collection.length; i++)
    {
        //hides all collection elements that were not clicked and did not have their input box clicked
        if (Event.target !== collection[i] && Event.target !== GetFirstChildWithClass(collection[i].parentElement, "IngredientInputBox")) {
            HideElement(collection[i]);
        }
    }
};

function HideAllSearchDropdowns()
{
    const collection = document.getElementsByClassName("SearchDropdown");
    for (let i = 0; i < collection.length; i++)
    {
        HideElement(collection[i]);
    }
}

function HideElement(element)
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
    const drop = GetFirstChildWithClass(Event.target.parentElement, "SearchDropdown");
    console.log(Event.target);
    if (drop !== null)
    {
        ShowElement(drop);
    }
    if (Event.target.classList.contains("IngredientInputBox") && Event.target.value == "")
    {
        HideElement(drop);
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
    //inputBox.addEventListener("mousedown", textupdate);
    //inputBox.addEventListener("input", textupdate);
    inputBox.value = "default value";
    return inputBox;
}

function CreateSearchDropdown()
{

    const holder = document.createElement("div");
    holder.id = "dropdown";
    holder.classList.add("SearchDropdown")
    holder.classList.add("structure");
    holder.classList.add("dropdown")
    //holder.classList.add("hide");
    
    const ings = parseIngredients().then(
    response => {
    
        for (let i = 0; i < response.ingredients.length; i++) {
    
        const Person = document.createElement("div");
        Person.innerHTML = response.ingredients[i].name;
        Person.classList.add("dropdown")
        holder.appendChild(Person);
        }
    });
    return holder;
}

function CreateWholeSearchObject(inputLocation)
{
    inputLocation.appendChild(CreatePropertyInputBox());


    inputLocation.appendChild(CreateSearchDropdown());
}

CreateWholeSearchObject(document.querySelector("#ItemSelector"));
CreateWholeSearchObject(document.querySelector("#ItemSelector2"));


//document.addEventListener("mousedown", onDocumentClick);