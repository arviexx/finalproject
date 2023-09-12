
    document.addEventListener("DOMContentLoaded", function () {
        const form = document.querySelector("form");
        const usernameInput = document.querySelector("#Username");
        const emailInput = document.querySelector("#Email");
        const passwordInput = document.querySelector("#Password");
        const confirmPasswordInput = document.querySelector("#password");

        form.addEventListener("submit", function (event) {
            if (usernameInput.value.trim() === "" || emailInput.value.trim() === "" || passwordInput.value.trim() === "" || confirmPasswordInput.value.trim() === "") {
                event.preventDefault(); // Prevent form submission
                alert("Please fill out all required fields.");
            }
        });
    })

    function validateForm() {
        const password = document.getElementById("Password").value;
        const confirmPassword = document.getElementById("password").value; // Use the correct ID
        const passwordError = document.getElementById("passwordError");
        const successMessage = document.getElementById("successMessage");

        if (password !== confirmPassword) {
            passwordError.innerHTML = "Passwords do not match. Please try again.";
            passwordError.style.display = "block";
            successMessage.style.display = "none"
            return false;
        } else {
            passwordError.style.display = "none";
            successMessage.style.display = "block";
            setTimeout(function() {
                window.location.href = "{% url 'loginuser' %}";
            }, 9000);
            return true;
        }
    }



    