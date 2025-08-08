# 📋 CRUD de Clientes com Flask e Validação via Regex

Este projeto é uma aplicação web simples desenvolvida com **Flask** que realiza operações **CRUD (Create, Read, Update, Delete)** em um banco de dados SQLite. O sistema inclui **validação de dados com expressões regulares (Regex)** para garantir a integridade dos dados inseridos (nome, CPF e email).

---

## ✨ Funcionalidades

- ✅ Listar todos os clientes cadastrados
- ➕ Criar novos clientes com validação de:
  - Nome (somente letras e espaços, mínimo de 3 caracteres)
  - CPF (formato `000.000.000-00` ou apenas números)
  - Email (formato válido)
- ✏️ Editar os dados de um cliente com validação
- 🗑️ Remover clientes do banco de dados
- 💾 Armazenamento persistente em **SQLite**
- 🎨 Interface HTML com Bootstrap 5

---

## 🧰 Ferramentas utilizadas

- Python 3.9.13
- Ambiente virtual `venv`
- Framework Flask
- Módulo `re`
- SQLite3
- `unittest` para testes
- Git/GitHub
- Visual Studio Code
- Sistema operacional Windows 10

---

## Requisitos

- Python 3.x
- Módulo `re`
- Framework Flask
- SQLite3
- `unittest` para testes

---

## Como utilizar

```bash
# Clone o repositório
git clone https://github.com/jcarlossc/crud-flask.git

# Acesse o diretório
cd crud-flask

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate           # Windows
source venv/bin/activate        # Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py

# Para sair do ambiente virtual
deactivate
```
---

## ▶️ Acesse no navegador: 
```
    http://localhost:5000
```

---

## Contribuição:

Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

---

## Licença:

Este projeto é licenciado sob a Licença MIT.

---

## Comandos importantes:

```bash
python -m venv venv               # Cria um ambiente virtual
venv\Scripts\activate             # Ativa o ambiente no Windows
source venv/bin/activate          # Ativa o ambiente no Linux/macOS
deactivate                        # Encerra o ambiente virtual

pip install nome-pacote           # Instala um pacote
pip uninstall nome-pacote         # Remove um pacote
pip freeze > requirements.txt     # Gera (ou atualiza) o arquivo de dependências
pip install -r requirements.txt   # Instala pacotes listados no requirements.txt
pip list                          # Lista pacotes instalados
pip show nome-pacote              # Exibe detalhes de um pacote
```
