class Relogio:
    def __init__(self):
        self.horas = 5
        self.minutos = 30

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))


class agiota:
    def __init__(self):
        self.divida = 10.000
        self.juros = 10


class npcs:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque


npc1 = npcs('velha', 20, 2)
npc2 = npcs('badido',50, 100)

class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.vida = 100
        self.sanidade = 10
        self.poder = 10
        self.jogar = False
        self.dinheiro = 4
        self.salario = 120

    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "cheirosinho")+", "+("com" if self.fome else "sem")+" fome e "+'sua sanidade é '+str(self.sanidade)+" Você tem R$"+str(self.dinheiro)+" reais na sua conta."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.sanidade -= 1
        self.vida = 100


class Casa:
    def __init__(self):
        self.jogar = False
        self.comida = 15


if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = Personagem()
    casa = Casa()
    cafe_da_manha = False
    passagem = False
    jogar = False

print('so tem um lugar vago no onibus...jorginho e a velha se encaram por 1 minuto. ')
print('a velha sai correndo como se nao tivesse amanha em direçao a cadeora vaga')
print()
print('o que fazer.\n1=atacar.\n2=ser um bundao e ir a viagem toda de pe')
print()
acao = (input('acão ? '))
op = True
while op == True:
    if (acao == '1'):
        opc=0
        op=False
        while opc == 0:
            npc1.vida=npc1.vida-personagem.poder
            print()
            print('jorginho foi correndo e deu uma voadora de dois pes na velha \na velha cai no chao  ')
            print()
            opc=0
            acao = (input('escolha : \n\n1=terminar o serviço\n2=ser bondoso e ir sentar\n\nacão ? '))
            if acao == '1':
                npc1.vida = npc1.vida-personagem.poder
                opc=1
                
                if npc1.vida <=0:
                    print('jorginho termina o serviço e vai sentar' )
                    opc=1        
                elif npc1.vida !=0:
                    opc =0
                    acao = ('escolha : \n\n1=terminar o serviço\n2=ser bondoso e ir sentar\n\nacão ? ')
            elif acao == '2':
                print('jorginho arruma o pentiado e vai se sentar') 
                opc=1  
            else:
                opc=0
                print('voce e burro ou se faz, escolha 1 ou 2')
    elif acao == '2':
        print('jorginho ficou a pé e triste')
        op=False
    else:
        print('voce e burro ou se faz, escolha 1 ou 2')
        op = True
        acao = (input('acão ? '))
