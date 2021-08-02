import React from 'react';

import './App.css'

export default class App extends React.Component{
  
  

  constructor(props){

    super(props);

    this.state={

      itens:[
        {
          id:1,
          nome:'Pizzas',
          imagemUrl:'https://imagensemoldes.com.br/wp-content/uploads/2020/04/Foto-Pizza-PNG.png',

        },
        {
          id:2,
          nome:'Crepes',
          imagemUrl:'https://png.pngitem.com/pimgs/s/297-2977143_transparent-crepe-png-strawberry-png-download.png',

        },
        {
          id:3,
          nome:'Sanduiches',
          imagemUrl:'https://www.pikpng.com/pngl/m/461-4616485_hamburguer-com-fritas-png-trio-sanduiche-clipart.png',

        },
        {
          id:4,
          nome:'Jantinhas',
          imagemUrl:'https://lh3.googleusercontent.com/B0BskrMeXDiwttkXhFbjWpjELW-JL04RBVR3aJSdGhK4FpkVdkSiTLXWaJxcWR_dFMcsS9FsY8l0jT3UHA=w768-h768-n-o-v1',

        },
        {
          id:5,
          nome:'Cremes',
          imagemUrl:'http://www.mundoboaforma.com.br/wp-content/uploads/2014/10/Vitaminas-de-Frutas-600x330.jpg?ad9cc4',

        },
        {
          id:6,
          nome:'Pasteis',
          imagemUrl:'https://imagensemoldes.com.br/wp-content/uploads/2020/05/Figura-Pastel-PNG.png',

        },
      ],
      nomeIten: "",
      imagemUrlIten: "",
      editando: false,
      indexEditando: null,
    };
  }

  onSubmit = (e) => {
    e.preventDefault();
    const { itens, editando, indexEditando, nomeIten, imagemUrlIten } =
      this.state;

    if (editando) {
      const itensAtualizados = itens.map((itens, index) => {
        if (indexEditando === index) {
          itens.nome = nomeIten;
          itens.imagemUrl = imagemUrlIten;
        }

        return itens;
      });

      this.setState({
        itens: itensAtualizados,
        indexEditando: null,
        editando: false,
      });
    } else {
      this.setState({
        itens: [
          ...itens,
          {
            nome: nomeIten,
            imagemUrl: imagemUrlIten,
          },
        ],
      });
    }

    this.setState({
      nomeIten: "",
      imagemUrlIten: "",
    });
  };

  deletar = (index) => {
    const { itens } = this.state;
    this.setState({
      itens: itens.filter((itens, i) => i !== index),
    });
  };

  render() {
    const { itens, nomeIten, imagemUrlIten, editando, indexEditando } =
      this.state;

    return (
      <div className="cardapio">
        <main className="nomes">
          <h1></h1>
          <hr />
          <h2>
            {editando
              ? `Editando: ${itens[indexEditando].nome}`
              : "*-*-Cadastre um novo Iten-*-*"}
          </h2>
          <form onSubmit={this.onSubmit}>
            <input
              placeholder="Nome"
              value={nomeIten}
              onChange={(e) => {
                this.setState({
                  nomeIten: e.target.value,
                });
              }}
            />
            <br />
            <input
              placeholder="Url da Imagem"
              value={imagemUrlIten}
              onChange={(e) => {
                this.setState({
                  imagemUrlIten: e.target.value,
                });
              }}
            />
            <br />
            <button type="submit">Salvar</button>
          </form>
          <hr />
          <h2>Itens</h2>
          <ul>
            {itens.map((itens, index) => (
              <li key={index}>
                <h3>{itens.nome}</h3>
                <img src={itens.imagemUrl} alt={itens.nome} />
                <br />
                <button onClick={() => this.deletar(index)}>Deletar</button>
                <br />
                <button
                  onClick={() => {
                    this.setState({
                      editando: true,
                      indexEditando: index,
                      nomeIten: itens.nome,
                      imagemUrlIten: itens.imagemUrl,
                    });
                  }}
                >
                  Editar
                </button>
              </li>
            ))}
          </ul>
        </main>
      </div>
    );
  }

}