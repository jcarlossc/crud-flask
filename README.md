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

## 🧰 Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLite3](https://www.sqlite.org/)
- [Bootstrap 5 (CDN)](https://getbootstrap.com/)
- [Regex (re módulo do Python)](https://docs.python.org/3/library/re.html)

---

## 🗂️ Estrutura do projeto


