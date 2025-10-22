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
    return f"{Blue}{datetime.now.strftime("%d/%m/%Y %H:%M")}{Reset}"

# Armazenamento das Contas
Contas_Acesso = []
Chaves_Pix = []

import random
def Random_Conta_Acesso():
    return f"{Blue}{random.randint(0, 999999):06}{Reset}"
    


def Random_Conta_Cartao(Tipo='Crédito'):
    if Tipo == 'Crédito':
        Prefixo = random.choice(['4', '5'])  # Visa ou MasterCard
    elif Tipo == 'Débito':
        Prefixo = random.choice(['6', '7'])  # Simulação para débito
    else:
        Prefixo = '9'  # Genérico

    Restante = ''.join(random.choices('0123456789', k=15))  # Total 16 dígitos com Prefixo
    Numero = Prefixo + Restante[:15]
    return f"{Blue}{Numero[:4]}.{Numero[4:8]}.{Numero[8:12]}.{Numero[12:16]}{Reset}"
    
import string
def Random_Chave_Pix(Tamanho=32):
    Caracteres = string.ascii_letters + string.digits
    Chave = ''.join(random.choices(Caracteres, k=Tamanho))
    return f"{Blue}{Chave}{Reset}"


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
            print(f"{Red}❌ Value Error -> Except(Ver_Str()){Reset} 🙄")
            continue
         
        if Entrada.lower() == 'sair':
            print(f"{Yellow}❕ Operação Cancelada. Voltando...{Reset}")
            return None
        
        if Entrada == '':
            print(f"{Yellow}⚠ Campo Vazio.{Reset} {Yellow_Ligth}Digite um Dado Válido.{Reset}")
            continue
        
        if len(Entrada) < 3:
            print(f"{Red}Poucas Letras. Quantidade Inválida.{Reset} {Red_Ligth}Tente Novamente.{Reset}")
            continue
        
        if len(Entrada) > 15:
            print(f"{Red}Não deve ter mais que 15 Letras. Quantidade Inválida.{Reset} {Red_Ligth}Tente Novamente.{Reset}")
            continue
            
        if not Entrada.replace(" ", "").isalpha():
            print(f"{Red}❌ Dado Inválido. Use apenas Letras.{Reset} {Yellow_Ligth}Evite Números ou Símbolos.{Reset}")
            continue
        
        return Entrada
    
    
def Ver_Senha():
    while True:
        Limpar_Terminal()
        
        try:
            print("Digite 'sair' para voltar.")
            Entrada = input(f"Digite a Senha (4 Dígitos): ").strip()
        except ValueError:
            print(f"{Red}❌ Value Error -> Except(Ver_Str()){Reset} 🙄")
            continue
        
        if Entrada.lower() == 'sair':
            print(f"{Yellow}❕ Operação Cancelada. Voltando...{Reset}")
            return None
        
        if Entrada == '':
            print(f"{Yellow}⚠ Campo Vazio.{Reset} {Yellow_Ligth}Digite uma Senha Válida.{Reset}")
            continue
            
        if not Entrada.replace(" ", "").isdigit():
            print(f"{Red}❌ Senha Inválida. Use apenas Números.{Reset} {Yellow_Ligth}Evite Letras ou Símbolos.{Reset}")
            continue
            
        if len(Entrada) < 4:
            print(f"{Red}Senha Inválida.{Reset} {Red_Ligth}Tente Novamente.{Reset}")
            print(f"Senha deve conter {Yellow}4 Dígitos{Reset}")
            continue
        
        if len(Entrada) > 4:
            print(f"{Red}Senha Inválida.{Reset} {Red_Ligth}Tente Novamente.{Reset}")
            print(f"Senha deve conter {Yellow}4 Dígitos{Reset}")
            continue

        return Entrada
    
def Ver_Idade():
    while True:
        Limpar_Terminal()
        
        try:
            print("Digite 'sair' para voltar.")
            Entrada = input(f"Digite sua Idade (+ 18): ").strip()
        except ValueError:
            print(f"{Red}❌ Value Error -> Except(Ver_Idade()){Reset} 🙄")
            continue
        
        if Entrada.lower() == 'sair':
            print(f"{Yellow}❕ Operação Cancelada. Voltando...{Reset}")
            return None
        
        if Entrada == '':
            print(f"{Yellow}⚠ Campo Vazio.{Reset} {Yellow_Ligth}Digite uma Senha Válida.{Reset}")
            continue
        
        if not Entrada.replace(" ", "").isdigit():
            print(f"{Red}❌ Idade Inválida. Use apenas Números.{Reset} {Yellow_Ligth}Evite Letras ou Símbolos.{Reset}")
            continue
        
        Convert = int(Entrada)
        
        if Convert < 18:
            print(f"{Yellow}Você têm que ter 18 anos ou mais, para criar uma conta{Reset}")
            continue
        
        if Convert > 120:
            print(f"{Yellow}Idade não pode ser maior que 120")
            continue
        
        return Convert
            
                  
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
        New = Ver_Str(f"➡ {White}Digite seu Segundo Nome{Reset}")
        if New:
            self._Nome2 = New
            print(f"{Green_Ligth}✅ Informação Salva com Sucesso.{Reset}")
            
    def Get_Idade(self): return f"{self._Idade}"
    def Set_Idade(self):
        New = Ver_Idade()
        if New:
            self._Idade = New
            print(f"{Green_Ligth}✅ Informação Salva com Sucesso.{Reset}")
    
    def Get_Sexo(self): return f"{self._Sexo}"
    def Set_Sexo(self):
        New = Ver_Str(f"➡ {White}Digite seu Sexo{Reset}")
        if New:
            self._Sexo = New
            print(f"{Green_Ligth}✅ Informação Salva com Sucesso.{Reset}")
        
    def Get_Deficiencia(self): return f"Cliente PCD"
    
    def Get_Titular(self): return f"{Blue_Ligth}{self._Nome1} {self._Nome2}{Reset}"
    
    def Get_Info(self):
        print(
            f"\nNome1: {self._Nome1}",
            f"\nNome2: {self._Nome2}",
            f"\nIdade: {self._Idade}",
            f"\nSexo: {self._Sexo}"
        )


Teste_Nome1 = Cla_Cli("Jose", "Rivaldo", 24, "Masculino")
Teste_Nome2 = Cla_Cli("Carlos", "Sérgio", 19, "Masculino")
Teste_Nome3 = Cla_Cli("Maria", "Luisa", 23, "Feminina")

#----------------------------------------
# SUB-CLASSE / Cadastro de Acesso
#----------------------------------------
class Cla_Ac(Cla_Cli):
    def __init__(self, Nome1, Nome2, Idade, Sexo, Senha):
        super().__init__(Nome1, Nome2, Idade, Sexo)
        
        self._Senha = Senha
        self._Saldo = 0.0
        self._Conta_Acesso = Random_Conta_Acesso()
        self._Extrato = []
        
    def Get_Senha(self): return self._Senha
    def Set_Senha(self):
        New = Ver_Senha()
        if New:
            self._Senha = New
            print(f"{Green_Ligth}✅ Informação Salva com Sucesso.{Reset}")
            
    def Get_Saldo(self): return self._Saldo
        
    def Get_Acesso(self): return self._Conta_Acesso
    def Get_Extrato(self): return self._Extrato
    
    def Config_User(self):
            while True:
                Limpar_Terminal()
                print("-" * 60)
                print(f"Titular: {self.Get_Titular()} | N° da Conta: {self._Conta_Acesso}")
                print(f"Saldo Atual: R$ {self.Get_Saldo():.2f}")
                print("-" * 60)
                print(f"{White}{'Coluna'.center(17)}{Reset} | {White}{'Dados'.center(15)}{Reset} | {White}{'Opções'.center(17)}{Reset}")
                print(f"{'Primeiro Nome':<17} | {self.Get_Nome1():<15} | {f'[{Ciano_Ligth}1{Reset}] - Alterar':<17}")
                print(f"{'Segundo Nome':<17} | {self.Get_Nome2():<15} | {f'[{Ciano_Ligth}2{Reset}] - Alterar':<17}")
                print(f"{'Idade':<17} | {self.Get_Idade():<15} | {f'[{Ciano_Ligth}3{Reset}] - Alterar':<17}")           
                print(f"{'Sexo':<17} | {self.Get_Sexo():<15} | {f'[{Ciano_Ligth}4{Reset}] - Alterar':<17}")
                print(f"{'Senha':<17} | {self.Get_Senha():<15} | {f'[{Ciano_Ligth}5{Reset}] - Alterar':<17}")
                print("-" * 60)
                print(f"[{Ciano_Ligth}0{Reset}] - Voltar...")
                print()
                
                Ops = Opcoes_Menu()
                
                match Ops:
                    case 0: print(f"Voltando... 🙃"); break
                    case 1: self.Set_Nome1()
                    case 2: self.Set_Nome2()
                    case 3: self.Set_Idade()
                    case 4: self.Set_Sexo()
                    case 5: self.Set_Senha()
                    case _: print(f"{Red}Não Temos Essa Opção...{Reset} 🙃")



#----------------------------------------
# SUB-CLASSE / Cadastro de Contas
#----------------------------------------
class Cla_Cns(Cla_Ac):
    def __init__(self, Nome1, Nome2, Idade, Sexo, Senha):
        super().__init__(Nome1, Nome2, Idade, Sexo, Senha)
        
        self._Contas_Cartao = Random_Conta_Cartao()
        self._Chaves_Pix = Random_Chave_Pix()
        
    def Get_Cns_Ct(self): return self._Contas_Cartao
    def Get_Cns_Pix(self): return self._Chaves_Pix
    
    def Criar_Cns_Ct(self):
        Numero = self._Contas_Cartao
        Contas_Cartao.append(Numero)
        return Numero
    
    def Criar_Cns_Pix(self):
        Numero = self._Chaves_Pix
        Chaves_Pix.append(Numero)
        return Numero
    
    

#----------------------------------------
# Clientes / Usuário -> Cadastrados
#----------------------------------------
def Lista_Cns_Ct():
    for i, C in enumerate(Contas_Cartao):
        print(f"[{i}] - {C}")


def Lista_Cns_Pix():
    for i, C in enumerate(Chaves_Pix):
        print(f"[{i}] - {C}")

#----------------------------------------
# CONFIGURAÇÃO / Usuário -> Agência
#----------------------------------------

Teste_Nome4 = Cla_Ac("Cara", "Zorel", 29, "Feminina", "0123")
Cns1 = Cla_Cns("Nion", "Lara", 34, "Masculino", "0123")


#----------------------------------------
# MENU / Agência
#----------------------------------------
def Menu_Ag():
    while True:
        Limpar_Terminal()
        print(f"[{Ciano_Ligth}1{Reset}] - Configurações")
        print(f"[{Ciano_Ligth}2{Reset}] - Transferências")
        print(f"[{Ciano_Ligth}3{Reset}] - Extrato")
        print(f"[{Ciano_Ligth}4{Reset}] - Saque")
        print(f"[{Ciano_Ligth}5{Reset}] - Depósito")
        print(f"[{Ciano_Ligth}0{Reset}] - Voltar...")
        
        try:
            Ops = Opcoes_Menu()
        except ValueError:
            print(f"{Red}❌ Value Error -> Except(Entrar()){Reset} 🙄")
            continue
        
        match Ops:
            case 0: print(f"Voltando... 🙃"); break
            case 1: Teste_Nome4.Config_User()
            case _: print(f"{Red}Não Temos Essa Opção...{Reset} 🙃")



#----------------------------------------
# MENU / Caixa Eletrônico
#----------------------------------------
def Menu_Cx():
    while True:
        Limpar_Terminal()
        print(f"[{Ciano_Ligth}1{Reset}] - Transferência Entre Contas")
        print(f"[{Ciano_Ligth}2{Reset}] - Saque")
        print(f"[{Ciano_Ligth}3{Reset}] - Depósito")
        print(f"[{Ciano_Ligth}4{Reset}] - Extrato")
        print(f"[{Ciano_Ligth}5{Reset}] - Saldo Atual")
        print(f"[{Ciano_Ligth}0{Reset}] - Voltar...")
        
        try:
            Ops = Opcoes_Menu()
        except ValueError:
            print(f"{Red}❌ Value Error -> Except(Entrar()){Reset} 🙄")
            continue
        
        match Ops:
            case 0: print(f"Voltando... 🙃"); break                            
            case _: print(f"{Red}Não Temos Essa Opção...{Reset} 🙃")
            
            
            
#----------------------------------------
# SUB-MENU / Agência - Caixa Eletrônico
#----------------------------------------
def SubMenu():
    while True:
        Limpar_Terminal()
        print(f"[{Ciano_Ligth}1{Reset}] - Ir na Agencia")
        print(f"[{Ciano_Ligth}2{Reset}] - Ir no Caixa Eletrônico")
        print(f"[{Ciano_Ligth}0{Reset}] - Voltar...")
        
        try:
            Ops = Opcoes_Menu()
        except ValueError:
            print(f"{Red}❌ Value Error -> Except(Entrar()){Reset} 🙄")
            continue
        
        match Ops:
            case 0: print(f"Voltando... 🙃"); break
            case 1:
                Menu_Ag()
            case 2:
                Menu_Cx()                
            case _: print(f"{Red}Não Temos Essa Opção...{Reset} 🙃")
        
        

#----------------------------------------
# CADASTRO / Entrada Interface
#----------------------------------------

Lista_Clientes = []

def Interface_Cadastro():
        
    print("Cadastro de Usuários")
    Nome1 = Ver_Str("Primeiro Nome")
    Nome2 = Ver_Str("Segundo Nome")
    Idade = Ver_Idade()
    Sexo = Ver_Str("Sexo")
    New = Cla_Cli(Nome1, Nome2, Idade, Sexo)
    
    New.Get_Info()
    Lista_Clientes.append(New)
    
    return



#----------------------------------------
# MENU PRINCIPAL / Inicialização
#----------------------------------------
def Iniciar():
    while True:
        Limpar_Terminal()
        print(f"Seja Bem-Vindo ao {Blue}BANCO SENTAR{Reset}.")
        print(f"[{Ciano_Ligth}1{Reset}] - Entrar")
        print(f"[{Ciano_Ligth}2{Reset}] - Cadastrar-se")
        print(f"[{Ciano_Ligth}0{Reset}] - Sair...")
        
        try:
            Ops = Opcoes_Menu()
        except ValueError:
            print(f"{Red}❌ Value Error -> Except(Iniciar()){Reset} 🙄")
            continue
            
        match Ops:
            case 0: print(f"Saindo... 🙃{Ciano} Até outra Hora.{Reset}"); break
            case 1:
                #Inter_Entrar()
                SubMenu()
            case 2:
                Interface_Cadastro()
            case 3:
                print("Cliente")
                Lista_Clientes()
                    
            case _: print(f"{Red}Não Temos Essa Opção...{Reset} 🙃")
        


if __name__ == '__main__':
    Iniciar()