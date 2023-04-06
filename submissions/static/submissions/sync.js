document.addEventListener('DOMContentLoaded', () => {
    
    document.querySelector('#sync').addEventListener('click', sync);
    
});


const sync = () => {
    
    fetch("/sync", {
        method: 'POST',
        headers: {
            "X-CSRFToken": CSRF_TOKEN
        }
    })
}