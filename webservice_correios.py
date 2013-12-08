# coding:utf-8
import urllib
import urllib2
from decimal import *
import xml.etree.ElementTree as ET


class Correios(object):

        def retorna_frete(self, cep):
                
                cep_destino = cep                   

                data = urllib.urlencode(
                        {
                                "nCdEmpresa": "",
                                "sDsSenha":   "",
                                "nCdServico": "40010",
                                "sCepOrigem": "14091170",
                                "sCepDestino": str(cep_destino),# CEP DE DESTINO
                                "nVlPeso" : "2",
                                "nCdFormato": int(1),
                                "nVlComprimento": Decimal(17),
                                "nVlAltura": Decimal(17),
                                "nVlLargura": Decimal(17),
                                "nVlDiametro": Decimal(17),
                                "sCdMaoPropria": "N",
                                "nVlValorDeclarado": Decimal(100),
                                "sCdAvisoRecebimento": "N",
                                "StrRetorno": "xml",
                                #"nIndicaCalculo": Decimal(1)
                        }

                )
                #URL do correios + dados mesclados com ?&
                url = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?" + data

                #Faz o request. 
                req = urllib2.Request(url)

                #Abre a url
                response = urllib2.urlopen(req)

                #atribui o conteudo nessa variavel xml
                conteudo = response.read()

                #imprimi o conteudo xml
                #print conteudo

                #cria um doc ET pela string passada
                doc = ET.ElementTree(ET.fromstring(conteudo))

                #recupera a tag principal
                root = doc.getroot()

                #pega o valor do frete pelo indice do XML
                frete =  root[0][1].text
                #print "O valor do frete é" ,frete

                return frete


        


