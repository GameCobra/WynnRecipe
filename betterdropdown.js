const hide = (Event) => {
    const dropdown = document.getElementById("dropdown");
    const clickObject = document.getElementById("Box");
    console.log(Event.target);
    if (Event.target !== clickObject) {
        // The object was not clicked
        //console.log('Object not clicked');
        trueHide();
    }

};

function trueHide()
{
    if (!dropdown.classList.contains("hide")) {
        dropdown.classList.add("hide");
    }
}

const show = () => {
    const dropdown = document.getElementById("dropdown");
    dropdown.classList.remove("hide");
};

function textupdate()
{
    const box = document.getElementById("Box");
    console.log(box.value);
    show();
    if (box.value == "")
    {
        trueHide();
    }
        
}


const inputLocation = document.querySelector("#inputBox");


const inputBox = document.createElement("input");
inputBox.id = "Box";
inputBox.addEventListener("mousedown", textupdate);
inputBox.addEventListener("input", textupdate)

inputLocation.appendChild(inputBox);

const holder = document.createElement("div");
holder.innerHTML = "Bob";
holder.id = "dropdown";
holder.classList.add("structure");

inputLocation.appendChild(holder);


document.getElementById("Box").value = "Johnny Bravo";

document.addEventListener("mousedown", hide);

