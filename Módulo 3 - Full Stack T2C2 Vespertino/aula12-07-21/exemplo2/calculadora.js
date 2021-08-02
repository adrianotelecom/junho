const nome = 'Kalkuladora versão 1.0'

function soma(a, b) {

    return a + b
}

function sub(a, b) {

    return a - b
}

function mult(a, b) {

    return a * b
}

function div(a, b) {
    
    return a / b
}

module.exportes = {

    soma,
    sub,
    mult,
    div,
    nome,
};