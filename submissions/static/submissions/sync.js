document.addEventListener('DOMContentLoaded', () => {
    
    document.querySelector('#sync').addEventListener('click', (event) => sync(event.target));
    
});


const sync = (button) => {
    
    button.innerHTML = '<div class="spinner-border spinner-border-sm text-light" role="status"><span class="sr-only">Loading...</span></div>'

    fetch("/sync", {
        method: 'POST',
        headers: {
            "X-CSRFToken": CSRF_TOKEN
        }
    })
    .then(() => location.reload())
    
}