import chardet

with open('Emendas.csv', 'r', encoding='ISO-8859-1') as old_file:
    rows = old_file.readlines()

with open('emendas_utf8.csv', 'w', encoding='UTF-8', newline='\n') as new_file:
    new_file.writelines(rows)

print("Arquivo convertido para UTF-8 com sucesso.")
