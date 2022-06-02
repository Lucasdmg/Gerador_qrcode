import openpyxl
import qrcode

def intervalo(inicio, fim):
    return range(inicio, fim + 1)

pasta_de_trabalho = openpyxl.load_workbook('C:\\Users\\Administrador\\Desktop\\teste1.xlsx')  # Caminho do arquivo
planilha = pasta_de_trabalho['MATRICULADOS']  # Nome da Planilha
for coluna in intervalo(1, 1):
    for linha in intervalo(1, 3):
        linha1=planilha.cell(row=linha, column=coluna).value
        img=qrcode.make(linha1)
        img.save(f'{linha1}.png')
