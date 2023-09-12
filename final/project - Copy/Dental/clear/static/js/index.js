// Get references to the register and explore buttons
const registerButton = document.getElementById("registerButton");
const exploreButton = document.getElementById("exploreButton");

// Get a reference to the registration form
const registrationForm = document.querySelector(".registration-form");

// Function to show the registration form
function showRegistrationForm() {
    registrationForm.style.display = "block";
}

// Function to hide the registration form
function hideRegistrationForm() {
    registrationForm.style.display = "none";
}

// Event listeners for showing and hiding the registration form
registerButton.addEventListener("click", showRegistrationForm);
exploreButton.addEventListener("click", hideRegistrationForm);
