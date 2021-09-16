create database cadastro_produtos;
use cadastro_produtos;
create table produtos(
	id int primary key not null auto_increment,
    codigo int,
    descricao varchar(50),
    preco double,
    categoria varchar(20)
);

insert into produtos(codigo, descricao, preco, categoria) VALUES(123, "impressora", 500.00, "informatica");
insert into produtos(codigo, descricao, preco, categoria) VALUES(124, "monitor", 800.00, "informatica");
insert into produtos(codigo, descricao, preco, categoria) VALUES(125, "tablet", 1000.00, "eletronicos");
insert into produtos(codigo, descricao, preco, categoria) VALUES(126, "arroz", 15.00, "alimentos");
insert into produtos(codigo, descricao, preco, categoria) VALUES(127, "feijao", 9.50, "alimentos");

describe produtos;