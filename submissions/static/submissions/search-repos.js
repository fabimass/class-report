document.addEventListener('DOMContentLoaded', () => {
    
    const allRepos = document.querySelectorAll('.repo');

    document.querySelector('#search').addEventListener('input', (event) => search(event.target.value, allRepos));
    
});


const search = (input, allRepos) => {
    
    const filteredArray = [...allRepos].filter(element => element.innerHTML.includes(input));

    let searchResults = '';

    filteredArray.forEach( (element) => searchResults += `<div><h4>📂<a class="text-info repo" href="${element.href}">${element.innerHTML}</a></h4></div>`);
   
    document.querySelector('#repo-list').innerHTML = searchResults;
}