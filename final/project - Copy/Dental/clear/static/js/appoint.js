<script>
    const dateInput = document.getElementById('date');
    const dateNote = document.getElementById('dateNote');

    dateInput.addEventListener('change', () => {
        const selectedDate = new Date(dateInput.value);
        const dayOfWeek = selectedDate.getDay(); // 0 for Sunday, 1 for Monday, and so on

        if (dayOfWeek === 0) {
            dateNote.textContent = 'Not available day';
        } else {
            dateNote.textContent = '';
        }
    });
</script>
