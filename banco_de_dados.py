CREATE DATABASE loja_roupas;
CREATE TABLE produtos (
  id_produto SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  descricao TEXT,
  preco_compra DECIMAL(10,2) NOT NULL,
  preco_venda DECIMAL(10,2) NOT NULL,
  quantidade_estoque INT NOT NULL,
  id_categoria INT NOT NULL,
  FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);
CREATE TABLE categorias (
  id_categoria SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL
);
CREATE TABLE clientes (
  id_cliente SERIAL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  cpf VARCHAR(11) NOT NULL UNIQUE,
  endereco VARCHAR(255),
  telefone VARCHAR(20)
);
CREATE TABLE vendas (
  id_venda SERIAL PRIMARY KEY,
  data_venda DATE NOT NULL,
  valor_total DECIMAL(10,2) NOT NULL,
  id_cliente INT NOT NULL,
  FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);
CREATE TABLE itens_venda (
  id_item_venda SERIAL PRIMARY KEY,
  id_venda INT NOT NULL,
  id_produto INT NOT NULL,
  quantidade INT NOT NULL,
  preco_venda DECIMAL(10,2) NOT NULL,
  FOREIGN KEY (id_venda) REFERENCES vendas(id_venda),
  FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);
INSERT INTO produtos (nome, descricao, preco_compra, preco_venda, quantidade_estoque, id_categoria)
VALUES
  ('Camisa X', 'Camisa manga curta em algodão.', 15.00, 30.00, 10, 1),
  ('Calça Y', 'Calça jeans slim fit.', 30.00, 50.00, 15, 2),
  ('Vestido Z', 'Vestido longo estampado.', 40.00, 80.00, 8, 3);
INSERT INTO categorias (nome)
VALUES
  ('Camisas'),
  ('Calças'),
  ('Vestidos');
INSERT INTO clientes (nome, cpf, endereco, telefone)
VALUES
  ('Ana Silva', '000.000.000-00', 'Rua das Flores, 123', '(11) 9999-9999'),
  ('João Oliveira', '111.111.111-11', 'Avenida Paulista, 456', '(12) 8888-8888');
INSERT INTO vendas (data_venda, valor_total, id_cliente)
VALUES
  ('2024-04-24', 150.00, 1),
  ('2024-04-23', 230.00, 2);
INSERT INTO itens_venda (id_venda, id_produto, quantidade, preco_venda)
VALUES
  (1, 1, 2, 30.00),
  (1, 2, 1, 50.00),
