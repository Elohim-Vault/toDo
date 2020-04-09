var deleteBtn = document.getElementsByClassName('delete-btn')
var searchBtn = document.getElementById('search-btn')
var searchForm = document.getElementById('search-form')
var urlPadrao = 'http://127.0.0.1:8000/'
var filter = document.getElementById('filter')

console.log(filter.value)

// console.log(deleteBtn)
// console.log(deleteBtn[0])


for (var c = 0; c < deleteBtn.length; c++){
    link = deleteBtn[c].href
    deleteBtn[c].addEventListener("click", function (e){
        e.preventDefault()
        result = confirm('Você tem certeza que deseja excluir essa tarefa?')

        if (result){
            window.location.href = link
        }
    })
}

searchBtn.addEventListener("click", function (){
    searchForm.submit()
})

filter.addEventListener('change', function(){
    console.log(filter.value)
    window.location.href = urlPadrao + '?filter=' + filter.value
})