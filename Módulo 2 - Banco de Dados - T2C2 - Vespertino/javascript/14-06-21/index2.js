const botao = document.querySelector(".wrapper-button #botao");

function botaoFoiClicado(){

alert("você clicou no botão!!!.");
}

botao.addEventListener("Click", botaoFoiClicado);
botao.innerHTML = "Clique aqui!";