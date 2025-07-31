from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
from config.config import DATABASE
from validation.validation import validation

cliente_blueprint = Blueprint('cliente', __name__)

@cliente_blueprint.route('/')
def index():
    try:
        with sqlite3.connect(DATABASE) as conn:
            cliente = conn.execute("SELECT * FROM cliente").fetchall()
        return render_template('index.html', cliente = cliente) 
    except Exception as e:
        print(f"Erro as listar clientes: {e}")
        return f"Erro ao carregar clientes: {e}", 500

@cliente_blueprint.route('/criar', methods = ['GET', 'POST'])  
def criar():
    if request.method == 'POST': 
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']

        erros = validation(nome, cpf, email)

        if erros:
            return render_template('criar.html', erros = erros, nome = nome, cpf = cpf, email = email)
        
        try:
            with sqlite3.connect(DATABASE) as conn:
                conn.execute(
                    "INSERT INTO cliente (nome, cpf, email) VALUES (?, ?, ?)",
                    (nome, cpf, email)
                )
            return redirect(url_for('cliente.index'))
        except Exception as e:
            print(f"Erro ao criar cliente: {e}")
            return f"Erro ao criar cliente: {e}", 500
    return render_template('criar.html')        

@cliente_blueprint.route('//editar/<int:cliente_id>', methods = ['GET', 'POST'])
def editar(cliente_id):
    try:
        with sqlite3.connect() as conn:
            if request.method == 'POST':
                nome = request.form['nome']
                cpf = request.form['cpf']
                email = request.form['email']

                erros = validation(nome, cpf, email)

                if erros:
                    cliente = {'id': cliente_id, 'nome': nome, 'cpf': cpf, 'email': email}
                    return render_template('editar.html', cliente = cliente, erros = erros)
                
                conn.execute(
                    "UPDATE cliente SET nome = ?, cpf = ?, email = ? WHERE id = ?",
                    (nome, cpf, email, cliente_id)
                )
                return redirect(url_for('cliente.index'))
            
            cliente = conn.execute(
                "SELECT * FROM cliente WHERE id = ?",
                (cliente_id)
            ).fetchone()

            if cliente is None:
                return "Cliente não encontrado.", 404
            
        return render_template('editar.html', cliente = cliente)  

    except Exception as e:
        print(f"Erro ao editar cliente: {e}")
        return f"Erro ao editar cliente: {e}", 500

@cliente_blueprint.route('/apagar/<int:cliente_id>') 
def apagar(cliente_id):
    try:
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("DELETE FROM cliente WHERE id = ?", (cliente_id,))
        return redirect(url_for('cliente.index'))
    except Exception as e:
        print(f"Erro ao apagar cliente: {e}")
        return f"Erro ao apagar cliente. {e}", 500

