#! /bin/bash

#Este pe o arquivo mais importante, através dele quie todas as configurações do firewall iptables são ativadas ao startar o servidor
#Dentro desse arquivo são inseridas as regras criados por meio do gerenciador de rede desenvolvido em python

#Executando as regras;
#-F serve para excluir todas as regras contidas na
#Entrada
iptables -F INPUT
#Saída
iptables -F OUTPUT
#Encaminhamento
iptables -F FORWARD
#Na tabela nat (novas conexões)
iptables -t nat -F
#Na tabela mangle (alterações de pacotes especifícos
iptables -t mangle -F

#As demais regras que forem sendo criadas pelo administrador da rede irão aqui.

#Adiciona os modulos no kernel;
modprobe ip_tables
modprobe iptable_nat

#Libera encaminhamento de pacotes;
echo "1" > /proc/sys/net/ipv4/ip_forward

#Compartilha a internet;
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

#Proxy transparente, tratando dos protocolos UDP e TCP, e movendo o trafego das portas 80,443 para porta 3128;
iptables -t nat -A PREROUTING -s 192.168.0.0/24 -p tcp --dport 80 -j REDIRECT --to-port 3128

iptables -t nat -A PREROUTING -s 192.168.0.0/24 -p udp --dport 80 -j REDIRECT --to-port 3128

iptables -t nat -A PREROUTING -s 192.168.0.0/24 -p tcp --dport 443 -j REDIRECT --to-port 3128

iptables -t nat -A PREROUTING -s 192.168.0.0/24 -p udp --dport 443 -j REDIRECT --to-port 3128 
