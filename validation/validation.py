import re

def validation(nome, cpf, email):
    """
    Valida os dados de nome, CPF e email fornecidos por um formulário.

    Realiza as seguintes validações:
    - Nome: obrigatório, mínimo de 3 caracteres, apenas letras e espaços.
    - CPF: obrigatório, deve conter 11 dígitos ou no formato 000.000.000-00.
    - Email: obrigatório, deve seguir um formato válido de email.

    Args:
        nome (str): Nome completo do cliente.
        cpf (str): CPF do cliente com ou sem formatação.
        email (str): Endereço de email do cliente.

    Returns:
        dict: Um dicionário contendo os erros encontrados. As chaves são os campos com erro
              ('nome', 'cpf', 'email') e os valores são mensagens explicativas. Se não houver erros,
              o dicionário estará vazio.
    """
    erros = {}

    regex_nome = re.compile(r'^[A-Za-zÀ-ÿ\s]+$')
    regex_cpf = re.compile(r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$|^(\d{11})$')
    regex_email = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')

    if not nome:
        erros['nome'] = 'O nome é obrigatório.'
    elif not regex_nome.fullmatch(nome):
        erros['nome'] = 'Nome inválido. Use apenas letras e espaços.'
    elif len(nome) < 3:
        erros['nome'] = 'O nome deve ter pelo menos 3 caracteres.'

    if not cpf:
        erros['cpf'] = 'O CPF é obrigatório.'
    elif not regex_cpf.fullmatch(cpf):
        erros['cpf'] = 'CPF inválido. Use o formato 000.000.000-00 ou apenas os 11 dígitos.'

    if not email:
        erros['email'] = 'O email é obrigatório.'
    elif not regex_email.fullmatch(email):
        erros['email'] = 'E-mail inválido.'

    return erros

