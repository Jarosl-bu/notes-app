/*index*/
const btnCreateNote = document.getElementById("btn-create-note");
const btnCreateList = document.getElementById("btn-create-list");

btnCreateNote.addEventListener("click", function(){
    window.location.href="/notes/create-note"
});

btnCreateList.addEventListener("click", function(){
    window.location.href="/notes/create-list"
});


