import click
import sys
import subprocess

def exit():
  """SAIR DO SISTEMA"""
  print "Obrigado por utilizar o gerenciador do redes."
  return sys.exit(0)


def list_rules():
  """LISTAR REGRAS"""
  comando = "iptables -L"
  print subprocess.check_output(comando, shell=True)
  click.pause("Pressione ENTER para continuar")


def add_block():
  """ADICIONAR REGRAS"""
  while True:
    op = raw_input("Digite 1 para bloqueio de URL ou 2 para bloqueio de IP: ")
    if op == "1":
      return add_block_url()
    elif op == "2":
      return add_block_ip()
    else:
      print "OPCAO INVALIDA"


def add_block_url():
  """ADICIONAR BLOQUEIO DE URL"""
  end = raw_input("Digite o endereco que deseja bloquear: ")
  


def add_block_ip():
  """ADICIONAR BLOQUEIO DE IP"""
  ip = raw_input("Digite o endereco de IP que deseja bloquear: ")
  comando = "iptables -A INPUT -s %s -j DROP" % ip
  print subprocess.check_output(comando, shell=True)
  print "Comando executado."
  click.pause("Pressione ENTER para continuar")


def remove_block():
  """REMOVER REGRAS"""
  pass


def remove_block_url():
  """REMOVER BLOQUEIO DE URL"""
  pass


def remove_block_ip():
  """REMOVER BLOQUEIO DE IP"""
  pass


@click.command()
def main():
  options = {'9': exit, '1': add_block, '2': add_block_url, '3': add_block_ip, '4': remove_block, '5': remove_block_url,
	     '6': remove_block_ip, '7': list_rules }


  def print_menu():
    click.clear()
    print "MENU DE OPCOES"
    for opt, func in sorted(options.iteritems()):
      print "%s\t - \t%s" % (opt, func.__doc__)

  while True:
    print_menu()
    opt = raw_input("Digite sua escolha: ")
    if opt in options:
      options[opt]()
    else:
      click.pause( click.style("Opcao invalida. Aperte ENTER para continuar.\n", fg='red'))


if __name__ == "__main__":
  main()
