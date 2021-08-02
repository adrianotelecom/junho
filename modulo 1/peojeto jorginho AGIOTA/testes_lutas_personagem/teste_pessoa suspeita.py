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

npc1_0 = npcs('suspeito',20,5)
npc1 = npcs('velha', 20, 5)
npc2 = npcs('badido', 50, 100)


class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.vida = 100
        self.sanidade = 10
        self.poder = 10
        self.nivel = 1
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

print('jorginho estava correndo e encontrou uma pessoa suspeita com um sobre tudo. ')
print('a pesssoa suspeita se aproxima de jorginho e fala enquanto coloca a mão dentro do sobre tudo:')
print('"ola queridinho você quer um docinho"')
ac=input('1=que tipo de doce ?\n2=hummm...minha mâe me ensinou a não pegar doces de estranos\n fala ? ')
print()
cpo=True
while cpo == True:
    if (ac == '1'):
        cpo= False
        print('"você vai adorar eu garanto" a pessoa suspeita fala enquanto abre o sobre tudo e sai correndo para cima do jorginho com um biquine de baixo do sobre tudo')
    elif (ac == '2'):
        cpo=False
        print('"não seja timido voce vai adorar" a pessoa suspeita fala enquanto abre o sobre tudo e sai correndo para cima do jorginho com um biquine de baixo do sobre tudo')
    else:
        print('serio quer que eu desenhe, escolhe logo 1 ou 2')
        cpo=True
        ac=input('ação ? ')
print()
print('o que fazer.\n1=atacar com toda sua força.\n2=esperar a pessoa suspeita chegar perto para ganhar um doce\n')
print()
acao = (input('acão ? '))
op = True
while op == True:
    if (acao == '1'):
        opc = 0
        op = False
        while opc == 0:
            npc1.vida = npc1.vida-personagem.poder
            print()
            print(
                'jorginho deu um chute nas partes baixar do homem suspeito \na pessoa suspeita cai de joelhos no chao ')
            print()
            opc = 0
            acao = (input(
                'escolha : \n\n1=terminar o serviço\n2=ser bondoso e terminar o serviço\n\nacão ? '))
            if acao == '1':
                npc1.vida = npc1.vida-personagem.poder
                opc = 1

                if npc1.vida <= 0:
                    print('jorginho chuta o o queixo de seu inimigo que logo depois desmaia')
                    opc = 1
                    personagem.sanidade-=2
                    personagem.nivel+=1
                    personagem.poder+=10
                    print('jorginho mesmo ganhando a luta sente que perdeu algo...talvez sua sanidade.\nmas pelo lado bom jorginho subiu de nivel seja la o que isso significa')
                    print('como um bom jogador de RPG mesmo não querendo jorginho saqueia seu inimigo')
                    print('ele pega : \n1-um biquine\n2-um objeto longo de borracha com um cheiro ruim(talvez de para usar como arma)')
                    personagem.poder+=5
                elif npc1.vida != 0:
                    opc = 0
                    acao = (
                        'escolha : \n\n1=terminar o serviço\n2=ser bondoso e terminar o serviço\n\nacão ? ')
            elif acao == '2':
                print('jorginho chuta o o queixo de seu inimigo que logo depois desmaia')
                opc = 1
                personagem.sanidade-=2
                personagem.nivel+=1
                personagem.poder+=10
                print('jorginho mesmo ganhando a luta sente que perdeu algo...talvez sua sanidade.\nmas pelo lado bom jorginho subiu de nivel seja la o que isso significa')
                print('como um bom jogador de RPG mesmo não querendo jorginho saqueia seu inimigo')
                print('ele pega : \n1-um biquine\n2-um objeto longo de borracha com um cheiro ruim(talvez de para usar como arma)')
                personagem.poder+=5
            else:
                opc = 0
                print('serio quer que eu desenhe, escolhe logo 1 ou 2')
    elif acao == '2':
        print('jorginho não lembra muito bem o que aconteceu... mas ele tem certeza que não ganhou nem um doce so dificuldades para andar e ficar sentado')
        op = False
        personagem.sanidade-=5
        relogio.avancaTempo(30)
    else:
        print('serio quer que eu desenhe, escolhe logo 1 ou 2')
        op = True
        acao = (input('acão ? '))
