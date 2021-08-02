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

npc1=npcs('Joaquim',30,1)


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

    def __str__(self):
        return "jorginho está " + ("fedendo" if self.sujo else "cheirosinho")+", "+("cheio de" if self.fome else "sem")+" fome e "+'sua sanidade é '+str(self.sanidade)+" Você tem R$: "+str(self.dinheiro) + " reais na sua conta."+'Seu nivel é '+str(self.nivel)

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
        print("São "+str(relogio)+" do dia "+str(dia) +". Você tem que sair pro trabalho até às 07:00.")
        print(personagem)
        print("")
        print("Ações:")
        print("1 - tomar banho")
        print("2 - Fazer o rango")
        print("3 - Pedir um ifood")
        print("4 - Tomar café da manhã")
        print("5 - jogar")
        print("6 - Ir trabalhar")
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
                print("O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
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
            print("-=-=-"*25)
            print("1- Hoje vou fazer uma caminhada.")
            print("2- Rere vou de baique")
            op = input('escolha uma maneira de ir para o trabalho : ')
        if(op == '1'):
            print('')
            relogio.avancaTempo(25)
            opc = 1
            print('Jorginho sai de casa logo cedo para seu primeiro dia de trabalho, logo na primeira esquina encontra um mendigo: ')
            print('O mendigo vendo Jorginho o aborda! O irmão se não tem uma ajuda pro café ai não?')
            print('Jorginho todo nervoso pelo seu primeiro dia de serviço?\n 1 = Lembrar do GTA(socar ele de porrada).\n 2 = Jorginho entrega o que tem ao mendigo!')
            print()
            acao = (input('acão ? '))
            op = True
            while opc == 1:
                npc1.vida = npc1.vida-personagem.poder
                print('Jorginho se irrita com o mendigo e começa o encher de porrada  ')
                opc = 0
                acao = (input('O mendigo esta insanguentado Jorginho decide: \n 1 = Jogar ele em uma lata de lixo? \n 2 = Deixar para ver se alguem o ajuda? \n Ação? '))
                if acao == '1':
                    npc1.vida = npc1.vida-personagem.poder
                    print('Jorginho o agarra pela camisa e o arasta até os tambores de lixo!')
                    print('\n\n Jorginho o deixa e sai sorridente, porem apos tudo isso ele acaba se ferrando pois acaba de perder todo o seu dinheiro R$:',str(personagem.dinheiro),"reais")
                    opc = 1
                    personagem.sanidade-=4
                    personagem.dinheiro -= personagem.dinheiro
                    personagem.salario = 0
                    personagem.nivel+=1
                    personagem.poder+=5
                elif (acao == '2'):
                    print('Jorginho sai falando headshot') 
                    print('let s go, quem sera o prossimo? Vamos! vai trabalhar rapaz. Nem eu tomei café da manha!')   
                    personagem.nivel+=1                                    
                    opc = 1
                else:
                    opc = 0
                    print('você e burro ou se faz, escolha 1 ou 2')

        elif op == '2':
            print('O mendigo agradesse! Jorginho acaba de achar R$: ',str(personagem.salario))
            op = False
            personagem.sanidade+=20
            personagem.salario += personagem.salario == 120
                                        
            if(acao == '2'):
                print("-=-=-"*25)
                print("1- Volta para casa.")
                print("2- Opa! vou trabalhar para pagar logo o Gustavo rere")
                op = input('Jorginho decide: ')#Colocar a opção escolhida(1 ou a dois inves de aparecer o numero)
                if(op == ''):
                    if (personagem.dinheiro >= 5):
                        personagem.dinheiro += 120
                        print('O juros ja está quase garantido!')
                        relogio.avancaTempo(720)
                        personagem.sanidade == 48
                        opc = 1
                        print('Jorginho volta para casa e passa o dia jogando video game, sua sanidade almenta em: ',str(personagem.sanidade))
                                                            
                    elif(acao == '2'):
                        personagem.salario+=360
                        print('jorginho decide ir trabalhar apesar de chegar atrasado ainda consegue uma boa grana R$: ',str(personagem.salario))

                    else:
                        print('escolha umas das duas opçoes validas')
                        opc = 0
                                        
                    print(personagem)
                    print("-=-=-"*25)
                    recebido = personagem.salario
                    if(personagem.sanidade < 1):
                        print("você esta de saco cheio da vida e decide voltar para casa e jogar o dia todo")
                        recebido = 0
                    elif(personagem.sujo):
                        print("Como você estava sujo, o seu chefe não aguentou o seu cheiro e te mandou para casa mais cedo .")
                        recebido *= 0.8
                    elif(personagem.fome):
                        print("você estava com fome, e não teve um rendimento bom no trampo.")
                        recebido *= 0.5
                    elif(relogio.atrasado()):
                        print("alem de chegar atrasado você teve que escutar muitas reclamações do seu chefe.Você produziu menos do que de costume.")
                        personagem.sanidade -= 1
                        recebido *= 0.8
                    print("Você recebeu "+str(recebido) +" reais pelo seu trabalho hoje.")
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
