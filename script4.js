// Criando o elemento h1
const titulo = document.createElement("h1");
titulo.id = "titulo";
titulo.innerText = "Título do Site";

// Criando o elemento que representa o produto
const produto = document.createElement("div");
produto.classList.add("produto");

// Criando elementos filhos do produto
const nomeProduto = document.createElement("h2");
nomeProduto.innerText = "Nome do Produto";

const descricaoProduto = document.createElement("p");
descricaoProduto.innerText = "Descrição do Produto";

const precoProduto = document.createElement("span");
precoProduto.classList.add("preco");
precoProduto.innerText = "R$ 100,00";

// Adicionando elementos filhos ao produto
produto.appendChild(nomeProduto);
produto.appendChild(descricaoProduto);
produto.appendChild(precoProduto);

// Adicionando o título e o produto ao corpo da página
document.body.appendChild(titulo);
document.body.appendChild(produto);
