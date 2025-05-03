# 🧾 Sistema Web de Cadastro de Clientes com Python, Flask e MySQL

Projeto desenvolvido por **Paulo César**, estudante de Sistemas de Informação, com foco em soluções práticas e integradas de desenvolvimento web.  
Esta aplicação realiza o **cadastro, edição, visualização e exclusão de clientes**, conectando o backend Python com um banco de dados relacional MySQL e uma interface web simples e funcional.


## 🚀 Destaques do Projeto

- 🔗 Integração completa entre Python (Flask) e MySQL
- 📄 Interface web responsiva com HTML e CSS
- 🧩 Banco de dados com estrutura relacional e chaves estrangeiras
- 🛠 Operações CRUD completas (Create, Read, Update, Delete)
- 📦 Código limpo, comentado e 100% funcional


## 🛠 Tecnologias Utilizadas

- **Python 3 + Flask** — Backend web moderno e leve
- **MySQL** — Armazenamento relacional de dados
- **HTML + CSS** — Estrutura e estilo da interface web
- **MySQL Connector** — Integração entre Python e banco
- **Visual Studio Code** — Ambiente de desenvolvimento
- **Git + GitHub** — Versionamento e portfólio


## 🧱 Estrutura do Banco de Dados

O banco de dados `cadastro_clientes` possui três tabelas principais:

- `clientes`: dados pessoais (nome, email, telefone, CPF, data de nascimento)
- `enderecos`: endereço completo (rua, número, complemento, bairro, cidade, estado, CEP)
- `contatos`: tipo de contato adicional (e.g. WhatsApp, comercial) e seu valor

> Todas as tabelas são interligadas com chaves estrangeiras, garantindo integridade e consistência nos dados.


## 💻 Como Executar o Projeto Localmente

### 1. Configure o Banco MySQL

Crie o banco de dados e as tabelas  `Clientes`,  `Endereços` e  `Contatos` com o seguinte comando:

CREATE DATABASE cadastro_clientes;
USE cadastro_clientes;

-- Ativa suporte a transações e InnoDB (padrão a partir do MySQL 8.0)
SET default_storage_engine = 'InnoDB';

CREATE TABLE IF NOT EXISTS Clientes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome_completo VARCHAR(255) NOT NULL,
  cpf CHAR(11) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  telefone VARCHAR(20),
  data_nascimento DATE,
  INDEX idx_clientes_cpf (cpf),
  INDEX idx_clientes_email (email)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Enderecos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT NOT NULL,
  rua VARCHAR(255) NOT NULL,
  numero VARCHAR(20) NOT NULL,
  complemento VARCHAR(100),
  bairro VARCHAR(100) NOT NULL,
  cidade VARCHAR(100) NOT NULL,
  estado CHAR(2) NOT NULL,
  cep VARCHAR(10) NOT NULL,
  CONSTRAINT fk_enderecos_clientes
    FOREIGN KEY (cliente_id)
    REFERENCES Clientes(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Contatos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT NOT NULL,
  tipo_contato ENUM('telefone', 'email', 'outro') NOT NULL,
  valor_contato VARCHAR(255) NOT NULL,
  CONSTRAINT fk_contatos_clientes
    FOREIGN KEY (cliente_id)
    REFERENCES Clientes(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;


### 2. Instale as Dependências

pip install flask mysql-connector-python

### 3. Execute o Servidor

python main.py

Abra o navegador e acesse: `http://127.0.0.1:5000`


## 📌 Funcionalidades Implementadas

* ✔ Cadastro de novos clientes
* ✔ Edição de dados existentes
* ✔ Visualização da lista de clientes
* ✔ Exclusão de registros com confirmação
* ✔ Banco relacional robusto e bem estruturado


## 🎯 Objetivo do Projeto

Este projeto tem caráter **educacional e profissional**, ideal para:

* Demonstrar habilidades em **desenvolvimento web com Flask**
* Consolidar o uso de **bancos relacionais em aplicações reais**
* Criar soluções reutilizáveis para **sistemas de cadastro em ambientes comerciais**


## 👨‍💻 Sobre o Autor

Sou **Paulo César**, estudante de Sistemas de Informação, e tenho como propósito criar soluções funcionais que unem backend, banco de dados e front-end de forma prática, clara e objetiva.

📬 Conecte-se comigo:

* [LinkedIn](https://www.linkedin.com/in/pcsdv)
* [GitHub](https://github.com/pcsdv0)


🧠 Este é mais um passo na construção do meu portfólio como desenvolvedor. Estou sempre em busca de aprendizado, desafios e novas oportunidades. Obrigado por acompanhar!*


