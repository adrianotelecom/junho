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
npc2 = npcs('badido', 50, 50)
npc3 = npcs('gustavo',150, 100)

class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.vida = 100
        self.sanidade = 10
        self.nivel=1
        self.poder = 30
        self.jogar = False
        self.dinheiro = 4
        self.salario = 120

    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "cheirosinho")+", "+("com" if self.fome else "sem")+" fome e "+'sua sanidade é '+str(self.sanidade)+" Você tem R$"+str(self.dinheiro)+" reais na sua conta."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.sanidade -= 1
        self.vida = self.vida


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

print('quando jorginho estava correno para não chegar atrasado no trampo ele encontra uma pessoa de capuz')
print('a pessoa de capuz fala para jorginho ')
print("se você quiser continuar correndo passa a carteira")
print()
print('o que fazer.\n1=ser corajoso uma vez na vida e atacar.\n2=ser um bundao e passar a grana para o assaltante')
print()
acao = (input('acão ? '))
op= True
while op == True:
    if (acao == '1'):
        opc = 0
        op = False
        while opc == 0:
            print()
            print('jorginho lembra dos anime que asistiu pela madrugada e pensa que é um protagonista e parte para cima do assaltante')
            npc2.vida = npc2.vida-personagem.poder
            print()
            print('assaltante olha com cara de curiosidade para jorginho e contra ataca ele com um chute na barriga')
            personagem.vida=personagem.vida-npc2.ataque
            print()
            print('jorginho perde o ar mas continua em pé')
            opc = 0
            acao = (input(
                'escolha : \n\n1=ser idiota e atacar novamente\n2=ser um bundao e passar a carteira\n\nacão ? '))
            if acao == '1':
                print()
                print('jorginho lembra que um protagonista nunca desiste vai atacar o assaltante de novo')
                npc2.vida = npc2.vida-personagem.poder
                print()
                print('jorginho leva um ataque')
                personagem.vida = personagem.vida-npc2.ataque
                opc = 0
                acao = (input(
                    'escolha : \n\n1=ser idiota e atacar\n2=ser um bundao\n\nacão ? '))
                if npc2.vida <= 0:
                    print('jorginho quase perdendo a consciência mas consegue dar o ataque final em seu inimigo')
                    personagem.sanidade+=2
                    print('jorginho como um bom jogador de RPG saqueia o corpo do assaltante\nitens adiquiridos :\nfaca\nR$300\n1 maço de derbi')
                    personagem.nivel+=1
                    personagem.poder+=20
                    personagem.vida+=100
                    opc = 1   
                elif personagem.vida <= 0:
                    print('depos de apanhar muito jorginho desmaia')
                    personagem.sanidade -= 4
                    personagem.dinheiro=personagem.dinheiro-personagem.dinheiro
                    opc=1
                    relogio.avancaTempo(30)
                    print('depois de um tempo jorginho acorda ,com seu copo dolorido e sem sua carteira mesmo com dificuldade ele vai para o trampo')
                    print('quando jorginho chega na firma ele estranhamente sente dificuldade para ficar sentado e trabalha o resto do dia todo em pé')
            elif acao == '2':
                print('jorginho viu que não tinha como vencer e entraga a carteira para o assaltante')
                personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                personagem.sanidade-=4
                opc = 1
                relogio.avancaTempo(20)
            else:
                opc = 0
                print('voce e burro ou se faz, escolha 1 ou 2')
    elif acao == '2':
        personagem.dinheiro=personagem.dinheiro-personagem.dinheiro
        print(f'jorginho passa a carteira para o assaltante e perde todo seu dinhero e sua dignidade')
        relogio.avancaTempo(15)
        op= False
    else:
        print('voce e burro ou se faz, escolha 1 ou 2')
        op = True
        acao = (input('acão ? '))



print("""    ▄▄▄▄▄▄▄
░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░
░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░
░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░
░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░
░░░░░█░░▀░░░░░░░░░░░░░░░░▀░""")
