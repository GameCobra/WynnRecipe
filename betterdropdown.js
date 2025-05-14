
const hide = () => {
    const dropdown = document.querySelector(".structure");
    if (dropdown.classList.contains("hide")) {
        dropdown.classList.remove("hide");
      }
};


document.addEventListener("click", function(event) {
    const dropdown = document.querySelector(".structure");
    if (event.target !== dropdown) {
        // The object was not clicked
        console.log('Object not clicked');
        // Perform actions here, e.g., hide a menu, reset a state, etc.
      
    if (!dropdown.classList.contains("hide")) {
        dropdown.classList.add("hide");
      }
    }

});


const inputLocation = document.querySelector("#inputBox");

const holder = document.createElement("div");
holder.innerHTML = "Bob";
holder.classList.add("structure");

const inputBox = document.createElement("input");
inputBox.id = "Box";
inputBox.addEventListener("click", drop(event));

inputLocation.appendChild(inputBox);
inputLocation.appendChild(holder);

