#Sistema de elevador de prédio
#O prédio possui 10 andares, sendo o térreo o andad 0. O elevador pode se mover para cima ou para baixo, e tem capacidade de transportar até 5 pessoas.
#O elevador começa no andar 0 e pode ser chamado por qualquer pessoa e qualquer andar.
#O elevador deve se mover para onde a pessoa chamou, e depois para o andar destino da pessoa.
#O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

 #Requisitos funcionais:
#  O elevador deve se mover para cima e para baixo
#  O elevador deve se dirigir no andar que a pessoa escolheu
#  O elevador deve informaas açoes
# O programa deve permitir várias chamadas do elevador.
# O sistema deve encerrar apenas quando o usuário escolher sair.
# Requisitos Não Funcionais

# O sistema deve ser fácil de usar.
# As mensagens exibidas devem ser claras.
# O programa deve responder rapidamente aos comandos.
# O sistema não deve permitir mais de 5 pessoas no elevador.
# O sistema não deve permitir andares menores que 0.
# O sistema não deve permitir andares maiores que 10.
# O programa deve funcionar continuamente até o usuário encerrar.
# O sistema deve evitar erros de entrada inválida.
# O código deve ser organizado e fácil de manter.

# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.


def elevador():
    capacidade_maxima = 5
    andar_maximo = 10
    andar_atual = 0
    import time
    while True:
        print("Bem-vindo ao elevador do prédio! ")
        print("Você está no andar", andar_atual)
        print(f"O elevador tem capacidade para {capacidade_maxima} de pessoas.")
        entrada = int(input("Digite o número do andar que você deseja ir (0-10) "))
        if entrada > 10:
            print("Esse andar não existe... Selecione outro andar!")
        andar_chamado = int(entrada)
        if andar_chamado < 0 or andar_chamado > 10:
            print("Andar inválido. Por favor, digite um número entre 0 e 10.")
            break
        print("Elevador se movendo para o andar", andar_chamado)
        if andar_chamado > andar_atual:
            print("Subindo...")
            for andares in range (entrada):
                print(f"Andar {andares}...")
            time.sleep(0.9)
            print("Elevador chegou ao andar! ")
        elif andar_chamado < andar_atual:
            print("Descendo...")
        else:
            print("O elevador já está no seu andar.")
            andar_atual = andar_chamado
            print("Elevador chegou ao andar", {andar_chamado})
        break

print(elevador())