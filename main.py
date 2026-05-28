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

            if resposta == "x":
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

def modo_descobrir_caracteristicas(assunto, dados, ordem):

    pontuação = 0 
    quantidaAssunto = 0

    sub_assuntos = list(dados[assunto].keys())

    while len(sub_assuntos) > 0:

        print(sub_assuntos,"\n")

        sub_assunto_escolhido = input("Qual sub-assunto: ").strip().lower()

        if sub_assunto_escolhido == "x":
            break

        try: 
            caracteristicas = dados[assunto][sub_assunto_escolhido].copy()
        except:
            print("Sub-assunto não encontrado\n")
            continue

        if ordem == True:

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


        else: #Forma não ordenada

            while len(caracteristicas) > 0:

                resposta = input("Característica: ").strip().lower()

                if resposta == "x":
                    break

                restante = len(caracteristicas) - quantidaAssunto

                melhorCaracteristica = ""

                maiorQuantidade = 0


                for caracteristica in caracteristicas:

                    respostaLista = resposta.split()

                    caracteristicaLista = caracteristica.lower().split()

                    iguais = set(caracteristicaLista) & set(respostaLista)


                    if len(iguais) > maiorQuantidade:

                        maiorQuantidade = len(iguais)

                        melhorCaracteristica = caracteristica


                if melhorCaracteristica == "":

                    print("Nenhuma característica parecida encontrada.\n")

                    continue


                caracteristicaLista = melhorCaracteristica.lower().split()

                quantidadePalavras = len(caracteristicaLista)


                if quantidadePalavras > 0:

                    porcentagem = (maiorQuantidade / quantidadePalavras) * 100

                    pontuação += maiorQuantidade / quantidadePalavras

                else:

                    porcentagem = 0


                if resposta == melhorCaracteristica.lower():

                    print("Perfeito!\n")

                    quantidaAssunto += 1

                elif maiorQuantidade > 0:

                    print(f"Você acertou {maiorQuantidade} de {quantidadePalavras} palavras... {porcentagem:.1f}%")

                    quantidaAssunto += 1

                    print(f"Resposta CORRETA: {melhorCaracteristica}. ainda faltam {restante}\n")

                else:

                    print(f"Nenhuma palavra correspondente encontrada. ainda faltam {restante}")

                    print(f"Resposta CORRETA: {melhorCaracteristica}\n")


                caracteristicas.remove(melhorCaracteristica)

        try:
            porcentagemTotal = (pontuação/quantidaAssunto)*100
        except:
            porcentagemTotal = 0

        print(f"\nFim do sub-assunto... Sua pontuação foi de {pontuação:.2f} de {quantidaAssunto} total / {porcentagemTotal:.1f}%")

#Programa principal
with open("assuntos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

assunto = ""

while assunto != "x":

    assunto = input("Escolha um assunto: ").strip().lower()

    if assunto in dados:

        if assunto.lower() == "direito constitucional":

            modo_descobrir_caracteristicas(assunto, dados, True)

        elif assunto.lower() == "português":

            modo_descobrir_caracteristicas(assunto, dados, False)

        else:

            modo_descobrir_subassunto(assunto, dados)
    
    if assunto == "x":

        print("Finalizando programa em 10s")
        time.sleep(10)
        break

    if assunto not in dados:

        print("assunto não encontrado")