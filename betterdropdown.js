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
        element.classList.add("hide"); //Hide CSS element removes object from affecting elements
    }
}

//Adds a removed (hiden) element back into existence
function ShowElement(element)
{
    element.classList.remove("hide");
}

//Makes an element invisible (wont move other elements)
function DisapearElement(element)
{
    if (!element.classList.contains("disapear")) {
        element.classList.add("disapear"); //Disapear CSS element removes an object from being displayed
    }
}

//Makes an invisible element visible
function UnDisapearElement(element)
{
    element.classList.remove("disapear"); 
}

//Update search element requires an HTML element input to be compatable with being called from other functions
//But input needs an event object if you want the target
//This function just converts the event element to target and calls the appropriet function
function UpdateSearchElementsEventInput(Event)
{
    UpdateSearchElements(Event.target);
}

//Removes elements from the search autocomleat dropdown based on the current text in the search box
function UpdateSearchElements(element)
{
    let numOfResults = 0;
    const dropdownObject = GetFirstChildWithClass(element.parentElement, "SearchDropdown");
    for (let i = 0; i < dropdownObject.children.length - 1; i++)
    {
        if (dropdownObject.children[i].innerHTML.toLowerCase().includes(element.value.toLowerCase()))
        {
            UnDisapearElement(dropdownObject.children[i]);
            numOfResults += 1;
        }
        else
        {
            DisapearElement(dropdownObject.children[i]);
        }
    }
    if (numOfResults == 0)
    {
        UnDisapearElement(dropdownObject.children[dropdownObject.children.length - 1]);
    }
    else
    {
        DisapearElement(dropdownObject.children[dropdownObject.children.length - 1]);
    }
    var rootCSS = document.querySelector(':root');
    rootCSS.style.setProperty("--dropdownDisplaySize", Math.min(200, 60 * Math.max(1, numOfResults)) + "px");
}

//Webpage causes error if directly trying to get the JSOn from its local files, so will just directly pull it with this instead
//Should work identicaly when viewed on github
async function GetItemProperties() {
    let response = await fetch('https://gamecobra.github.io/WynnRecipe/optimizableProperties.json');
    let data = await response.json(); 
    return data; 
}

function CreatePropertyInputBox()
{
    const inputBox = document.createElement("input");
    inputBox.id = "InputBox";
    inputBox.classList.add("IngredientInputBox")
    inputBox.addEventListener("input", UpdateSearchElementsEventInput);
    //inputBox.value = "default value";
    inputBox.placeholder = "Enter value";
    return inputBox;
}

function AddPropertyElementsToDropDown(holderElement)
{
    const ings = GetItemProperties().then(
    response => {
    
    for (let i = 0; i < response.Properties.length; i++) {
    
        const element = document.createElement("button");
        element.innerHTML = response.Properties[i][0];
        element.classList.add("dropdown");
        element.onclick = function(Event) {SearchDropdownElementClicked(Event)};
        holderElement.appendChild(element);
        }
        const noResults = document.createElement("button");
        noResults.innerHTML = "No Results";
        noResults.classList.add("dropdown");
        DisapearElement(noResults);
        holderElement.appendChild(noResults);
    });
}

function CreateSearchDropdown()
{

    const holder = document.createElement("div");
    holder.id = "dropdown";
    holder.classList.add("SearchDropdown")
    holder.classList.add("structure");
    holder.classList.add("dropdown");
    
    AddPropertyElementsToDropDown(holder);
    return holder;
}

function SearchDropdownElementClicked(Event)
{
    const inputBox = GetFirstChildWithClass(Event.target.parentElement.parentElement, "IngredientInputBox") 
    inputBox.value = Event.target.innerHTML;
    UpdateSearchElements(inputBox);
}

function CreateWholeSearchObject(inputLocation)
{
    inputLocation.appendChild(CreatePropertyInputBox());


    inputLocation.appendChild(CreateSearchDropdown());
}

CreateWholeSearchObject(document.querySelector("#ItemSelector"));
CreateWholeSearchObject(document.querySelector("#ItemSelector2"));