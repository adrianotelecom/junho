const objeto = {
    'globin': 3,
    'orc': 5,
    'feiticeira': 7,
};

const potenciaDaFaca = {
    'soco': 1,
    'arco': 3,
    'espada': 5,
};

let LugarDoObjeto;
let lugarDaArma;

function iniciar() {
    const lugares = document.getElementsByClassName('lugar');

    for (const lugar of lugares) {
        lugar.addEventListener('click', marcarLugarBatalha);
    }

    document.getElementById('calcular').addEventListener('click', calcularEstrago);
}

function marcarLugarBatalha(evento) {
    const lugarBatalha = evento.target.parentElement;
    if (!lugarBatalha.classList.contains('lugar')) {
        return;
    }
    const idLugarBatalha = lugarBatalha.getAttribute('id');
    if (lugarBatalha.classList.contains('objeto')) {
        LugarDoObjeto = idLugarBatalha;
        limparLugares('objeto')
    } else {
        lugarDaArma = idLugarBatalha;
        limparLugares('faca');
    }
    lugarBatalha.classList.add('batalha')
}

function calcularEstrago() {
    if (!LugarDoObjeto || !lugarDaArma) {
        alert('Ou se você quer brincar vamos escolher alguma coisa né!');
        return;
    }
    const estragoCausar = verEstrago();
    const estragoPotenciaDaFaca = potenciaDaFaca [lugarDaArma];
    const estragoGeral = estragoCausar + estragoPotenciaDaFaca;
    const fileObjeto = objeto[LugarDoObjeto];

    let resultado = "Estrago:" + estragoGeral + '!';
    if (estragoGeral >= fileObjeto) {
        resultado += 'Olha consegui colocar ele(a) pra repousar:' + LugarDoObjeto
    } else {
        resultado += 'Você tera que comer mais Feijão, e volte a tentar...';
    }

    document.getElementById('estrago').innerHTML = resultado;
}

function limparLugares(tipo) {
    const lugares = document.getElementsByClassName('lugar');
    
    for (const lugar of lugares) {
        if (lugar.classList.contains(tipo)) {
            lugar.classList.remove('batalha')
        }
    }
}

function verEstrago() {
    const min = Math.ceil(1);
    const max = Math.floor(10);

    return Math.floor(Math.random() * (max - min + 1)) + min;
}