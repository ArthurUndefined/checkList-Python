atividadeResposta = []

def askAtividade():

    if(atividadeResposta == []):
        print("Sem atividades!")
    else:
        print(atividadeResposta)

    def criarAtividade():
        global atividadeResposta
        atividadeResposta.append(input("Digite uma nova atividade: "))
        askAtividade()

    escolha = int(input("1.Criar atividade \n2.Dar pronto na atividade\n"))

    if(escolha == 1):
        criarAtividade()
    if(escolha == 2):
        return

askAtividade()