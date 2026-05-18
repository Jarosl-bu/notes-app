const container = document.getElementById("container");
const template = document.getElementById("template");

function clickHandler(event){
    event.target.append(" — Clicked this button");
}

function addInput(){
    const firstClone = template.content.firstElementChild.cloneNode(true);

    const block = document.createElement("div");
    block.className = "first-delete";

    const bullet = document.createElement("span");
    bullet.textContent = "• ";

    const Delete = document.createElement("button");
    Delete.type = "button";
    Delete.textContent = "Delete";
    Delete.className = "btn btn-outline-light";

    /*const newLine = document.createElement("br");*/

    block.appendChild(bullet);
    block.appendChild(firstClone);
    block.appendChild(Delete);
    /*block.appendChild(newLine);*/

    container.appendChild(block);

    Delete.addEventListener("click", function(){
        block.remove();
    });
}

const addInputBtn = document.querySelector(".js-add-input-btn");
addInputBtn.addEventListener("click", addInput);

document.querySelectorAll(".js-first-delete-btn").forEach(btn => {
    btn.addEventListener("click", function () {
        btn.parentElement.remove();
    });
});