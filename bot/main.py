'''Chama os Scripts

'''
from SAP import loginSAP
from sql_server import conectar
from sql_server import desconectar
from sites import amazon

loginSAP.loginSap()
conectar.conectar()
desconectar.desconectar()
amazon.acessarAmazon()