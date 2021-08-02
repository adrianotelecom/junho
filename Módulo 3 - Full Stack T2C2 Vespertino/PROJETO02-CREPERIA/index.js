const { json} = request
const { request } = require("express");
const express = require("express");
const app = express();
const port = 3000;
app.use(express.json());


//Transformando em uma lista de objetos
const creperia = [
    {   id:1,
        nome:"Pizza",
        imagemUrl: 'https://blog.praticabr.com/wp-content/uploads/2019/06/Pizza-Pizzaria-Forno-Forza-Express.jpg'
    },

    {   id:2,
        nome:"Crepes",
        imagemUrl: 'https://img.itdg.com.br/tdg/images/recipes/000/057/368/278486/278486_original.jpg?mode=crop&width=710&height=400'
    },

    {   id:3,
        nome:"Sanduiches",
        imagemUrl: 'https://i1.wp.com/3talheres.com.br/wp-content/uploads/2019/11/Dupla-Bob%E2%80%99s-traz-4-novos-sandu%C3%ADches-para-o-Bob%E2%80%99s.jpg?fit=850%2C600&ssl=1'
    },

    {   id:4,
        nome:"Açai",
        imagemUrl: 'https://mapadasfranquias.com.br/wp-content/uploads/2020/12/acaidabarramesa.jpg'
    },

    {   id:5,
        nome:"Suco",
        imagemUrl: 'https://img.riomarevoce.com/salvadornorteonline/2020/07/Suco-Natural-da-Fruta.-Viva-Gula.jpg'
    },

    {   id:6,
        nome:"Cremes",
        imagemUrl: 'https://www.guiadasemana.com.br/contentFiles/system/pictures/2012/3/44331/original/pe-no-parque-01.jpg'
    },

    {   id:7,
        nome:"Jantinha",
        imagemUrl: 'https://uploads.emaisgoias.com.br/2021/02/pedir-jantinha-em-goiania_capa.jpg'
    },

    {   id:8,
        nome:"Espetinhos",
        imagemUrl: 'https://i.pinimg.com/564x/80/9e/8c/809e8c4570870c00ac589cb3fb534266.jpg'
    },

    {   id:9,
        nome:"Porções",
        imagemUrl: 'http://www.lollos.com.br/uploads/produtos/1440440334.png'
    },
    
    
    ];

const getCreperiaValidos = () =>creperia.filter(Boolean);
const getCreperiabyID = id => getCreperiaValidos ().find(creperias=>creperias.id===id);
const getCreperiaIndexbyID = id => getCreperiaValidos().findIndex(creperias=>creperias.id===id)


//[GET] - /home - 100%
app.get('/',(req,res) =>{

    res.send('SEJA BEM VINDO!');
});

//[GET] -/filmes - retorna a lista de filmes -- 100%

app.get('/creperia',(req,res) =>{

    res.send(getCreperiaValidos());
});

//[GET] - /creperiA{id} - Retorna um único filme - 100%

app.get("/creperia/:id",(req,res) =>{

    const id = +req.params.id;

    const creperias = getCreperiabyID(id);

    

    if(!creperias){
        return res.send("No momento não servimos esse item.");

    }
    res.send(creperias);
});



//PARTE 2 do PROJETO
//[POST] - /CREPERIA - CRIA um novo Item 

app.post("/creperia",(req,res) =>{

    const creperias = req.body;

    //Validação

    if(!creperias || !creperias.nome || !creperias.imagemUrl){

        res.status(400).send({message:'Item não disponivel. Certifique-se  de que o body da requisição possui "nome" e "imagemURL".'});
            return;
    }

    const id = creperia.length + 1;
    let data = creperia
    creperia = {id: data.id, ...creperias};

    creperia.push(creperias);

    res.send(creperias);
});

//[PUT] - /filmes/{id} - Ataualiza um filme pelo ID

app.put("/filmes/:id",(req,res) =>{

    const id = req.params.id;

    const creperiasIndex = getCreperiasIndexbyID(id);

    creperia[id] = creperias;

    res.send(`Item atualizado com sucesso'${creperias}'.`);


//Validação

    if(creperiasIndex < 0){

        res.status(404).send({message: 'O item que você esta tentando editar não existe.'});
        
        return;
    }

    const novoItem = req.body;

    if(!Object.keys(novoItem).length){}


});















app.listen(port,()=>{

    console.info(`App rodando em:http://localhost:${port}`);
});