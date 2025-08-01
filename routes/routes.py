from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
from config.config import DATABASE
from validation.validation import validation

cliente_blueprint = Blueprint('cliente', __name__)

@cliente_blueprint.route('/')
def index():
    """
    Exibe a lista de todos os clientes cadastrados.

    Returns:
        Renderização do template 'index.html' com os dados dos clientes,
        ou uma mensagem de erro.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            cliente = conn.execute("SELECT * FROM cliente").fetchall() 
        return render_template('index.html', cliente = cliente) 
    except Exception as e:
        print(f"Erro as listar clientes: {e}")
        return f"Erro ao carregar clientes: {e}", 500

@cliente_blueprint.route('/criar', methods = ['GET', 'POST'])  
def criar():
    """
    Cria um novo cliente a partir dos dados enviados via formulário.

    Returns:
        - Em caso de sucesso: redireciona para a rota de listagem.
        - Em caso de erro: renderiza o formulário com mensagens de erro.
    """
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

@cliente_blueprint.route('/editar/<int:cliente_id>', methods = ['GET', 'POST'])
def editar(cliente_id):
    """
    Edita os dados de um cliente existente.

    Args:
        cliente_id (int): ID do cliente a ser editado.

    Returns:
        - Em caso de sucesso: redireciona para a rota de listagem.
        - Em caso de erro: renderiza o formulário com mensagens de erro
          ou retorna erro 404/500 conforme o caso.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
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
                (cliente_id,)
            ).fetchone()

            if cliente is None:
                return "Cliente não encontrado.", 404
            
        return render_template('editar.html', cliente = cliente)  

    except Exception as e:
        print(f"Erro ao editar cliente: {e}")
        return f"Erro ao editar cliente: {e}", 500

@cliente_blueprint.route('/apagar/<int:cliente_id>') 
def apagar(cliente_id):
    """
    Exclui um cliente do banco de dados.

    Args:
        cliente_id (int): ID do cliente a ser removido.

    Returns:
        Redireciona para a página principal ou exibe mensagem de erro.
    """
    try:
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("DELETE FROM cliente WHERE id = ?", (cliente_id,))
        return redirect(url_for('cliente.index'))
    except Exception as e:
        print(f"Erro ao apagar cliente: {e}")
        return f"Erro ao apagar cliente. {e}", 500

