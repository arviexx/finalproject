// appointment.js

document.addEventListener('DOMContentLoaded', () => {
    const appointmentForm = document.getElementById('appointmentForm');
    const timeNote = document.getElementById('timeNote');
    const dateNote = document.getElementById('dateNote');
    const successMessage = document.getElementById('successMessage');
    const popupMessage = document.getElementById('popupMessage');

    // Initialize warning messages to empty strings
    timeNote.innerText = '';
    dateNote.innerText = '';

    appointmentForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = {
            fullName: document.getElementById('fullName').value,
            age: document.getElementById('age').value,
            date: document.getElementById('date').value,
            time: document.getElementById('time').value,
            address: document.getElementById('address').value,
            phoneNumber: document.getElementById('phoneNumber').value,
            services: Array.from(document.querySelectorAll('input[name="service"]:checked')).map(input => input.value),
            doctorChoice: document.querySelector('input[name="doctorChoice"]:checked').value,
        };

        // Validate time, date, and submit the form
        const isTimeValid = validateTime(formData.time, timeNote);
        const isDateValid = validateDate(formData.date, dateNote);

        if (isTimeValid && isDateValid) {
            submitForm(formData, successMessage, popupMessage);
        }
    });
});
