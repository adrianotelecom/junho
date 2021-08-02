const calculadora = require('./calculadora') //ECMA 5

//import calculadora from './calculadora'; //ECMA 6

console.log(calculadora.soma(8,10));

console.log(calculadora.sub(20,5));

console.log(calculadora.mult(2,4));

console.log(calculadora.div(10,2));

console.log(calculadora.nome);

calculadora.nome = "Calculadora do Molina";

console.log(calculadora.nome);