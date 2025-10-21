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
        Ops = input(f"❗ Aperte {Yellow}ENTER{Reset} Para Continuar. ")
        if Ops == '':
            break
        else:
            print(f"❗ Aperte {Red}ENTER{Reset} Para Continuar. 🙃")
            
    os.system('cls' if os.name == 'nt' else 'clear')


from datetime import datetime
def Data_Hora():
    return f"{Ciano_Ligth}{datetime.now.strftime("%d/%m/%Y %H:%M")}{Reset}"


import random
def Random_Conta_Acesso():
    return f"{Ciano_Ligth}{random.randint(0, 999999):06}{Reset}"

def Random_Conta_Cartao(Tipo='Crédito'):
    if Tipo == 'Crédito':
        Prefixo = random.choice(['4', '5'])  # Visa ou MasterCard
    elif Tipo == 'Débito':
        Prefixo = random.choice(['6', '7'])  # Simulação para débito
    else:
        Prefixo = '9'  # Genérico

    Restante = ''.join(random.choices('0123456789', k=15))  # Total 16 dígitos com Prefixo
    Numero = Prefixo + Restante[:15]
    return f"{Ciano_Ligth}{Numero[:4]}.{Numero[4:8]}.{Numero[8:12]}.{Numero[12:16]}{Reset}"
    
import string
def Random_Chave_Pix(Tamanho=32):
    Caracteres = string.ascii_letters + string.digits
    Chave = ''.join(random.choice(Caracteres, k=Tamanho))
    return f"{Ciano_Ligth}{Chave}{Reset}"



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
    return f"{Ciano_Ligth}{Combinar(Valor, Notas)}{Reset}"

def Combinar(Valor, Notas):
    if Valor == 0:
        return True
    
    if Valor < 0:
        return False
    
    for Cada_Nota in Notas:
        if Combinar(Valor - Cada_Nota, Notas):
            return True
    return False



#----------------------------------------
# VERIFICAÕES / Antes da Execução
#----------------------------------------

def Opcoes_Menu():
    while True:
        try:
            Entrada = input(f"💢 {Black}Digite uma Opção:{Reset} ").strip()
            
            if Entrada.isalpha():
                print(f"{Yellow}❗ Letras ou Símbolos são Inválidos.{Reset} {Yellow_Ligth}Digite apenas Números.{Reset} 🙃")
                input(f"❗ Aperte {Yellow}ENTER{Reset} Para Continuar. ")
                continue
            
            if not Entrada.isdigit():
                print(f"{Yellow}❗ Entrada Inválida. Apenas Números Inteiros.{Reset} 🙃")
                input(f"❗ Aperte {Yellow}ENTER{Reset} Para Continuar. ")
                continue
            
            Convert = int(Entrada)
            
            if Convert < 0:
                print(f"{Red}❌ Números Negativos são inválidos.{Reset} 🤔")
                input(f"❗ Aperte {Yellow}ENTER{Reset} Para Continuar. ")
                continue
            
            return Convert
        except ValueError:
            print(f"{Red}❌ Value Error -> Except(Opcoes_Menu){Reset} 🙄")
            input(f"❗ Aperte {Yellow}ENTER{Reset} Para Continuar. ")
            
            
def Ver_Str(Texto=(f"➡ {Black}Texto do Input:{Reset} ")):
    while True:
        Limpar_Terminal()
        try:
            print("Digite 'sair' para voltar.")
            Entrada = input(f"{Texto}: ").strip()
        except ValueError:
            print(f"{Red}❌ Value Error -> Except(Ver_Str){Reset} 🙄")
            continue
         
        if Entrada.lower() == 'sair':
            print(f"{Yellow}❕ Operação Cancelada. Voltando...{Reset}")
            return None
        
        if Entrada == '':
            print(f"{Yellow}⚠ Campo Vazio.{Reset} {Yellow_Ligth}Digite um Nome Válido.{Reset}")
            continue
        
        if len(Entrada) < 3:
            print(f"{Red}Poucas Letras, Nome Inválido.{Reset} {Red_Ligth}Tente Novamente.{Reset}")
            continue
            
        if not Entrada.replace(" ", "").isalpha():
            print(f"{Red}❌ Nome inválido. Use apenas letras.{Reset} {Yellow_Ligth}Evite números ou símbolos.{Reset}")
            continue
        
        return Entrada
            
            
                  
#----------------------------------------
# CLASSE / Cadastrode Clientes
#----------------------------------------
class Cla_Cli:
    def __init__(self, Nome1, Nome2, Idade, Sexo):
        self._Nome1 = Nome1
        self._Nome2 = Nome2
        self._Idade = Idade
        self._Sexo = Sexo
        
    def Get_Nome1(self): return self._Nome1
    def Set_Nome1(self):
        New = Ver_Str(f"➡ {White}Digite seu Primeiro Nome{Reset}")
        if New:
            self._Nome1 = New
            print(f"{Green_Ligth}✅ Informação Salva com Sucesso.{Reset}")
            
    def Get_Nome2(self): return f"{self._Nome2}"
    def Set_Nome2(self):
        New = Ver_Str(f"➡ {White}Digite seu Primeiro Nome{Reset}")
        if New:
            self._Nome2 = New
            print(f"{Green_Ligth}✅ Informação Salva com Sucesso.{Reset}")
            
    def Get_Idade(self): return f"{self._Idade}"
    def Get_Sexo(self): return f"{self._Sexo}"
        
    def Get_Deficiencia(self): return f"Cliente PCD"
    
    def Get_Titular(self): return f"{self._Nome1} {self._Nome2}"
    
    def Get_Info(self):
        print(
            f"\nNome1: {self._Nome1}",
            f"\nNome2: {self._Nome2}",
            f"\nIdade: {self._Idade}",
            f"\nSexo: {self._Sexo}"
        )


Teste_Nome = Cla_Cli("Jose", "Mario", 24, "Masculino")

#----------------------------------------
# SUB-CLASSE / Cadastro de Contas
#----------------------------------------



#----------------------------------------
# MENU PRINCIPAL / Inicialização
#----------------------------------------
def Iniciar():
    while True:
        Limpar_Terminal()
        print(f"{Blue}BANCO SENTAR{Reset}. Bem-Vindo á Agência")
        #print(f"[{Ciano_Ligth}1{Reset}] - Entrar")
        #print(f"[{Ciano_Ligth}2{Reset}] - Cadastrar-se")
        print("1 - Nome")
        print("2 - Ver Nome")
        print("3 - Informações")
        
        try:
            Ops = Opcoes_Menu()
        except ValueError:
            print(f"{Red}❌ Value Error -> Except(Iniciar){Reset} 🙄")
            continue
            
        match Ops:
            case 0: print(f"Saindo... {Ciano}👋🏽 Até outra Hora.{Reset}"); break
            case 1:
                Teste_Nome.Set_Nome1()
            case 2:
                print(f"Nome Atual: {Teste_Nome.Get_Nome1()}")
            case 3:
                print(Teste_Nome.Get_Deficiencia())
                print(Teste_Nome.Get_Titular())
                Teste_Nome.Get_Info()
            case _: print(f"{Red}Não Temos Essa Opção...{Reset} 🙃")
        


if __name__ == '__main__':
    Iniciar()