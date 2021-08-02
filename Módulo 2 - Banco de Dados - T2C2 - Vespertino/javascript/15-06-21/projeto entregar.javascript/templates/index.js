const dados ={
    nome: "Popeye",
    idade: "120",
    sorrindo: true,
    imagem: "https://i.gifer.com/1sC.gif",
    imagem2: "https://blogopod.com/image/2009/popeye-vs-johnny-bravo.jpg",
}
const elementoNome = document.getElementById('nome');
const elementoIdade = document.getElementById('idade');

elementoNome.innerText = dados.nome;
elementoIdade.innerText = dados.idade;

function atualizarHumor () {
    const elementoImagem = document.getElementById('imagem');
    const humor = document.getElementById('humor');

    if (dados.sorrindo){
        elementoImagem.src = dados.imagem;
        humor.innerText = "Popeye hoje comeu espinafre! ";
    } else{

        elementoImagem.src = dados.imagem2;
        humor.innerText = "Olivia saiu e até agora não voltou!";
    }
}

atualizarHumor ();

const botaoOutroVersao = document.getElementById('outroVersao');
botaoOutroVersao.addEventListener ('click', function () {
    dados.sorrindo = !dados.sorrindo;
    atualizarHumor();
});