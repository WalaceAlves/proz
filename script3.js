// Capturando os elementos
const titulo = document.getElementById("titulo");
const listaNaoOrdenada = document.querySelector("ul");
const link = document.querySelector("a");
const listaOrdenada = document.getElementById("lista-ordenada");

// Adicionando conteúdo textual
titulo.innerText = "Título do Projeto";
link.innerText = "ProZed Educação";

// Adicionando itens à lista não ordenada
listaNaoOrdenada.innerHTML = `
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
`;

// Adicionando itens à lista ordenada
listaOrdenada.innerHTML = `
  <li><a href="https://www.google.com">Google</a></li>
  <li><a href="https://www.youtube.com">YouTube</a></li>
  <li><a href="https://www.wikipedia.org">Wikipedia</a></li>
`;
