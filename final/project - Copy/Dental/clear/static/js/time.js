// time.js

function validateTime(time, timeNote) {
    const [hours, minutes] = time.split(':').map(Number);

    if (hours < 8 || (hours === 17 && minutes !== 0) || hours > 17) {
        timeNote.innerText = 'Appointments are only available between 8:00 am and 5:00 pm';
        return false;
    } else {
        timeNote.innerText = '';
        return true;
    }
}
