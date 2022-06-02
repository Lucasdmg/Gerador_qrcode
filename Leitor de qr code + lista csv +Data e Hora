"""Lucas Domingues Dos Santos"""

arquivo = open('novo-arquivo.csv', 'w')
arquivo.close()
import datetime
print(20*"-*")
while True:
    arquivo = open('novo-arquivo.csv', 'r')  # Abra o arquivo (leitura)
    conteudo = arquivo.readlines()
    code = input("QR CODE >> ")
    print(20 * "-*")
    conteudo.append(code)
    hora =datetime.datetime.now()
    hora= str(hora)
    conteudo.append(" ")
    conteudo.append(hora)
    conteudo.append("\n")
    arquivo = open('novo-arquivo.csv', 'w')  # Abre novamente o arquivo (escrita)
    arquivo.writelines(conteudo)
    arquivo.close()
