CREATE TABLE "proprietarios" (
  "id" integer PRIMARY KEY,
  "nome" varchar,
  "cidade" varchar,
  "cep" varchar
);

CREATE TABLE "imoveis" (
  "id" integer PRIMARY KEY,
  "proprietario_id" integer,
  "aluguel" decimal,
  "cep" varchar,
  "area_m2" decimal,
  "quartos" integer,
  "tipo_propriedade" varchar,
  "possibilidade_compra" boolean
);

CREATE TABLE "clientes" (
  "id" integer PRIMARY KEY,
  "nome" varchar,
  "cidade" varchar,
  "cep" varchar
);

CREATE TABLE "vendas" (
  "id" integer PRIMARY KEY,
  "cliente_id" integer,
  "imovel_id" integer,
  "data_venda" timestamp
);

CREATE TABLE "alugueis" (
  "id" integer PRIMARY KEY,
  "cliente_id" integer,
  "imovel_id" integer,
  "data_inicio" timestamp,
  "data_fim" timestamp
);

ALTER TABLE "imoveis" ADD FOREIGN KEY ("proprietario_id") REFERENCES "proprietarios" ("id");

ALTER TABLE "vendas" ADD FOREIGN KEY ("cliente_id") REFERENCES "clientes" ("id");

ALTER TABLE "vendas" ADD FOREIGN KEY ("imovel_id") REFERENCES "imoveis" ("id");

ALTER TABLE "alugueis" ADD FOREIGN KEY ("cliente_id") REFERENCES "clientes" ("id");

ALTER TABLE "alugueis" ADD FOREIGN KEY ("imovel_id") REFERENCES "imoveis" ("id");
