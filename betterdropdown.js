
const hide = () => {
    const dropdown = document.getElementById("dropdown");
    dropdown.classList.remove("hide");
};



const inputLocation = document.querySelector("#inputBox");

const holder = document.createElement("div");
holder.innerHTML = "Bob";
holder.id = "dropdown";
holder.classList.add("structure");

inputLocation.appendChild(holder);

const inputBox = document.createElement("input");
inputBox.id = "Box";
inputBox.addEventListener("mousedown", hide);

inputLocation.appendChild(inputBox);


document.addEventListener("mousedown", function(event) {
    const dropdown = document.getElementById("dropdown");
    const clickObject = document.getElementById("Box");
    console.log(event.target);
    if (event.target !== clickObject) {
        // The object was not clicked
        console.log('Object not clicked');
        // Perform actions here, e.g., hide a menu, reset a state, etc.
      
    if (!dropdown.classList.contains("hide")) {
        dropdown.classList.add("hide");
      }
    }

});
