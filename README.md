# TFG
Raspberry Pi

O Que necessito para ter o servidor funcional.
1. Raspberry Pi 2 Model B;
2. Placa de rede ethernet usb;
3. Imagem do Raspbian Whezzy, obtida em:
https://downloads.raspberrypi.org/raspbian/images/raspbian-2015-05-07/2015-05-05-raspbian-wheezy.zip

Neste repositório você irá encontrar os arquivos de configuração necessários para a configuração de um servidor de firewall e proxy.
Para isso deve seguir alguns passos:

1. Instale o Raspbian Whezzy no seu Raspbery 2 Modelo B, já com a placa de rede USB conectada (Vale lembrar que o abaixo, foi testado somente nesse cenário)
2. Abra o terminal como root
3. Configure suas placas de rede, para eth0 receber o sinal da internet e eth1 distribuir para o switch
3.1 Neste caso é configurado a rede 192.168.0.0/24 com o ip 192.168.0.100 na placa de rede eth1
3.2 Caso deseje altere as suas temos o exemplo do arquivo interfaces que está localizado em /etc/network/interfaces
4. Execute o comando:
# apt-get install apache2 bind9 squid3 sarg isc-dhcp-server
4.1 Caso não tenhas é de suma importancia que instale o python 2.7 para executar o menu de opções desenvolvido para a aplicação:
# apt-get install python2.7
5. Inicie o serviço de ssh:
#/etc/init.d/ssh start, caso não tenhas instalado execute o comando: 
#apt-get install ssh
6. Copie o arquivo com script firewall.sh para /root/iptables (Está pasta deve ser criada e deve ficar oculta)
7. Copie o arquivo gestorderede.py para /root
IMPORTANTE faça uma cópia de todos os arquivos padrão
8. Altere os arquivos /etc/rc.local /etc/squid3 /etc/sarg /etc/default/isc-dhcp-server
9. Instale os pacotes no click-5.1
# pip install click
