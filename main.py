import json
import random
import time

def modo_descobrir_subassunto(assunto, dados):

    sub_assuntos = list(dados[assunto].keys())

    random.shuffle(sub_assuntos)

    print("\nPossíveis respostas:\n")

    for i in sub_assuntos:
        print(i)


    while len(sub_assuntos) > 0:

        sub_assunto_escolhido = sub_assuntos.pop()

        caracteristicas = dados[assunto][sub_assunto_escolhido].copy()

        random.shuffle(caracteristicas)


        for numero_pistas, caracteristica in enumerate(caracteristicas, start=1):

            print(f"\nCaracterística {numero_pistas}:")
            print(caracteristica)

            resposta = input("\nQual o sub-assunto? ").strip().lower()

            if assunto == "x":
                break


            if resposta == sub_assunto_escolhido.lower():

                print("\nAcertou!")

                print(f"Você acertou com {numero_pistas} pista(s).")

                break

            else:
                print("\nErrou.")


        else:
            print("\nVocê perdeu.")

            print(f"O sub-assunto era: {sub_assunto_escolhido}")


    print("\nTodos os sub-assuntos acabaram.")

def modo_descobrir_caracteristicas(assunto, dados):

    pontuação = 0 
    quantidaAssunto = 0

    sub_assuntos = list(dados[assunto].keys())

    while len(sub_assuntos) > 0:

        print(sub_assuntos,"\n")

        sub_assunto_escolhido = input("Qual sub-assunto: ").strip().lower()

        if sub_assunto_escolhido == "x":
            break

        caracteristicas = dados[assunto][sub_assunto_escolhido].copy()

        print(f"\nSub-assunto:\n{sub_assunto_escolhido}")

        print("\nDigite as características na ordem CORRETA.\n")


        for posicao, caracteristica in enumerate(caracteristicas, start=1):

            resposta = input(f"Característica {posicao}: ").strip()

            if resposta == "x":
                break
                
            quantidaAssunto += 1

            if resposta.lower() == caracteristica.lower():

                print("Perfeito!\n")
                pontuação += 1

            else:
                #Verifica quantas palavras foram acertadas caso tenha "errado"
                respostaLista = resposta.lower().split()
                caracteristicaLista = caracteristica.lower().split()
                iguais = set(caracteristicaLista) & set(respostaLista)
                porcentagem = (len(iguais)/len(caracteristicaLista))*100
                pontuação += len(iguais)/len(caracteristicaLista)
                print(f"Você acertou {len(iguais)} de {len(caracteristicaLista)} palavras... {porcentagem}%")

                print(f"Resposta CORRETA: {caracteristica}\n")

        try:
            porcentagemTotal = (pontuação/quantidaAssunto)*100
        except:
            porcentagemTotal = 0

        print(f"\nFim do sub-assunto... Sua pontuação foi de {pontuação:.2f} de {quantidaAssunto} total / {porcentagemTotal}%")

#Programa principal
with open("assuntos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

assunto = ""

while assunto != "x":

    assunto = input("Escolha um assunto: ").strip().lower()

    if assunto in dados:

        if assunto.lower() == "direito constitucional":

            modo_descobrir_caracteristicas(assunto, dados)

        else:

            modo_descobrir_subassunto(assunto, dados)
    
    if assunto == "x":

        print("Finalizando programa em 10s")
        time.sleep(10)
        break

    if assunto not in dados:

        print("assunto não encontrado")