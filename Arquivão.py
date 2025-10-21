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
# UTEIS
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