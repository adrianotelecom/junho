const express = require("express");
const app = express();
const port = 3000;


const creperia = [

    "Pizza",
    "Crepes",
    "Sanduiches",
    "Açai",
    "Suco",
    "Cremes",
    "Jantinha",
    "Espetinhos",
    "Porções"];

app.get('/',(req,res) =>{

    resp.send('SEJA BEM VINDO!');
});

app.get('/creperia',(req,res) =>{

    resp.send(creperia);
});

//[GET] - /creperiA{id} - Retorna um único filme

app.get("/creperia/:id",(req,res) =>{

    const id = req.params.id-1;

    const creperias = creperia[id];

    

    if(!creperia){
        return res.send("No momento não servimos esse item.");

    }
    res.send(creperias);
});

app.listen(port,()=>{

    console.info(`App rodando em:http://localhost:${port}`);
});