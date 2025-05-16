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

//Will remove an object from existing temporaraly (will move other elements)
function HideElement(element)
{
    if (!element.classList.contains("hide")) {
        element.classList.add("hide");
    }
}

//Adds a removed (hiden) element back into existence
function ShowElement(element)
{
    element.classList.remove("hide");
}

//Makes an invisible element visible
function UnDisapearElement(element)
{
    element.classList.remove("disapear");
}

//Makes an element invisible (wont move other elements)
function DisapearElement(element)
{
    if (!element.classList.contains("disapear")) {
        element.classList.add("disapear");
    }
}

function textupdateInputEvent(Event)
{
    textupdate(Event.target);
}

function textupdate(element)
{
    let noResults = true;
    const dropdownObject = GetFirstChildWithClass(element.parentElement, "SearchDropdown");
    for (let i = 0; i < dropdownObject.children.length - 1; i++)
    {
        if (dropdownObject.children[i].innerHTML.toLowerCase().includes(element.value.toLowerCase()))
        {
            UnDisapearElement(dropdownObject.children[i]);
            noResults = false;
        }
        else
        {
            DisapearElement(dropdownObject.children[i]);
        }
    }
    if (noResults == true)
    {
        UnDisapearElement(dropdownObject.children[dropdownObject.children.length - 1]);
    }
    else
    {
        DisapearElement(dropdownObject.children[dropdownObject.children.length - 1]);
    }
}


async function parseIngredients() {
    let response = await fetch('https://gamecobra.github.io/WynnRecipe/optimizableProperties.json');
    let data = await response.json(); 
    return data; 
}

function CreatePropertyInputBox()
{
    const inputBox = document.createElement("input");
    inputBox.id = "InputBox";
    inputBox.classList.add("IngredientInputBox")
    inputBox.addEventListener("input", textupdateInputEvent);
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
    
    for (let i = 0; i < response.Properties.length; i++) {
    
        const element = document.createElement("button");
        element.innerHTML = response.Properties[i][0];
        element.classList.add("dropdown");
        element.onclick = function(Event) {SearchDropdownElementClicked(Event)};
        holder.appendChild(element);
        }
        const noResults = document.createElement("div");
        noResults.innerHTML = "No Results";
        noResults.classList.add("dropdown");
        DisapearElement(noResults);
        holder.appendChild(noResults);
    });
    return holder;
}

function SearchDropdownElementClicked(Event)
{
    const inputBox = GetFirstChildWithClass(Event.target.parentElement.parentElement, "IngredientInputBox") 
    inputBox.value = Event.target.innerHTML;
    textupdate(inputBox);
}

function CreateWholeSearchObject(inputLocation)
{
    inputLocation.appendChild(CreatePropertyInputBox());


    inputLocation.appendChild(CreateSearchDropdown());
}

CreateWholeSearchObject(document.querySelector("#ItemSelector"));
CreateWholeSearchObject(document.querySelector("#ItemSelector2"));