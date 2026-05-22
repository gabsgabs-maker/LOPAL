#Símbolo d
# 1. Cadastro de Funcionários:
# ○ Armazene o nome, setor e o status dos treinamentos (NR-10, NR-35 e
# Brigada).

# 2. Verificação de EPI (NR-6):
# ○ O sistema deve receber o setor do funcionário.
# ○ Se o setor for "Elétrica", liste a obrigatoriedade de luvas de alta tensão e
# botas dielétricas.
# ○ Se o setor for "Trabalho em Altura", liste o cinturão de segurança e
# talabarte.
tempo_ultimo_treinamento= 2
print("Olá! Seja bem vindo ao sitema de cadastro de funcionários da Brigada.")
print("Por favor preencha as informações abaixo.")
nome = input("Digite o seu nome: ")
setor= input("Digite o seu setor: ")
treinamentos = input("Você já realizou os treinamentos?: (NR-10, NR-35 ou Brigada)  (Sim ou Não) ")
treinamentos_feitos =("NR-10, NR-35 ou Brigada")

if treinamentos == "Sim":
    print("Okay, você realizou os treinamentos disponiveis!")
    treinamentos_feitos = ("Qual foi o treinamento realizado? (NR-10, NR-35 ou Brigada) ")
    print("Ok ! seus dados froam registrados com sucesso! ")
if treinamentos=="Não":
    print("Por favor, volte e realize os treinamentos necessários o mais rápido possível !!!")

print(input("Quanto tempo faz desde o seu ultimo treinamento?: "))
if tempo_ultimo_treinamento <= 2 :
    print("Válido!")

elif tempo_ultimo_treinamento >= 2 :
    print("Treinamento Vencido! Encaminhar para reciclagem.")
