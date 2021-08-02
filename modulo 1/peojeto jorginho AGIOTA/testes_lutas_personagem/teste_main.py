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
    def __init__(self,nome,vida,ataque):
        self.nome=nome
        self.vida=vida
        self.ataque=ataque

npc1=npcs('velha',15,2)


class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.vida=100
        self.poder=10
        self.nivel=1
        self.sanidade = 10
        self.jogar = False
        self.dinheiro = 4
        self.salario = 120
        self.divida=10.000
    def __str__(self):
        return "jorginho está " + ("fedendo" if self.sujo else "cheirosinho")+", "+("cheio de" if self.fome else "sem")+" fome e "+'sua sanidade é '+str(self.sanidade)+" Você tem R$"+str(self.dinheiro)+" reais na sua conta."+'seu nivel é '+str(self.nivel)+'sua divida é '+str(self.divida)

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.sanidade -= 1
        self.vida=100


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
    while True:
        print("---")
        print("São "+str(relogio)+" do dia "+str(dia) +
              ". Você tem que sair pro trabalho até às 07:00.")
        print(personagem)
        print("")
        print("Ações:")
        print("1 - tomar banho")
        print("2 - Fazer o rango")
        print("3 - Pedir um ifood")
        print("4 - Tomar café da manhã")
        print("5 - jogar ps5")
        print("6 - Ir trabalhar")
        print('7 - ir para o mercado')
        print("0 - Sair do jogo")
        opcao = input("Escolha sua ação:")
        if(opcao == "1"):
            personagem.sujo = False
            relogio.avancaTempo(15)
        elif(opcao == "2"):
            if(casa.comida > 0):
                casa.comida -= 1
                cafe_da_manha = True
            else:
                print("Não há comida em casa.")
            relogio.avancaTempo(15)
        elif(opcao == "3"):
            if(personagem.dinheiro >= 15):
                personagem.dinheiro -= 15
                cafe_da_manha = True
            else:
                print(
                    "O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
            relogio.avancaTempo(5)
        elif(opcao == "4"):
            if(cafe_da_manha):
                personagem.fome = False
                cafe_da_manha = False
                relogio.avancaTempo(15)
            else:
                print("Não tem café da manhã na sua casa.")
                relogio.avancaTempo(5)
        elif(opcao == "5"):
            personagem.sanidade += 2
            relogio.avancaTempo(60)

        elif(opcao == "6"):
            opc = 0
            while opc == 0:
                print("-=-=-"*25)
                print("1- ir trabalhar de onibus (custa R$5.00).")
                print("2- ir trabalhar na sola")
                op = input('escolha uma maneira de ir para o trabalho : ')
                if(op == '1'):
                    if (personagem.dinheiro >= 5):
                        personagem.dinheiro -= 5
                        print('perdeu 5 pila')
                        relogio.avancaTempo(25)
                        opc = 1
                        if dia == 2:
                            print(
                                'so tem um lugar vago no onibus...jorginho e uma velha se encaram por 1 minuto. ')
                            print('a velha sai correndo como se não tivesse amanha em direçao ao lugar vago')
                            print('o que fazer.\n1=atacar.\n2=ser um bundao e ir a viagem toda de pe')
                            print()
                            acao = (input('acão ? '))
                            op = True
                            while op == True:
                                if(acao == '1'):
                                    op = False
                                    opc = 0
                                    while opc == 0:
                                        npc1.vida = npc1.vida-personagem.poder
                                        print(
                                            'jorginho foi correndo e deu uma voadora de dois pes na velhinha \na velhinha cai no chao  ')
                                        opc = 0
                                        acao = (input(
                                            'escolha entre \n1=terminar o serviço \n2=ser bondoso e ir sentar\nação ? '))
                                        if acao == '1':
                                            npc1.vida = npc1.vida-personagem.poder
                                            print(
                                                'jorginho ja jogou muito RPG para saber que é hora de saquear\nele consegur : \nR$ 5,00\n1 passe livre para idosos')
                                            print('jorginho pisa na velhinha e vai sentar')
                                            print('\n\nemquanto jorginho esta sentado ele sente sua sanidade diminuindo , porem algo dentro dele mudou.')
                                            opc = 1
                                            personagem.sanidade-=1 
                                            personagem.nivel+=1
                                            personagem.poder+=10
                                            personagem.vida+=50
                                        elif acao == '2':
                                            print('jorginho arruma o pentiado e vai se sentar') 
                                            print('emquanto jorginho esta sentado ele sente que algo dentro dele mudou')   
                                            personagem.nivel+=1   
                                            personagem.vida+=50                                 
                                            opc = 1
                                        else:
                                            opc = 0
                                            print('você e burro ou se faz, escolha 1 ou 2')
                                elif(acao == '2'):
                                    print('jorginho vai a viagem a pé e triste, porem sente que fez algo bom')
                                    op = False
                                    personagem.sanidade+=1
                                else:
                                    op = True
                                    print('voce e burro ou se faz, escolha 1 ou 2')
                                    acao = (input('acão ? '))

                    else:
                        print('você esta liso, não tem dinheiro para a passagem')
                        opc = 1
                elif (op == '2'):
                    relogio.avancaTempo(60)
                    print('voce chegou atrasado no trampo , seu chefe esta puto da vida')
                    opc = 1
                    personagem.sanidade -= 1
                    

                else:
                    print('escolha umas das duas opçoes validas')
                    opc = 0

            print(personagem)
            print("-=-=-"*25)
            recebido = personagem.salario
            if(personagem.sanidade < 1):
                print(
                    "você esta de saco cheio da vida e decide voltar para casa e jogar o dia todo")
                recebido = 0
            elif(personagem.sujo):
                print(
                    "Como você estava sujo, o seu chefe não aguentou o seu cheiro e te mandou para casa mais cedo .")
                recebido *= 0.8
            elif(personagem.fome):
                print("você estava com fome, e não teve um rendimento bom no trampo.")
                recebido *= 0.5
            elif(relogio.atrasado()):
                print("alem de chegar atrasado você teve que escutar muitas reclamações do seu chefe.Você produziu menos do que de costume.")
                personagem.sanidade -= 1
                recebido *= 0.8
            print("Você recebeu "+str(recebido) +
                  " reais pelo seu trabalho hoje.")
            print("-=-=-"*25)

            personagem.dinheiro += recebido
            personagem.dormir()
            relogio = Relogio()
            dia += 1
        elif(opcao == "0"):
            break
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)
