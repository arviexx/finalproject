// date.js

function validateDate(date, dateNote) {
    const selectedDate = new Date(date);

    if (selectedDate.getDay() === 0) {
        dateNote.innerText = 'Appointments are not available on Sundays';
        return false;
    } else {
        dateNote.innerText = '';
        return true;
    }
}
