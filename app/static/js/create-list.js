const container = document.getElementById("container");
const template = document.getElementById("template");


function clickHandler(event){
    event.target.append(" — Clicked this button");
}
function addInput(){
    const firstClone = template.content.firstElementChild.cloneNode(true);
    const block = document.createElement("div");
    const Delete = document.createElement("button");
    const firstDelete = document.querySelector(".first-delete");
    Delete.type = "button";
    Delete.textContent = "Delete";
    Delete.className = "btn btn-outline-light";
    const newLine = document.createElement("br");
    const bullet = document.createTextNode("• ");
    firstClone.addEventListener("click", clickHandler);
    block.appendChild(bullet);
    block.appendChild(firstClone);
    block.appendChild(Delete);
    block.appendChild(newLine);

    container.appendChild(block);

    Delete.addEventListener("click", function(){
        block.remove();
    });

    firstDelete.addEventListener("click", function(){
        firstDelete.remove();
    });
}
const addInputBtn = document.querySelector(".js-add-input-btn");
addInputBtn.addEventListener("click", addInput);