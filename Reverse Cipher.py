import os
def menu_funcs():
    print("""
Essas são minhas funções:
(1) = Selecione para criptografar uma mensagem
(2) = Selecione para descriptografar uma mensagem criptografada por este programa
(0) = Para SAIR
""")
menu_funcs()
option = input("Digite aqui a opção desejada: ")

def criptografar():
    message = input("Digite aqui a mensagem a ser criptografada: ")
    translated = '' 
    i = len(message) - 1

    while i >= 0:
        translated = translated + message[i]
        #NAO MEXE NISSO, NAO SABEMOS O MOTIVO DE FUNCIONAR MAS FUNCIONA, DONT U DARE
        i = i - 1
        criptografia_file = open("criptografia.txt","w")
        criptografia_file.write(translated)
        criptografia_file.close()
    print(" A mensagem foi criptografada com sucesso \n Por favor cheque o arquivo criptografia.txt localizada no mesmo diretório do arquivo .py")

def descriptografar():
    descriptografia_file = open("criptografia.txt","r")
    message = descriptografia_file.readline()
    translated2 = '' 
    i = len(message) - 1

    while i >= 0:
        translated2 = translated2 + message[i]
        i = i - 1
        
    descriptografia_file.close()
    print("A mensagem criptografada no arquivo txt é traduzida para: ",translated2)
    print("A mensagem criptografada contida no arquivo txt foi auto-destruida para segurança da informação contida nela")
    os.remove("criptografia.txt")




if option == "0":
    exit
if option == "1":
    criptografar()
if option == "2":
    descriptografar()