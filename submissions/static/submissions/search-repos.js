document.addEventListener('DOMContentLoaded', () => {
    
    const allRepos = document.querySelectorAll('.repo');

    document.querySelector('#search').addEventListener('input', (event) => search(event.target.value, allRepos));
    
});


const search = (input, allRepos) => {
    
    const filteredArray = [...allRepos].filter(element => element.children[0].children[0].innerHTML.includes(input));

    let searchResults = '';

    filteredArray.forEach( (element) => searchResults += element.outerHTML );
   
    document.querySelector('#repo-list').innerHTML = searchResults;
}