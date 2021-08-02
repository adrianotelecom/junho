create table departamento(
cord_depto serial primary key,
nome_depto varchar (25) not null
);

create table funcionario(
cod_func serial primary key,
nome_func varchar (50) not null,
salario money not null,
cord_depto int references departamento (cord_depto) not null
);

create table projeto (
cod_projeto serial primary key,
nome_projeto varchar (30) not null,
duracao int not null
);

create table func_proj(
cod_func_proj serial primary key,
horas_trab int not null,
cod_func int references funcionario (cod_func) not null,
cod_projeto int references projeto (cod_projeto) not null
);


select * from departamento;

insert into departamento (nome_depto)  values ('Programador');
insert into departamento (nome_depto)  values ('RH');
insert into departamento (nome_depto)  values ('Administrativo');
insert into departamento (nome_depto)  values ('Produção');
insert into departamento (nome_depto)  values ('Markting');
insert into departamento (nome_depto)  values ('Pesquisa');
insert into departamento (nome_depto)  values ('Vendas');


select * from funcionario;

insert  into funcionario (nome_func,salario,cord_depto) values ('Darth Vader', 3500, 6);
insert  into funcionario (nome_func,salario,cord_depto) values ('Megazord', 20000, 1);
insert  into funcionario (nome_func,salario,cord_depto) values ('Jiraya', 5000, 5);
insert  into funcionario (nome_func,salario,cord_depto) values ('Jaspion', 1200, 2);
insert  into funcionario (nome_func,salario,cord_depto) values ('Doctor Rey', 8000, 7);

insert  into funcionario (nome_func,salario,cord_depto) values ('Doctor Rey', 8000, 7);
insert  into funcionario (nome_func,salario,cord_depto) values ('Doctor Rey', 8000, 7);



select  * from projeto;


insert into projeto (nome_projeto,duracao) values ('Construção da Estrela da Morte', 48);
insert into projeto (nome_projeto,duracao) values ('Projeto Superzord', 6);
insert into projeto (nome_projeto,duracao) values ('Reconstrução Facial D. Vader', 2);
insert into projeto (nome_projeto,duracao) values ('Dominar o Mundo', 12);
insert into projeto (nome_projeto,duracao) values ('Projeto Togakur', 50);


select * from func_proj;

insert into func_proj (horas_trab,cod_func,cod_projeto) values (8000,1,1);
insert into func_proj (horas_trab,cod_func,cod_projeto) values (1000,2,2);
insert into func_proj (horas_trab,cod_func,cod_projeto) values (36500,3,5);
insert into func_proj (horas_trab,cod_func,cod_projeto) values (2000,4,4);
insert into func_proj (horas_trab,cod_func,cod_projeto) values (20,5,3);

----------------------------------------------------------------------------------------------------------------------
-- inner join -- obtenha o nome de cada funcionario e o nome do departamento  que cada um pertence


select f.nome_func, d.nome_depato
from funcionario f inner join departamento d -- full outer join
on f.cord_depto = d.cord_depto;
-----------------------------------------------------------------------------------------------------------------------


--********************************************************************************************************************************
---left join -- Obtenha o nome de todos os departamentos da empresa e a quantidade de funcionarios pertecentes a cada um deles.


select d.nome_depto,count(f.codigo_func) as Total_Empregados
from departamento d left join funcionario f 
on d.cod_depto = f.cord_depto
group by d.nome_depto;
order by total_empregados asc;

--mesmo exercício com Rigth Join
select d.nome_depto,count(f.codigo_func) as Total_Empregados
from funcionario f left join departamento d 
on d.cod_depto = f.cord_depto
group by d.nome_depto;
order by total_empregados asc;









