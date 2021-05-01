#! python3

#1 Importa Bibliotecas
from sys import exit
import time
import pandas as pd


#2 Conecta, lê e fecha o arquivo -- arquivo = open('demo2.txt', 'r', encoding='UTF-8')
print('SCRIPT DESENVOLVIDO POR LUIZ CLAUDIO TAVARES SILVA\nVERSÃO 1 - 24/04/2020\n')
print('O ARQUIVO A SER REESTRUTURADO DEVE ESTAR NA MESMA PASTA DO SCRIPT E NO FORMATO TXT.')
nome_arquivo_entrada = input('Informe o nome do arquivo a ser reestruturado (sem extensão): ')
arquivo = open(nome_arquivo_entrada + '.txt', 'r')
arq = arquivo.readlines()
arquivo.close()

#3 Função gerar arquivos em formato separado por vírgulas, planilha ou não gerar arquivo
def gerar_arquivo(option):
    if option == str(1):
        print('\nGRAVANDO OS DADOS EM SEU NOVO ARQUIVO. AGUARDE.')
        df_global.to_csv('_' + nome_arquivo_entrada + '.csv')
        tempo3 = time.time()
        intervalo2 = round((tempo3 - tempo2), 2)
        print('\nARQUIVO CSV GRAVADO COM SUCESSO EM ' + str(intervalo2) + ' SEGUNDOS\n')
    elif option == str(2):
        print('\nGRAVANDO OS DADOS EM SEU NOVO ARQUIVO. AGUARDE.')
        df_global.to_excel('_' + nome_arquivo_entrada + '.xlsx')
        tempo3 = time.time()
        intervalo2 = round((tempo3 - tempo2), 2)
        print('\nARQUIVO XLSX GRAVADO COM SUCESSO EM ' + str(intervalo2) + ' SEGUNDOS\n')
    elif option == str(3):
        print('\nGRAVANDO OS DADOS EM SEUS NOVOS ARQUIVOS. AGUARDE.')
        df_global.to_csv('_' + nome_arquivo_entrada + '.csv')
        df_global.to_excel('_' + nome_arquivo_entrada + '.xlsx')
        tempo3 = time.time()
        intervalo2 = round((tempo3 - tempo2), 2)
        print('\nARQUIVOS CSV E XLSX GRAVADOS COM SUCESSO EM ' + str(intervalo2) + ' SEGUNDOS\n')
    else:
        print('\nSCRIPT ENCERRADO\n')
        exit()


tempo1 = time.time()

#4 Mensagem ao usuário
print('\nARQUIVO CARREGADO COM SUCESSO')
print('REESTRUTURANDO O ARQUIVO. AGUARDE!')

#5 Criando um dicionário

dic = {}

dic['TIPO DE REGISTRO'] = [int(arq[nlinha][24:26]) for nlinha in range(1, len(arq)-1)]
dic['DATA DO PREGÃO'] = [(arq[nlinha][2:10]) for nlinha in range(1, len(arq)-1)]
dic['CÓDIGO BDI'] = [(arq[nlinha][10:12]) for nlinha in range(1, len(arq)-1)]
dic['CÓDIGO DE NEGOCIAÇÃO DO PAPEL'] = [(arq[nlinha][12:24]).rstrip() for nlinha in range(1, len(arq)-1)]
dic['TIPO DE MERCADO'] = [int(arq[nlinha][24:27]) for nlinha in range(1, len(arq)-1)]
dic['NOME RESUMIDO DA EMPRESA EMISSORA DO PAPEL'] = [(arq[nlinha][27:39]).rstrip() for nlinha in range(1, len(arq)-1)]
dic['ESPECIFICAÇÃO DO PAPEL'] = [(arq[nlinha][39:49]).strip('-') for nlinha in range(1, len(arq)-1)]
dic['PRAZO EM DIAS DO MERCADO A TERMO'] = [(arq[nlinha][49:52]) for nlinha in range(1, len(arq)-1)]
dic['MOEDA DE REFERÊNCIA'] = [(arq[nlinha][52:56]).rstrip() for nlinha in range(1, len(arq)-1)]
dic['PREÇO DE ABERTURA DO PAPEL-MERCADO NO PREGÃO'] = [float(arq[nlinha][56:69])/100 for nlinha in range(1, len(arq)-1)]
dic['PREÇO MÁXIMO DO PAPEL-MERCADO NO PREGÃO'] = [float(arq[nlinha][69:82])/100 for nlinha in range(1, len(arq)-1)]
dic['PREÇO MÍNIMO DO PAPEL-MERCADO NO PREGÃO'] = [float(arq[nlinha][82:95])/100 for nlinha in range(1, len(arq)-1)]
dic['PREÇO MÉDIO DO PAPEL-MERCADO NO PREGÃO'] = [float(arq[nlinha][95:108])/100 for nlinha in range(1, len(arq)-1)]
dic['PREÇO DO ÚLTIMO NEGÓCIO DO PAPEL-MERCADO NO PREGÃO'] = [float(arq[nlinha][108:121])/100 for nlinha in range(1, len(arq)-1)]
dic['PREÇO DA MELHOR OFERTA DE COMPRA DO PAPEL-MERCADO'] = [float(arq[nlinha][121:134])/100 for nlinha in range(1, len(arq)-1)]
dic['PREÇO DA MELHOR OFERTA DE VENDA DO PAPEL-MERCADO'] = [float(arq[nlinha][134:147])/100 for nlinha in range(1, len(arq)-1)]
dic['NÚMERO DE NEGÓCIOS EFETUADOS COM O PAPEL-MERCADO NO PREGÃO'] = [int(arq[nlinha][147:152]) for nlinha in range(1, len(arq)-1)]
dic['QUANTIDADE TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL- MERCADO'] = [int(arq[nlinha][152:170]) for nlinha in range(1, len(arq)-1)]
dic['VOLUME TOTAL DE TÍTULOS NEGOCIADOS NESTE PAPEL-MERCADO'] = [float(arq[nlinha][170:188])/100 for nlinha in range(1, len(arq)-1)]
dic['PREÇO DE EXERCÍCIO PARA O MERCADO DE OPÇÕES OU VALOR DO CONTRATO PARA O MERCADO DE TERMO SECUNDÁRIO'] = [float(arq[nlinha][188:201])/100 for nlinha in range(1, len(arq)-1)]
dic['INDICADOR DE CORREÇÃO DE PREÇOS DE EXERCÍCIOS OU VALORES DE CONTRATO PARA OS MERCADOS DE OPÇÕES OU TERMO SECUNDÁRIO'] = [int(arq[nlinha][201:202]) for nlinha in range(1, len(arq)-1)]
dic['DATA DO VENCIMENTO PARA OS MERCADOS DE OPÇÕES OU TERMO SECUNDÁRIO'] = [(arq[nlinha][202:210]) for nlinha in range(1, len(arq)-1)]
dic['FATOR DE COTAÇÃO DO PAPEL'] = [int(arq[nlinha][210:217]) for nlinha in range(1, len(arq)-1)]
dic['PREÇO DE EXERCÍCIO EM PONTOS PARA OPÇÕES REFERENCIADAS EM DÓLAR OU VALOR DE CONTRATO EM PONTOS PARA TERMO SECUNDÁRIO'] = [float(arq[nlinha][217:230])/100 for nlinha in range(1, len(arq)-1)]
dic['CÓDIGO DO PAPEL NO SISTEMA ISIN OU CÓDIGO INTERNO DO PAPEL'] = [(arq[nlinha][230:242]) for nlinha in range(1, len(arq)-1)]
dic['NÚMERO DE DISTRIBUIÇÃO DO PAPEL'] = [int(arq[nlinha][242:245]) for nlinha in range(1, len(arq)-1)]

#6 Criando Dataframe com Pandas
df_global = pd.DataFrame(dic)
df_global['DATA DO PREGÃO'] = pd.to_datetime(df_global['DATA DO PREGÃO'])
print(df_global)

#9 Informação de finalização do dataframe
tempo2 = time.time()
intervalo1 = round((tempo2 - tempo1), 2)
print('\nDATAFRAME CRIADO COM SUCESSO EM ' + str(intervalo1) + ' SEGUNDOS')

#10 Gerar arquivos
gerar_arquivo(input('\nDIGITE 1 PARA GERAR ARQUIVO CSV\nDIGITE 2 PARA GERAR ARQUIVO XLSX\nDIGITE 3 PARA GERAR ARQUIVOS CSV E XLSX\nDIGITE ENTER PARA ENCERRAR O SCRIPT\n'))