document.addEventListener('DOMContentLoaded', () => {
    
    document.querySelectorAll('.commit').forEach((element) => is_submitted(element));
    
});

const is_submitted = (commit) => {

    const commitParsed = commit.id.split('/');
    const repo_owner = commitParsed[0];
    const repo_name = commitParsed[1];
    const branch_name = commitParsed[2];
    const commit_name = commitParsed[3];

    fetch(`/${repo_owner}/${repo_name}/${branch_name}/${commit_name}`, { method: 'GET'})
        .then(response => response.json())
        .then(result => {
            
            commit.innerHTML = `${(result.submitted) ? '✅' : '❔'}` 
            console.log(result.submitted)
    })
}