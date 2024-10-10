document.addEventListener('DOMContentLoaded', (event) => {
    const rows = document.querySelectorAll('tr');
    rows.forEach(row => {
        row.addEventListener('click', () => {
            const url = row.getAttribute('data-href');
            if (url) {
                window.location.href = url;
            }
        });
    });
});
