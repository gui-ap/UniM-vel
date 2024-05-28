CREATE TABLE proprietarios (
  id INTEGER PRIMARY KEY,
  nome VARCHAR(255),
  cidade VARCHAR(255),
  cep VARCHAR(10)
);

CREATE TABLE imoveis (
  id INTEGER PRIMARY KEY,
  proprietario_id INTEGER,
  aluguel DECIMAL(10,2),
  cep VARCHAR(10),
  area_m2 DECIMAL(10,2),
  quartos INTEGER,
  tipo_propriedade VARCHAR(255),
  possibilidade_compra BOOLEAN,
  FOREIGN KEY (proprietario_id) REFERENCES proprietarios(id)
);

CREATE TABLE clientes (
  id INTEGER PRIMARY KEY,
  nome VARCHAR(255),
  cidade VARCHAR(255),
  cep VARCHAR(10)
);

CREATE TABLE vendas (
  id INTEGER PRIMARY KEY,
  cliente_id INTEGER,
  imovel_id INTEGER,
  data_venda TIMESTAMP,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id),
  FOREIGN KEY (imovel_id) REFERENCES imoveis(id)
);

CREATE TABLE alugueis (
  id INTEGER PRIMARY KEY,
  cliente_id INTEGER,
  imovel_id INTEGER,
  data_inicio TIMESTAMP,
  data_fim TIMESTAMP,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id),
  FOREIGN KEY (imovel_id) REFERENCES imoveis(id)
);

/*
Inserções
*/
-------------- inserindo os imoveis

INSERT INTO imoveis VALUES (2, 1200.00, 2, '60', '12345', 'Apartamento', 2, true);
INSERT INTO imoveis VALUES (3, 2200.00, 2, '70', '12344', 'Apartamento', 3, true);
INSERT INTO imoveis VALUES (4, 3200.00, 3, '62', '12343', 'Apartamento', 3, false);
INSERT INTO imoveis VALUES (5, 1400.00, 3, '24', '12342', 'Studio', 1, false);
INSERT INTO imoveis VALUES (6, 2200.00, 4, '44', '12341', 'Casa', 2, true);
INSERT INTO imoveis VALUES (7, 2400.00, 4, '45', '12340', 'Apartamento', 2, false);

-------------- inserindo os proprietarios

INSERT INTO proprietarios VALUES (2, 'Juan', 'São Paulo', '12345');
INSERT INTO proprietarios VALUES (3, 'Guilherme Augusto', 'São Paulo', '12344');
INSERT INTO proprietarios VALUES (4, 'Oliver Glenio', 'São Paulo', '12343');
INSERT INTO proprietarios VALUES (5, 'Wesley Evangelista', 'Rio de Janeiro', '12342');
INSERT INTO proprietarios VALUES (6, 'João da Silva', 'Curitiba', '12341');
INSERT INTO proprietarios VALUES (7, 'Maria de Jesus', 'Maceió', '12340');


-- Inserindos clientes
INSERT INTO clientes VALUES (2, 'Jose Oliveira', '30', '12345');
INSERT INTO clientes VALUES (3, 'Nathan Souza', '35', '12345');

-- Inserindos vendas
INSERT INTO vendas VALUES (2, 2, 2, 1200.00, CURRENT_TIMESTAMP);
INSERT INTO vendas VALUES (3, 3, 3, 2200.00, CURRENT_TIMESTAMP);

---------------------------------------------------- [Consultas]
--  buscar todas as vendas
SELECT vendas.id AS venda_id, clientes.nome AS cliente_nome, imoveis.id AS imovel_id, vendas.data_venda
FROM vendas
JOIN clientes ON vendas.cliente_id = clientes.id
JOIN imoveis ON vendas.imovel_id = imoveis.id;

-- consultando uma venda de um imovel especifico.
SELECT vendas.id AS venda_id, clientes.nome AS cliente_nome, imoveis.id AS imovel_id, vendas.data_venda
FROM vendas
JOIN clientes ON vendas.cliente_id = clientes.id
JOIN imoveis ON vendas.imovel_id = imoveis.id
WHERE imoveis.id = 12340; ------- aqui coloca o ID DO IMOVEL.

-- todas as vendas de um cliente específico
SELECT vendas.id AS venda_id, imoveis.id AS imovel_id, vendas.data_venda
FROM vendas
JOIN imoveis ON vendas.imovel_id = imoveis.id
WHERE vendas.cliente_id = 2; ------- aqui coloca o ID DO CLIENTE.

-- todos os aluguéis de um cliente específico
SELECT alugueis.id AS aluguel_id, imoveis.id AS imovel_id, alugueis.data_inicio, alugueis.data_fim
FROM alugueis
JOIN imoveis ON alugueis.imovel_id = imoveis.id
WHERE alugueis.cliente_id = 2; ------- aqui coloca o ID DO CLIENTE.
