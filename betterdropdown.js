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

function HideElement(element)
{
    if (!element.classList.contains("hide")) {
        element.classList.add("hide");
    }
}


function ShowElement(element)
{
    element.classList.remove("hide");
}


function UnDisapearElement(element)
{
    element.classList.remove("disapear");
}

function DisapearElement(element)
{
    if (!element.classList.contains("disapear")) {
        element.classList.add("disapear");
    }
}

function textupdate(Event)
{
    const dropdownObject = GetFirstChildWithClass(Event.target.parentElement, "SearchDropdown");
    for (let i = 0; i < dropdownObject.children.length; i++)
    {
        if (dropdownObject.children[i].innerHTML.toLowerCase().includes(Event.target.value.toLowerCase()))
        {
            UnDisapearElement(dropdownObject.children[i]);
        }
        else
        {
            DisapearElement(dropdownObject.children[i]);
        }
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
    inputBox.addEventListener("input", textupdate);
    //inputBox.value = "default value";
    inputBox.placeholder = "Enter value";
    return inputBox;
}

function CreateSearchDropdown()
{

    const holder = document.createElement("div");
    holder.id = "dropdown";
    holder.classList.add("SearchDropdown")
    holder.classList.add("structure");
    holder.classList.add("dropdown")
    
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