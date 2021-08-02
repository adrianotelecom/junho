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

class jorginho:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.jogar = False
        self.dinheiro = 10
        self.salario = 120
    
    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.jogar else "não ")+"sua sanidade é"+str(self). "Você tem "+str(self.dinheiro)+" reais na sua conta."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.jogar = False

class Casa:
    def __init__(self):
        self.sanidade = 1
        self.comida = 5

if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    jorginho = jorginho()
    casa = Casa()
    cafe_da_manha = False
    while True:
        print("---")
        print("São "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até às 07:00.")
        print(jorginho)
        print("")
        print("Ações:")
        print("1 - Tomar banho e escovar os dentes")
        print("2 - Fazer café da manhã")
        print("3 - Pedir café da manhã")
        print("4 - Tomar café da manhã")
        print("5 - Tomar remédio")
        print("6 - Comprar remédio")
        print("7 - Ir trabalhar")
        print("0 - Sair do jogo")
        opcao = input("Escolha sua ação:")
        if(opcao == "1"):
            jorginho.sujo = False
            relogio.avancaTempo(20)
        elif(opcao == "2"):
            if(casa.comida > 0):
                casa.comida -= 1
                cafe_da_manha = True
            else:
                print("Não há comida em casa.")
            relogio.avancaTempo(15)
        elif(opcao == "3"):
            if(jorginho.dinheiro >= 15):
                jorginho.dinheiro -= 15
                cafe_da_manha = True
            else:
                print("O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
            relogio.avancaTempo(5)
        elif(opcao == "4"):
            if(cafe_da_manha):
                jorginho.fome = False
                cafe_da_manha = False
                relogio.avancaTempo(15)
            else:
                print("Não tem café da manhã na sua casa.")
                relogio.avancaTempo(5)
        elif(opcao == "5"):
            if(casa.sanidade > 0):
                casa.sanidade -= 1
                jorginho.jogar = True
            else:
                print("Não tem remédio na sua casa")
            relogio.avancaTempo(5)
        elif(opcao == "6"):
            if(jorginho.dinheiro >= 20):
                casa.remedios += 10
                jorginho.dinheiro -= 20
                relogio.avancaTempo(10)
            else:
                print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
                relogio.avancaTempo(5)
        elif(opcao == "7"):
            print("-=-=-")
            print("Você foi trabalhar.")
            print(jorginho)
            print("-=-=-")
            recebido = jorginho.salario
            if(not jorginho.medicado):
                print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
                recebido = 0
            elif(jorginho.sujo):
                print("Como você estava sujo, seus colegas reclamaram para seu chefe, e você levou uma advertência.")
                recebido *= 0.9
            elif(jorginho.fome):
                print("Como você estava com fome, você trabalhou metade do que consegue trabalhar.")
                recebido *= 0.5
            elif(relogio.atrasado()):
                print("Como você chegou atrasado, você produziu menos do que de costume.")
                recebido *= 0.8
            print("Você recebeu "+str(recebido)+" reais pelo seu trabalho hoje.")
            print("-=-=-")

            jorginho.dinheiro += recebido
            jorginho.dormir()
            relogio = Relogio()
            dia+=1
        elif(opcao == "0"):
            break
        else:
            print("Opção inválida!")
            relogio.avancaTempo(5)
