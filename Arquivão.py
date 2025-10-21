#----------------------------------------
# CORES
#----------------------------------------
Black = '\033[3;30m'
Red = '\033[1;31m'
Green = '\033[1;32m'
Yellow = '\033[1;33m'
Blue = '\033[1;34m'
Magenta = '\033[1;35m'
Ciano = '\033[1;36m'
White = '\033[1;37m'
Cinza_Escuro = '\033[1;90m'

# Claras
Red_Ligth = '\033[1;91m'
Green_Ligth = '\033[1;92m'
Yellow_Ligth = '\033[1;93m'
Blue_Ligth = '\033[1;94m'
Magenta_Ligth = '\033[1;95m'
Ciano_Ligth = '\033[1;96m'
White_Ligth = '\033[1;97m'

# Back Ground para os Fundos
Fundo_Black = '\033[1;40m'
Fundo_Red = '\033[1;41m'
Fundo_Green = '\033[1;42m'
Fundo_Yellow = '\033[1;43m'
Fundo_Blue = '\033[1;44m'
Fundo_Magenta = '\033[1;45m'
Fundo_Ciano = '\033[1;46m'
Fundo_White = '\033[1;47m'

# Marcação de Textos
Reset = '\033[0m'
Bold = '\033[1m'
Fraco = '\033[2m'
Italico = '\033[3m'
Underline = '\033[4m'
Piscando = '\033[5m'
Reverse = '\033[7m'
Riscado = '\033[9m'



#----------------------------------------
# UTEIS / Configurações
#----------------------------------------

# Ideia da IA
import os
def Limpar_Terminal():
    while True:
        Ops = input(f"❗ Aperte {Yellow_Ligth}ENTER{Reset} Para Continuar")
        if Ops == '':
            break
        else:
            print(f"❗ Aperte {Red_Ligth}ENTER{Reset} Para Continuar")
            
    os.system('cls' if os.name == 'nt' else 'clear')


from datetime import datetime
def Data_Hora():
    return datetime.now.strftime("%d/%m/%Y %H:%M")


import random
def Random_Conta_Acesso():
    return f"{random.randint(0, 999999):06}"

def Random_Conta_Cartao(Tipo='Crédito'):
    if Tipo == 'Crédito':
        Prefixo = random.choice(['4', '5'])  # Visa ou MasterCard
    elif Tipo == 'Débito':
        Prefixo = random.choice(['6', '7'])  # Simulação para débito
    else:
        Prefixo = '9'  # Genérico

    Restante = ''.join(random.choices('0123456789', k=15))  # Total 16 dígitos com Prefixo
    Numero = Prefixo + Restante[:15]
    return f"{Numero[:4]}.{Numero[4:8]}.{Numero[8:12]}.{Numero[12:16]}"
    
import string
def Random_Chave_Pix(Tamanho=32):
    Caracteres = string.ascii_letters + string.digits
    Chave = ''.join(random.choice(Caracteres, k=Tamanho))
    return Chave



# Armazenamento das Contas
Contas_Acesso = []
Contas_Cartao = []
Chaves_Pix = []

# Notas Aceitas no Caixa Eletrônico
Notas_Aceitas = [20, 50, 100]

# Validar Valores de Entrada e Saída no Caixa Eletrônico
def Valor_Validado(Valor, Notas):
    if Valor < 0:
        return False
    return Combinar(Valor, Notas)

def Combinar(Valor, Notas):
    if Valor == 0:
        return True
    
    if Valor < 0:
        return False
    
    for Cada_Nota in Notas:
        if Combinar(Valor - Cada_Nota, Notas):
            return True
    return False