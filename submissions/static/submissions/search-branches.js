document.addEventListener('DOMContentLoaded', () => {
    
    const allBranches = document.querySelectorAll('.branch');

    document.querySelector('#search').addEventListener('input', (event) => search(event.target.value, allBranches));
    
});


const search = (input, allBranches) => {
    
    const filteredArray = [...allBranches].filter(element => element.children[0].children[0].innerHTML.includes(input));
    
    let searchResults = '';

    filteredArray.forEach( (element) => searchResults += element.outerHTML );

    document.querySelector('#branch-list').innerHTML = searchResults;
}