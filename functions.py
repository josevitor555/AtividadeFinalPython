
from list import *

def validar_cpf(cpf):
  cpf = cpf.replace(".", "").replace("-", "")

  cpf_lista_invalidos = ["00000000000", "11111111111", "22222222222",
                         "33333333333", "44444444444", "55555555555", 
                         "66666666666", "77777777777", "88888888888", 
                         "99999999999", "01234567890"]
  
  if len(cpf) != 11 or cpf in cpf_lista_invalidos:
    return False
  
  soma = 0
  for i in range(9):
    soma += int(cpf[i]) * (10 - i)
    
  resto = 11 - (soma % 11)
  if resto >= 10:
    resto = 0
  if resto != int(cpf[9]):
    return False
  
  soma = 0
  for i in range(10):
    soma += int(cpf[i]) * (11 - i)
  
  resto = 11 - (soma % 11)
  if resto >= 10:
    resto = 0
  if resto != int(cpf[10]):
    return False
  
  return True

def checar_valor(valor_passado):
  if valor_passado <= 0:
    print('Insira um valor válido!')
    return False
  return True

def verificar_saldo_suficiente(cpf, tipo_conta, valor):
  match tipo_conta:
    case 'corrente':
      for conta in contas_corrente:
        if conta[0] == cpf:
          return conta[2] >= valor
    case 'poupanca':
      for conta in contas_poupanca:
        if conta[0] == cpf:
          return conta[2] >= valor
        
  return False

# def registrar_transacao():
#   cpf = input('Informe o CPF da conta: ')
#   tipo_conta = input('Informe o tipo de conta [corrente/poupanca]: ').strip() # se é conta corrente ou poupança
  
#   conta_encontrada = False
#   conta_atual = None
  
#   match tipo_conta:
#     case 'corrente':
#       for conta in contas_corrente:
#         if conta[0] == cpf:
#           conta_encontrada = True
#           conta_atual = conta
#           break
#     case 'poupanca':
#       for conta in contas_poupanca:
#         if conta[0] == cpf:
#           conta_encontrada = True
#           conta_atual = conta
#           break
  
#   if not conta_encontrada:
#     print('COnta não encontrada. Verifique o CPF e o tipo de conta.')
#     return
  
#   tipo_transacao = input('Informe o tipo de transação [debitar/creditar/pix]: ').strip()
  
#   if tipo_transacao not in ['debitar', 'creditar', 'pix']:
#     print('Tipo de transação inválida.')
#     return
  
#   try:
#     valor = float(input('Informe o valor da transação: '))
#     if valor <= 0:
#       print('O valor deve ser positivo.')
#       return
#   except ValueError: # se caso o suário não registrar um tipo de dado específico.
#     print('Valor Inválido. Deves ser um número.')
#     return
  
#   transacao = {
#     'tipo': tipo_transacao,
#     'valor': valor,
#     'cpf': cpf,
#     'descricao': f'{tipo_transacao.capitalize()} de R$ {valor}'
#   } # Teste: Fazer um em dicionário pra guarda os dados, com seus respectivos atributos
  
#   conta_atual[3].append(transacao)
#   print(f'Transação registrada com sucesso: {transacao['descricao']}')


def encerrar_conta():
  cpf = input('Informe o CPF da conta a ser encerrada: ')
  tipo_conta = input('Informe o tipo da conta a ser encerrada [corrente/poupanca]: ').strip().lower()
  
  conta_encontrada = False
  saldo = 0
  conta = None
  contas = None
  
  match tipo_conta:
    case 'corrente':
      contas = contas_corrente
    case 'poupanca':
      contas = contas_poupanca
    case _:
      print('Tipo de conta inválida. Escolha entre "corrente" ou "poupança"')
      return
  
  for c in contas:
    if c[0] == cpf:
      conta_encontrada = True
      conta = c
      break
  
  if not conta_encontrada:
    print(f'Conta {tipo_conta} com CPF {cpf} não foi encontrada.')
    return
  
  if saldo > 0:
    print(f'A conta {tipo_conta} possui um saldo positivo de R$ {saldo}. Saque o saldo anes de encerrar.')
    return
  elif saldo < 0:
    print(f'A conta {tipo_conta} possui um saldo negativo de R$ {saldo}. Regularize o saldo anes de encerrar.')
    return
  
  # print('Encerrando conta...')
  # registrar_transacao()
  
  contas.remove(conta) # removendo a conta atual da lista
  print(f'A conta {tipo_conta} foi encerrada com sucesso.')

def creditar_conta():
  cpf = input('Informe o CPF da conta a ser creditada: ')
  tipo_conta = input('Informe o tipo da conta [corrente/poupanca]: ')
  
  conta_encontrada = False
  conta_atual = None
  
  match tipo_conta:
    case 'corrente':
      for conta in contas_corrente:
        if conta[0] == cpf:
          conta_encontrada = True
          conta_atual = conta
          break
    case 'poupanca':
      for conta in contas_poupanca:
        if conta[0] == cpf:
          conta_encontrada = True
          conta_atual = conta
          break
  
  if not conta_encontrada:
    print('CPF não encontrado. Verifique o CPF e tente novamente.')
    return
  
  try:
    valor_creditado = float(input('Informe valor a ser creditado: '))
    if not checar_valor(valor_creditado):
      return
  except ValueError as error:
    print(f'Por favor. Insira apenas número {error}')
  
  conta_atual[2] += valor_creditado
  print(f'Valor de R${valor_creditado} creditado com sucesso na conta de CPF {cpf}.')
  
  # registrar_transacao()

def debitar_conta():
  cpf = input('Informe o CPF da conta para realizar o saque: ')
  tipo_conta = input('Informe o tipo da conta [corrente/poupanca] a ser debitado: ')
  
  try:
    valor_debito = float(input('Informe o valor a ser debitado: '))
    if valor_debito <= 0:
      print('Valor inválido para débito.')
      return
  except ValueError as error:
    print(f'Por favor. Insira apenas número {error}')
  
  if not checar_valor(valor_debito):
    return # retorne nada...
  
  if not verificar_saldo_suficiente(cpf, tipo_conta, valor_debito):
    print(f'Saldo insuficiente na conta {tipo_conta} para realizar o débito de R${valor_debito}')
    return
  
  conta_encontrada = False
  # conta_atual = None
  
  match tipo_conta:
    case 'corrente':
      for conta in contas_corrente:
        if conta[0] == cpf:
          conta_encontrada = True
          if conta[2] >= valor_debito:
            conta[2] -= valor_debito
            # registrar_transacao()
            print(f'Valor de R${valor_debito} debitado com sucesso da conta corrente.')
          else:
            print(f'Saldo insuficiente para realizar débito.')
    case 'poupanca':
      for conta in contas_poupanca:
        if conta[0] == cpf:
          conta_encontrada = True
          if conta[2] >= valor_debito:
            conta[2] -= valor_debito
            # registrar_transacao()
            print(f'Valor de R${valor_debito} debitado com sucesso da conta poupança.')
          else:
            print(f'Saldo insuficiente para realizar débito.')
  
  
  # registrar_transacao(conta_atual, 'saque', valor_debito, cpf)
  if not conta_encontrada:
    print(f'Conta {tipo_conta} com CPF {cpf} não foi encontrada.')

def consultar_saldo():
  cpf = input('Informe o cpf para verificar o saldo: ')
  if not validar_cpf(cpf):
    print(f'{cpf} inválido!')
    return
  
  conta_corrente_encontrada = False
  conta_poupanca_encontrada = False
  
  for conta in contas_corrente:
    if conta[0] == cpf:
      conta_corrente_encontrada = True
      print(f'Saldo da Conta Corrente (Nome: {conta[1]}): R${conta[2]}')
      break
  
  for conta in contas_poupanca:
    if conta[0] == cpf:
      conta_poupanca_encontrada = True
      print(f'Saldo da Conta Poupança (Nome: {conta[1]}): R${conta[2]}')
      break
  
  if not conta_corrente_encontrada:
    print('Conta Corrente não encontrada para o CPF informado.')
  
  if not conta_poupanca_encontrada:
    print('Conta Poupança não encontrada para o CPF informado.')

def criar_conta_corrente():
  cpf = input('Informe o CPF do titular: ')
  if not validar_cpf(cpf):
    print(f'{cpf} inválido!')
    return
  
  nome_titular = input('Informe o nome do titular: ')
  
  cpf_encontrado = False
  nome_incorreto = False
  
  for conta in contas_corrente + contas_poupanca:
    if conta[0] == cpf:
      cpf_encontrado = True
      if conta[1] != nome_titular:
        nome_incorreto = True
        break
    
  if cpf_encontrado and nome_incorreto:
    print(f'O CPF {cpf} já estar cadastrado com outro nome.')
    return
    
  for conta in contas_corrente:
    if conta[0] == cpf:
      print(f'O cliente já possui uma conta corrente com CPF {cpf}.')
      return
  
  try:  
    saldo_inicial = float(input("Informe o saldo inicial: "))
    if saldo_inicial < 0:
      print("O saldo inicial não pode ser negativo.")
      return
  except ValueError as error:
    print(f'Por favor. Insira apenas número {error}')
  
  conta_corrente = [cpf, nome_titular, saldo_inicial, [], 500, 1000, 0]
  contas_corrente.append(conta_corrente)
  clientes.append([cpf, nome_titular])
  
  print(f'Conta de {nome_titular} criada com sucesso!')
  
def criar_conta_poupanca():
  cpf = input('Informe o CPF do titular: ')
  if not validar_cpf(cpf):
    print(f'{cpf} inválido!')
    return
  
  nome_titular = str(input('Informe o nome do titular: '))
  
  cpf_encontrado = False
  nome_iconrreto = False
  
  for conta in contas_corrente + contas_poupanca:
    if conta[0] == cpf:
      cpf_encontrado = True
      if conta[1] != nome_titular:
        nome_iconrreto = True
        break
  
  if cpf_encontrado and nome_iconrreto:
    print(f'O CPF {cpf} já está cadastrado com outro nome.')
    return
    
  for conta in contas_poupanca:
    if conta[0] == cpf:
      print(f'O cliente já possui uma conta poupança com CPF {cpf}.')
      return
  
  try:
    saldo_inicial = float(input("Informe o saldo inicial: "))
    if saldo_inicial < 0:
      print("O saldo inicial não pode ser negativo.")
      return
  except ValueError as error:
    print(f'Por favor. Insira apenas número {error}')
  
  conta_poupanca = [cpf, nome_titular, saldo_inicial, [], 0.02]
  contas_poupanca.append(conta_poupanca)
  clientes.append([cpf, nome_titular])
  
  print(f'Conta de {nome_titular} criada com sucesso!')

def realizar_pix():
  cpf_origem = input('Informe o CPF da conta de origem: ')
  tipo_conta_origem = input('Informe o tipo da conta de origem [corrente/poupanca]: ')
  cpf_destino = input('Informe o CPF da conta de destino: ')
  tipo_conta_destino = input('Informe o tipo de conta de destino [corrente/poupanca]: ')
  
  try:
    valor_pix = float(input('Informe o valor a ser transferido via PIX: '))
    if valor_pix <= 0:
      print('Valor inválido para transferência via PIX')
      return
  except ValueError as error:
    print(f'Error: {error}')
  
  if not verificar_saldo_suficiente(cpf_origem, tipo_conta_origem, valor_pix):
    print(f'Saldo insuficente na conta {tipo_conta_origem} para realizar o PIX de R${valor_pix}')
    
  conta_origem_econtrada = False  
  conta_destino_econtrada = False
  conta_origem = None
  conta_destino = None
  
  match tipo_conta_origem:
    case 'corrente':
      for conta in contas_corrente:
        if conta[0] == cpf_origem:
          conta_origem_econtrada = True
          if conta[2] >= valor_pix:
            conta[2] -= valor_pix
            conta_origem = conta # Guardar referência para registrar transação depois
            # registrar_transacao()
            print(f'Valor de R${valor_pix} transferido via PIX da conta corrente de origem.')
          else:
            print('Saldo insuficiente para realizar o PIX.')
            return
          break    
    case 'poupanca':
      for conta in contas_poupanca:
        if conta[0] == cpf_origem:
          conta_origem_econtrada = True
          if conta[2] >= valor_pix:
            conta[2] -= valor_pix
            conta_origem = conta # Guardar referência para registrar transação depois
            # registrar_transacao()
            print(f'Valor de R${valor_pix} transferido via PIX da conta poupança de origem.')
          else:
            print('Saldo insuficiente para realizar o PIX.')
            return
          break
  
  match tipo_conta_destino:
    case 'corrente':
      for conta in contas_corrente:
        if conta[0] == cpf_destino:
          conta_destino_econtrada = True
          conta[2] += valor_pix
          conta_destino = conta # Guardar referência para registrar transação depois
          # registrar_transacao()
          print(f'Valor de R${valor_pix} recebido via PIX na conta corrente de destino.')
          break
        
    case 'poupanca':
      for conta in contas_poupanca:
        if conta[0] == cpf_destino:
          conta_destino_econtrada = True
          conta[2] += valor_pix
          conta_destino = conta # Guardar referência para registrar transação depois
          # registrar_transacao()
          print(f'Valor de R${valor_pix} recebido via PIX na conta poupanca de destino.')
          break
  
  if not conta_origem_econtrada:
    print(f'Conta de origem {tipo_conta_origem} com CPF {cpf_origem} não foi encontrada.')
    return
  
  if not conta_destino_econtrada:
    print(f'Conta de destino {tipo_conta_destino} com CPF {cpf_destino} não foi encontrada.')
    return
  
  if conta_origem:
    # registrar_transacao() registrar os detalhes do PIX na conta de origem
    pass
  if conta_destino:
    # registrar_transacao() registrar os detalhes do PIX na conta de destino
    pass

def exibir_menu():
  list_menu = {
    '1': 'Criar Conta Corrente',
    '2': 'Criar Conta Poupança',
    '3': 'Depositar Valor',
    '4': 'Sacar Valor',
    '5': 'Realizar Pix',
    '6': 'Excluir conta',
    '7': 'Ver Histórico de Transações',
    '8': 'Consultar saldo',
    '9': 'Sair do Sistema'
  }
  
  menu = ''
  for key, value in list_menu.items():
    menu += f'{key}. {value}\n'
  
  return menu.strip()
