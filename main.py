from functions import *

def rows(str):
  print('-' * 30)
  print(str)
  print('-' * 30)

rows("The PyBank Corp.")

def operacoes():
  while True:
    exibir = exibir_menu()
    print(exibir)
    
    opcao = input('Informe sua opção: ')
    match opcao:
      case '1':
        rows('Você escolheu criar conta corrente.')
        criar_conta_corrente()
      case '2':
        rows('Você escolheu criar conta poupança.')
        criar_conta_poupanca()
      case '3':
        rows('Você escolheu Depositar valor.')
        creditar_conta()
      case '4':
        rows('Você escolheu Sacar valor.')
        debitar_conta()
      case '5':
        rows('Você escolheu Realizar Pix.')
        realizar_pix()
      case '6':
        rows('Você escolheu Encerrar Conta')
        encerrar_conta()
      case '7':
        rows('Você escolheu Ver Histórico de Transações')
        ver_historico_transacao()
      case '8':
        rows('você escolheu Consultar Saldo')
        atualizar_saldo_poupanca()
        consultar_saldo()
      case '9':
        atualizar_saldo_poupanca()
        rows('Você saiu do sistema! Seus saldos foram atualizados.')
        exit()
      
operacoes()