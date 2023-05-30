import contatos_converter

try:
    contatos = contatos_converter.csv_para_contatos('contatos.csv', 'windows-1252')

    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email} ')

except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Acesso ao arquivo negado')
