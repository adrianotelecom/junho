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
npc3 = npcs('gustavo', 150, 100)


class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.vida = 100
        self.sanidade = 10
        self.poder = 10
        self.nivel=1
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

print('emquanto jorginho saia de casa ele encontra Gustavo o agiota que ele pegou dinhero emprestado')
print('Gustavo foi a encontro de jorginho para cobrar sua divida e ele nao parecia nada feliz')
print('"jorginho... jorginho sabe que dia é hoje"')
a=input('1=domingo... ?\n2=seu aniversario ?\nfala ? ')
print()
opi=True
while opi == True:
    if (a == '1'):
        print('"sim idiota hoje e domingo dia do meu pagamento, agora passa logo o dinhero')
        opi=False
    elif (a == '2'):
        print('"como você sabia... agora para de ser engraçadinho e da o meu presente')
        opi=False    
    else:
        print('estou começando a ter certeza que você e um idiota , escolha logo 1 ou 2')
        opi=True
        a=input('acão ?')


print()
print('o que o jorginho pode fazer.\n1=lutar contra o agiota para guanhar mais tempo.\n2=ser um bundao e implorara para o agiota mais tempo')
print()
acao = (input('acão ? '))
op = True
while op == True:
    if (acao == '1'):
        opc = 0
        op = False
        while opc == 0:
            print()
            print('jorginho esta confiate que pode descer o agiota na porrada e parte para cima dele acertando um ataque')
            npc3.vida = npc3.vida-personagem.poder
            print()
            print('o agiota fica ainda mais furioso')
            personagem.vida = personagem.vida-npc3.ataque
            print()
            print('o agiota ataca o jorginho com um taco de baseball coberto de arame farpado')
            opc = 0
            acao = (input('escolha : \n\n1=atacar \n2=se ajoelhar e se desculpar\n\nacão ? '))
            if acao == '1':
                print()
                print('jorginho acerta um ataque no safado')
                npc2.vida = npc2.vida-personagem.poder
                print()
                print('jorginho leva uma tacada gostosa')
                personagem.vida = personagem.vida-npc2.ataque
                opc = 0
                acao = (input(
                    'escolha : \n\natacar\n2=se ajoelhar e se desculpar\n\nacão ? '))
                if npc2.vida <= 0:
                    print('depos de jorginho e gustavo trocarem muitos golpes jorginho consegue finalmente acertar o ultimo ataque')
                    print('com a maior felicidade do mundo jorginho saqueia o agiota')
                    print('conseguindo :\n1-uma peruca\n2-um rtaco de baseball\n3-um charuto\n3-R$1.000')
                    opc = 1
                elif personagem.vida <= 0:
                    print('jorginho cai nop chao, no frio, na chuva, com dor e individado ')
                    print('depois do gustavo bricar de saco de pancadas com o jorginho ele pega sua carteira e fala :')
                    print('voce lutou... eu quase suei para te dar uma surra\nvou pegar seu dinhero e te da um praso de mais um mes para voce me pagar, com um pequeno grande juros claro')
                
                    personagem.sanidade -= 10
                    personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                    opc = 1
                    
            elif acao == '2':
                print('')
                personagem.sanidade -= 10
                personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
                opc = 1
                relogio.avancaTempo(20)
            else:
                opc = 0
                print('eu sei que você e meio lerdo mas escolha 1 ou 2')
    elif acao == '2':
        personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
        print('"jorginho...jorginho como eu fui seu professor eu vou te dar mais tempo,com um pequeno juros de 50% o que acha" fala gustavo acendendo umn charuto')
        print('"voce sabe que fazer um mestrado custa caro ne, entao o juros e valido"')
        print('"como um adiantamento me passa tudo que voce tem ai"')
        personagem.sanidade-=10
        personagem.dinheiro = personagem.dinheiro-personagem.dinheiro
        op = False
    else:
        print('eu sei que você e meio lerdo mas escolha 1 ou 2')
        op = True
        acao = (input('acão ? '))


print("""      ▄▄▄▄▄▄▄
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
