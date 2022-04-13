/*
-- OBSERVAÇÃO: Os dados informados nas tabelas podem fugir um pouco da realidade porque a finalidade dos mesmos era testar os comandos aqui 
--             apresentados, podendo aparecer, por exemplo, professor em várias disciplinas de diversos cursos, assim como disciplinas 
--             que na realidade não tem como correspondencia, dependencias aqui apresentadas.
-- CRIA BANCO DE DADOS
CREATE DATABASE bd_projeto4_Desenvolve40mais;

-- CRIA TABELAS DE DADOS
USE bd_projeto4_Desenvolve40mais;

CREATE TABLE aluno (
	cpf_aluno BIGINT PRIMARY KEY,
	nome VARCHAR(40),
	endereco VARCHAR(50),
	telefone CHAR(11),
	data_nasc DATE);

CREATE TABLE departamento(
	codigo_dpto INT PRIMARY KEY AUTO_INCREMENT,
    nome CHAR(5),
    descricao VARCHAR(45));
    
CREATE TABLE curso(
	codigo_curso INT PRIMARY KEY AUTO_INCREMENT,
    nome_curso CHAR(30),
    descricao VARCHAR(100),
    codigo_dpto INT,
	FOREIGN KEY (codigo_dpto) REFERENCES departamento(codigo_dpto));

CREATE TABLE matricula(
	codigo_curso INT,
    cpf_aluno BIGINT,
    data_matricula DATE,
    FOREIGN KEY (codigo_curso) REFERENCES curso (codigo_curso),
    FOREIGN KEY (cpf_aluno) REFERENCES aluno (cpf_aluno));

CREATE TABLE professor(
	matricula_prof INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(45),
    endereco VARCHAR(45),
    telefone CHAR(11),
    data_nasc DATE,
    codigo_dpto INT,
    data_contratacao DATE,
	FOREIGN KEY (codigo_dpto) REFERENCES departamento (codigo_dpto));

CREATE TABLE disciplina(
	codigo_disciplina INT PRIMARY KEY AUTO_INCREMENT,
    nome_disciplina VARCHAR(45),
    qtd_creditos INT,
    matricula_prof INT);

CREATE TABLE cursa(
	cpf_aluno BIGINT,
    codigo_disciplina INT,
	FOREIGN KEY (cpf_aluno) REFERENCES aluno (cpf_aluno),
	FOREIGN KEY (codigo_disciplina) REFERENCES disciplina (codigo_disciplina));

CREATE TABLE compoe(
	codigo_curso INT,
    codigo_disciplina INT,
	FOREIGN KEY (codigo_curso) REFERENCES curso (codigo_curso),
	FOREIGN KEY (codigo_disciplina) REFERENCES disciplina (codigo_disciplina));

CREATE TABLE pre_req(
	codigo_disciplina INT,
    codigo_disciplina_dependencia INT,
	FOREIGN KEY (codigo_disciplina) REFERENCES disciplina (codigo_disciplina),
	FOREIGN KEY (codigo_disciplina_dependencia) REFERENCES disciplina (codigo_disciplina));
-- ****************************************FIM DA CRIAÇÃO DAS TABELAS******************************************************************************
-- ****************************************INICIO DAS INSERÇÕES DE DADOS******************************************************************************
-- ADICIONA DADOS NAS TABELAS CRIADAS
-- Aluno
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (11111111111, 'Pedro Ancântara Coelho', 'Rua das Flores, 1549 bairro Santos Timon-Ma', '86985461254', '2001-06-27');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (98798798798, 'Maria da Cruz dos Santos', 'Praça Anita Garibaldi, 536 Centro Campinas-SP', '77925453578', '2003-02-12');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (78978978978, 'Cleide Josefina da Silva', 'Rua Anfibólios, 560 Bonfim Belo Horizonte-MG', '11965783265', '1995-09-22');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (45645645645, 'Manoel Freitas Neto', 'Rua Anita Ferraz, 208 Sé São Paulo-SP', '1433017515', '2002-08-2');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (65465465465, 'Hugo Pereira do Vale', 'Rua Condado, 114 Cavalhada Porto Alegre-RS', '8840012535', '1998-01-15');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (12312312312, 'Marta Gonçalves', 'Rua Anita Cajado, 232 Praia Grande Salvados-BA', '99920006578', '2001-06-06');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (32132132132, 'José dos Santos e Silva', 'Rua Anita Garibald, 249 Santo Antônio Manaus-AM', '61335078848', '1975-03-08');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (15915915915, 'Fernanda Nobre', 'Avenida Pedro II, 946 Conjunto B Brasilia-DF', '65224567799', '1959-05-21');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (95195195195, 'Claudia Araujo Péricles', 'Conjunto Calhau Quadra 15 Casa 22 Fortaleza-CE', '31955552222', '2003-12-18');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (35735735735, 'Amanda Gonçalves', 'Avenida Miguel Rosa, 5674 Centro Teresina-PI', '33685214578', '2000-06-19');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (75375375375, 'Rosilene do Carmo e Sousa', 'Avenida Presidente Figueiredo, 6721 Tabosa Codó-MA', '48965471235', '1999-10-16');
INSERT INTO aluno (cpf_aluno, nome, endereco, telefone, data_nasc) VALUES (58758758758, 'Severino da Silva Moreira', 'Rua Sem Fim,  1945 Areas Caxias-MA', '65986865454', '2002-10-19');

-- Departamento
INSERT INTO departamento (nome, descricao) VALUES ('CCHL', 'CENTRO DE CIÊNCIAS HUMANAS E LETRAS');
INSERT INTO departamento (nome, descricao) VALUES ('CCN', 'CENTRO DE CIÊNCIAS DA NATUREZA');
INSERT INTO departamento (nome, descricao) VALUES ('CCA', 'CENTRO DE CIÊNCIAS AGRÁRIAS');
INSERT INTO departamento (nome, descricao) VALUES ('CCE', 'CENTRO DE CIÊNCIAS DA EDUCAÇÃO');
INSERT INTO departamento (nome, descricao) VALUES ('CCS', 'CENTRO DE CIÊNCIAS DA SAÚDE');
INSERT INTO departamento (nome, descricao) VALUES ('CT', 'CENTRO DE TECNOLOGIA');
    
-- Curso
INSERT INTO curso (nome_curso, descricao, codigo_dpto) VALUES ('CIÊNCIAS POLÍTICA', 'Cria competências técnico-científica sobre o conhecimento das relações políticas.', 1);
INSERT INTO curso (nome_curso, descricao, codigo_dpto) VALUES ('DIREITO', 'Aprende tudo sobre leis e normas nacionais e internacionais torna-se apto a aplica-las na sociedade.', 1);
INSERT INTO curso (nome_curso, descricao, codigo_dpto) VALUES ('ADMINISTRAÇÃO', 'Gere os recursos de uma organização e atua em diferentes departamentos.', 1);
INSERT INTO curso (nome_curso, descricao, codigo_dpto) VALUES ('MEDICINA', 'Diagnostica doenças, receita medicamentos, realiza cirurgias e conduz tratamentos diversos.', 5);
INSERT INTO curso (nome_curso, descricao, codigo_dpto) VALUES ('ENFERMAGEM', 'Administram medicamentos , a alimentação e higiene de pessoas em processo de recuperação.', 5);
INSERT INTO curso (nome_curso, descricao, codigo_dpto) VALUES ('PEDAGOGIA', 'Profissional especialista em educação, que pode atuar dentro e fora do ambiente escolar.', 4);
INSERT INTO curso (nome_curso, descricao, codigo_dpto) VALUES ('MUSICA', 'Atua na produção, regencia, composição em eventos, orquestras, corais, estúdios, etc.', 4);
INSERT INTO curso (nome_curso, descricao, codigo_dpto) VALUES ('ENGENHARIA CIVIL', 'Elabora, conduz e realiza obras e projetos como casas, pontes, estradas e grandes edificações.', 6);
INSERT INTO curso (nome_curso, descricao, codigo_dpto) VALUES ('ZOOTECNIA', 'Trabalha para que animais vivam em boas condições, cuida da reprodução e melhoramento genético.', 3);
INSERT INTO curso (nome_curso, descricao, codigo_dpto) VALUES ('MEDICINA VETERINÁRIA', 'Responsável pela saúde animais domésticos e silvestres.', 3);

-- Matricula
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (1, '58758758758', '2022-01-23');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (1, '75375375375', '2021-01-27');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (1, '35735735735', '2020-06-12');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (4, '95195195195', '2022-01-15');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (4, '15915915915', '2022-06-30');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (4, '32132132132', '2019-01-05');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (4, '12312312312', '2021-06-09');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (8, '98798798798', '2020-01-16');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (8, '65465465465', '2019-01-17');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (8, '45645645645', '2022-01-11');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (8, '11111111111', '2019-01-17');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (8, '78978978978', '2022-01-11');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (5, '95195195195', '2022-01-15');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (5, '15915915915', '2022-06-30');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (5, '32132132132', '2019-01-05');
INSERT INTO matricula (codigo_curso, cpf_aluno, data_matricula) VALUES (5, '12312312312', '2021-06-09');

-- Professor
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Agnes Figueiredo', 'Conjunto Sacy Q-15 C-10 Sacy Teresina-PI', '86945458787', '1975-01-11', 1, '2011-05-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Nicolas Lucas Ricardo Gonçalves', 'QD QNP 30 Conjunto 442 Sul Brasília-DF', '86912345678', '2001-02-01', 1, '2014-07-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Pietro Thomas Campos', 'Av. Brasilia, 391 Fazendinha MAcapa-AP', '86932146547', '2005-05-16', 1, '2014-12-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Raimundo Thales Bruno da Luz', 'Rua São Benedito, 825 São Benedito Cuiabá-MT', '88925873698', '1995-09-24', 1, '2018-11-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Victor Theo Dias', 'Rua Marte, 270 Parnamirim Teresina-PI', '88654132585', '1994-11-15', 1, '2016-09-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Liz Alessandra Araújo', 'Rua Plutão Santos Teresina-PI', '88912366547', '1975-10-18', 1, '2015-01-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Eliane Stefany Laís Rezende', 'Rua das Camélias, 3456 Garagem Teresina-PI', '86947891596', '1972-09-04', 1, '2005-06-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Carolina Aparecida Figueiredo', 'Rua 100 Parque Alvorada Timon-MA', '85915963574', '1988-04-16', 1, '2021-08-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Lucca Antonio Elias Almada', 'Rua 200 Parque Alvorada Timon-MA', '85945647897', '1983-02-19', 5, '2020-03-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Juliana Marina Agatha Santos', 'Quadra 34 Casa 12 Sacy Teresina-PI', '86975417541', '1959-12-26', 5, '2019-04-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Paulo Manoel Ramos', 'Rua Posto, 6521 Felipe Teresina-PI', '86915423256', '1977-11-30', 5, '2019-10-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Tatiane Analu Elisa Castro', 'Rua Horizonte, 478 Mocambinho Teresina-PI', '86920212122', '1965-08-07', 5, '2019-11-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Vitor Lucas da Conceição', 'Rua Campos, 6547 Fatima Teresina-PI', '98920202020', '1999-07-08', 5, '2016-12-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Vera Sophia Viana', 'Rua dos Idosos, 4565 Areas Teresina-PI', '99920001111', '2002-09-29', 5, '2018-02-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Natália Elaine Nunes', 'Rua Descente, 65 Centro Teresina-PI', '99920002222', '1989-03-11', 5, '2019-11-22');
INSERT INTO professor (nome, endereco, telefone, data_nasc, codigo_dpto, data_contratacao) VALUES ('Luiza Isadora Sara Teixeira', 'Rua 87, 987 Centro Timon-MA', '99930002545', '1991-04-13', 5, '2017-07-22');

-- Disciplina
-- Ciências Politica
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Pensamento Social e Político Brasileiro', 1, 1); -- Ciências Politica
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Sociologia', 1, 2); -- Ciências Politica
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Introdução à Ciência Política', 1, 3); -- Ciências Politica
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Estudo em Segurança Internacional', 1, 4); -- Ciências Politica
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Antropologia', 1, 5); -- Ciências Politica
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Estatística', 1, 6); -- Ciências Politica
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Relações Internacionais', 1, 7); -- Ciências Politica
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Direito', 1, 8); -- Ciências Politica
-- Medicina
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Anatomia Humana ', 42, 9); -- Medicina
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Imagenologia', 12, 10); -- Medicina
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Práticas Integradoras', 12, 11); -- Medicina
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Introdução à Saúde Coletiva', 27, 12); -- Medicina
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Fisiologia Humana I', 12, 13); -- Medicina
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Bioquímica', 18, 14); -- Medicina
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Biofísica', 12, 15); -- Medicina
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Histologia /Embriologia', 42, 16); -- Medicina
-- Enfermagem
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Anatomia Humana', 16, 9); -- Endermagem
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Biologia Celular, Histologia e Embriologia', 10, 10); -- Endermagem
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Bioquímica', 6, 11); -- Endermagem
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('História da Enfermagem', 6, 12); -- Endermagem
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Lingua Portuguesa', 6, 13); -- Endermagem
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Meio Ambiente e Saúde', 6, 14); -- Endermagem
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Microbiologia e Imunologia', 10, 15); -- Endermagem
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Parasitologia', 6, 16); -- Endermagem
-- Engenharia Civil
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Lingua Portuguesa', 6, 1); -- Engenharia Civil
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Bases Matematicas para Engenharia', 6, 1); -- Engenharia Civil
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Bases Físicas para Engenharia', 16, 5); -- Engenharia Civil
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Introdução à Engenharia', 10, 3); -- Engenharia Civil
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Ciências do Ambiente', 6, 9); -- Engenharia Civil
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Planejamento de Carreira, Sucesso', 6, 10); -- Engenharia Civil
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Probabilidade e Estatística para Engenharia', 16, 11); -- Engenharia Civil
INSERT INTO disciplina (nome_disciplina, qtd_creditos, matricula_prof) VALUES ('Lógica de Programação', 10, 7); -- Engenharia Civil

-- Cursa
-- Ciências Política
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('58758758758', 1);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('58758758758', 2);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('58758758758', 3);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('75375375375', 1);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('75375375375', 2);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('75375375375', 3);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('35735735735', 1);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('35735735735', 2);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('35735735735', 3);
-- Medicina
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('95195195195', 9);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('95195195195', 10);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('95195195195', 11);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('15915915915', 9);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('15915915915', 10);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('15915915915', 11);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('32132132132', 9);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('32132132132', 10);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('32132132132', 11);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('12312312312', 9);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('12312312312', 10);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('12312312312', 11);
-- Enfermagem
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('95195195195', 17);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('95195195195', 18);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('95195195195', 19);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('15915915915', 17);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('15915915915', 18);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('15915915915', 19);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('32132132132', 17);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('32132132132', 18);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('32132132132', 19);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('12312312312', 17);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('12312312312', 18);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('12312312312', 19);
-- Engenharia Civil
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('98798798798', 25);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('98798798798', 26);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('98798798798', 27);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('65465465465', 25);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('65465465465', 26);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('65465465465', 27);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('45645645645', 25);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('45645645645', 26);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('45645645645', 27);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('11111111111', 25);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('11111111111', 26);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('11111111111', 27);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('78978978978', 25);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('78978978978', 26);
INSERT INTO cursa (cpf_aluno, codigo_disciplina) VALUES ('78978978978', 27);

-- Compoe
-- Ciências Política
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (1, 1);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (1, 2);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (1, 3);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (1, 4);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (1, 5);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (1, 6);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (1, 7);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (1, 8);
-- Medicina
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (4, 9);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (4, 10);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (4, 11);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (4, 12);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (4, 13);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (4, 14);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (4, 15);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (4, 16);
-- Enfermagem
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (5, 17);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (5, 18);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (5, 19);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (5, 20);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (5, 21);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (5, 22);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (5, 23);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (5, 24);
-- Engenharia
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (8, 25);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (8, 26);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (8, 27);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (8, 28);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (8, 29);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (8, 30);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (8, 31);
INSERT INTO compoe (codigo_curso, codigo_disciplina) VALUES (8, 32);


-- Pre-requisitos
-- Ciências Política
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (1, 3);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (2, 3);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (3, 3);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (4, 1);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (5, 3);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (6, 3);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (7, 4);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (8, 1);
-- Medicina
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (9, 12);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (10, 12);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (11, 11);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (12, 12);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (13, 9);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (14, 12);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (15, 12);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (16, 12);
-- Enfermagem
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (17, 20);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (18, 21);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (19, 20);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (20, 20);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (21, 21);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (22, 20);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (23, 21);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (24, 21);
-- Engenharia
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (25, 25);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (26, 28);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (27, 28);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (28, 28);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (29, 25);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (30, 28);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (31, 28);
INSERT INTO pre_req (codigo_disciplina, codigo_disciplina_dependencia) VALUES (32, 25);
*/
-- ****************************************FIM DAS INSERÇÕES DE DADOS******************************************************************************
/*
-- a.	Produza um relatório que contenha os dados dos alunos matriculados em todos os cursos oferecidos pela escola. 
USE bd_projeto4_Desenvolve40mais;
SELECT aluno.nome 'Nome do Aluno', aluno.cpf_aluno 'CPF do Aluno', aluno.telefone 'Telefone', DATE_FORMAT(aluno.data_nasc, '%d/%m/%Y') 'Data de Nascimento', departamento.nome 'Nome do Departamento', curso.nome_curso 'Nome do Curso', DATE_FORMAT(matricula.data_matricula, '%d/%m/%Y') 'Data da Matrícula'
FROM matricula
INNER JOIN (curso) on (curso.codigo_curso) = (matricula.codigo_curso) 
INNER JOIN (aluno) on (aluno.cpf_aluno) = (matricula.cpf_aluno)
INNER JOIN (departamento) on (curso.codigo_dpto) = (departamento.codigo_dpto)
ORDER BY aluno.nome, curso.nome_curso;
*/
/*
-- b.	Produza um relatório com os dados de todos os cursos, com suas respectivas disciplinas, oferecidos pela escola.
USE bd_projeto4_Desenvolve40mais;
SELECT curso.nome_curso 'CURSO', disciplina.nome_disciplina 'DISCIPLINA', professor.nome 'PROFESSOR'
FROM compoe
INNER JOIN (curso) on (curso.codigo_curso) = (compoe.codigo_curso)
INNER JOIN (disciplina) on (disciplina.codigo_disciplina) = (compoe.codigo_disciplina)
INNER JOIN (professor) on (professor.matricula_prof) = (disciplina.matricula_prof)
ORDER BY curso.nome_curso, disciplina.nome_disciplina;
*/
/*
-- c.	Produza um relatório que contenha o nome dos alunos e as disciplinas em que estão matriculados.
USE bd_projeto4_Desenvolve40mais;
SELECT aluno.nome 'ALUNO', disciplina.nome_disciplina 'DISCIPLINA', curso.nome_curso 'CURSO', DATE_FORMAT(matricula.data_matricula, '%d/%m/%Y') 'DATA DA MATRÍCULA'
FROM aluno
INNER JOIN (cursa) on (cursa.cpf_aluno) = (aluno.cpf_aluno)
INNER JOIN (disciplina) on (disciplina.codigo_disciplina) = (cursa.codigo_disciplina)
INNER JOIN (compoe) on (compoe.codigo_disciplina) = (disciplina.codigo_disciplina)
INNER JOIN (curso) on (curso.codigo_curso) = (compoe.codigo_curso)
INNER JOIN (matricula) on  (matricula.cpf_aluno) = (aluno.cpf_aluno)
ORDER BY aluno.nome, curso.nome_curso;
*/
-- d.	Produza um relatório com os dados dos professores e as disciplinas que ministram.
/*
USE bd_projeto4_Desenvolve40mais;
SELECT professor.matricula_prof 'Matrícula', nome 'Nome', endereco 'Endereço', telefone 'Telefone', DATE_FORMAT(data_nasc, '%d/%m/%Y') 'Nascimento', codigo_dpto 'Depto', DATE_FORMAT(data_contratacao, '%d/%m/%Y') 'Contratado em' , disciplina.nome_disciplina 'Nome da Disciplina'
FROM professor
INNER JOIN (disciplina) on (disciplina.matricula_prof) = (professor.matricula_prof)
ORDER BY professor.matricula_prof;
*/
/*
-- e.	Produza um relatório com os nomes das disciplinas e seus pré-requisitos.
USE bd_projeto4_Desenvolve40mais;
SELECT (SELECT disciplina.nome_disciplina FROM disciplina WHERE disciplina.codigo_disciplina = pre_req.codigo_disciplina) 'DISCIPLINA', disciplina.nome_disciplina 'DEPENDENCIA' FROM pre_req
INNER JOIN disciplina ON disciplina.codigo_disciplina = pre_req.codigo_disciplina_dependencia
ORDER BY disciplina.nome_disciplina;
*/
/*
-- f.	Produza um relatório com a média de idade dos alunos matriculados em cada curso.
USE bd_projeto4_Desenvolve40mais;
SELECT FLOOR(AVG((DATEDIFF(CURRENT_DATE(), aluno.data_nasc))/365)) 'MÉDIA DE IDADE POR CURSO', curso.nome_curso 'CURSO'
FROM aluno
INNER JOIN matricula ON matricula.cpf_aluno = aluno.cpf_aluno
INNER JOIN curso ON curso.codigo_curso = matricula.codigo_curso
GROUP BY matricula.codigo_curso
ORDER BY matricula.codigo_curso;
*/
/*
-- g.	Produza um relatório com os cursos oferecidos por cada departamento.
USE bd_projeto4_Desenvolve40mais;
SELECT departamento.nome 'DEPARTAMENTO', departamento.descricao 'DESCRIÇÃO DEPARTAMENTO', curso.nome_curso 'CURSO'
FROM curso
INNER JOIN departamento ON departamento.codigo_dpto = curso.codigo_dpto
ORDER BY departamento.codigo_dpto;
 */
/*
-- RELTÓRIO EXTRA
-- Relatório dos Alunos acrescido a idade.
USE bd_projeto4_Desenvolve40mais;
SELECT aluno.cpf_aluno 'CPF Aluno', aluno.nome 'Nome', DATE_FORMAT(aluno.data_nasc, '%d/%m/%Y') 'Nascimento', FLOOR((DATEDIFF(CURRENT_DATE(), aluno.data_nasc))/365), curso.nome_curso 'Curso' FROM aluno
INNER JOIN matricula ON matricula.cpf_aluno = aluno.cpf_aluno
INNER JOIN curso ON curso.codigo_curso = matricula.codigo_curso;
*/
-- ****************************************FIM DOS RELATÓRIOS******************************************************************************
-- ****************************************EXTRAS PARA TESTES******************************************************************************
/*
USE bd_projeto4_Desenvolve40mais;
SELECT * FROM aluno;
SELECT * FROM departamento;
SELECT * FROM curso;
SELECT * FROM matricula;
SELECT * FROM professor;
SELECT * FROM disciplina;
SELECT * FROM cursa;
SELECT * FROM compoe;
SELECT * FROM pre_req;
*/
/*
DESC alunos;
DESC departamento;
DESC curso;
DESC matricula;
DESC professor;
DESC disciplina;
DESC cursa;
DESC compoe;
DESC pre_req;
*/
-- ****************************************FIM DOS EXTRAS******************************************************************************
