# -*- coding: cp1252 -*-
import click
import sys
import subprocess

def exit():
  """SAIR DO SISTEMA"""
  print "Obrigado por utilizar o Gerenciador de Redes. \nFique tranquilo tudo está salvo."
  return sys.exit(0)


def list_rules():
  """LISTAR REGRAS"""
  comando = "iptables -L"
  print subprocess.check_output(comando, shell=True)
  click.pause("Pressione ENTER para continuar")


def add_block():
  """MENU ADICIONAR"""
  while True:
    op = raw_input("Digite 1 para bloqueio de URL ou 2 para bloqueio de IP: ")
    if op == "1":
      return add_block_url()
    elif op == "2":
      return add_block_ip()
    else:
      print "OPÇÃO INVALIDA"


def add_block_url():
  """ADICIONAR BLOQUEIO DE URL"""
  end = raw_input("Digite o endereco que deseja bloquear: ")
  comando = "iptables -A FORWARD -i eth1 -m string --algo bm --string % s -j DROP" % end
  print subprocess.check_output(comando, shell=True)

  with open("/root/.firewall/firewall.sh", "r+") as arq:
      conteudo = arq.read()
      conteudo.replace("#marcador#", "#marcador#\n"+comando+"\n")
      arq.seek(0)
      arq.write(conteudo)

  print "Comando executado."
  click.pause("Pressione ENTER para continuar")  


def add_block_ip():
  """ADICIONAR BLOQUEIO DE IP"""
  ip = raw_input("Digite o endereco de IP que deseja bloquear: ")
  comando = "iptables -A INPUT -s %s -j DROP" % ip
  print subprocess.check_output(comando, shell=True)
  
  
  with open("/root/.firewall/firewall.sh", "r+") as arq:
      conteudo = arq.read()
      conteudo.replace("#marcador#", "#marcador#\n"+comando+"\n")
      arq.seek(0)
      arq.write(conteudo)

  print "Comando executado."
  click.pause("Pressione ENTER para continuar")


def remove_block():
  """ MENU REMOVER """
  while True:
    op = raw_input("Digite 5 para remover bloqueio de URL ou 6 para remover bloqueio de IP: ")
    if op == "5":
      return add_block_url()
    elif op == "6":
      return add_block_ip()
    else:
      print "OPÇÃO INVALIDA"
 

def remove_block_url():
  """REMOVER BLOQUEIO DE URL"""
  end = raw_input("Digite o endereco que deseja remover o bloqueio: ")
  comando = "iptables -A FORWARD -i eth1 -m string --algo bm --string %s -j DROP --delete" % end
  comandoatualiza = "iptables -A FORWARD -i eth1 -m string --algo bm --string %s -j DROP" % end
  print subprocess.check_output(comando, shell=True)

  with open("/root/.firewall/firewall.sh", "r+") as arq:
      conteudo = arq.read()
      conteudo.remove(comandoatualiza)
      arq.seek(0)
      arq.write(conteudo)

  atualizascript = "./root/.firewall/firewall.sh"
  print subprocess.checkoutput(comando, shell=True)
  print subprocess.checkoutput(atualizascript, shell=True)
  print "Comandos executados."
  click.pause("Pressione ENTER para continuar")  


def remove_block_ip():
  """REMOVER BLOQUEIO DE IP"""
  ip = raw_input("Digite o IP que deseja remover o bloqueio: ")
  comando = "iptables -A INPUT -s %s -j DROP --delete" % ip
  print subprocess.check_output(comando, shell=True)

  with open("/root/.firewall/firewall.sh", "r+") as arq:
      conteudo = arq.read()
      conteudo.replace(comando, "")
      arq.seek(0)
      arq.write(conteudo)

  atualizascript = "./root/.firewall/firewall.sh"
  print subprocess.checkoutput(atualizascript, shell=True)
  print "Comandos executados."
  click.pause("Pressione ENTER para continuar")  


@click.command()
def main():
  options = {'9': exit, '1': add_block, '2': add_block_url, '3': add_block_ip, '4': remove_block, '5': remove_block_url,
	     '6': remove_block_ip, '7': list_rules }


  def print_menu():
    click.clear()
    print "MENU DE OPÇÕES DO GERENCIADOR DE REDES\n"
    for opt, func in sorted(options.iteritems()):
      print "%s\t - \t%s \n" % (opt, func.__doc__)

  while True:
    print_menu()
    opt = raw_input("Digite sua escolha: ")
    if opt in options:
      options[opt]()
    else:
      click.pause( click.style("Opção invalida. Aperte ENTER para continuar.\n", fg='red'))


if __name__ == "__main__":
  main()
