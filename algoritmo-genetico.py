from random import randint, random
import math



def gera_populacao(tamanho_papulacao, tamanho_individuo):
    populacao = []
    for p in range(tamanho_papulacao):
        individuo = ''
        for i in range(tamanho_individuo):
            individuo += str(randint(0,1))
        populacao.append(individuo)
    return populacao



#retorna individuo convertido de binário para decimal
def bin_to_dec(individuo):
    return int(individuo, 2)



def crossover(populacao, taxa):

    nova_populacao = []
    
    i = 0
    while i < len(populacao):
        pai = populacao[i]
        mae = populacao[i + 1]
        i += 2

        filho = ''
        filho += pai[0:int(len(pai)*taxa)]
        filho += mae[int(len(mae)*taxa):len(mae)]
        nova_populacao.append(filho)

        filho = ''
        filho += mae[0:int(len(pai)*taxa)]
        filho += pai[int(len(mae)*taxa):len(mae)]
        nova_populacao.append(filho)

    return nova_populacao



def mutacao(populacao, taxa):

    for individuo in populacao:

        l = list(individuo)
        aux = 0
        for i in l:
            if random() <= taxa:
                print('Mutou!') 
                if i == '0':
                    l[aux] = '1'
                else:
                    l[aux] = '0'
            aux += 1
        novo_individuo = ''.join(l)

        populacao.remove(individuo)
        populacao.append(novo_individuo)

    return populacao



# função de ajuste
def get_x(min, max, b):
    x = min+(max+min)*(bin_to_dec(b)/2**len(b)-1)
    return x



# essa é a função a ser minimizada
def aptidao(x):
    f = x*math.sin(10*math.pi*x)+1
    return f


 
def torneio(populacao, tamanho_populacao):

    nova_populacao = []

    for i in range(tamanho_populacao):
        k = randint(0, tamanho_populacao-1)
        j = randint(0, tamanho_populacao-1)

        if bin_to_dec(populacao[k]) > bin_to_dec(populacao[j]):
            nova_populacao.append(populacao[k])
        else:
            nova_populacao.append(populacao[j])
    
    return nova_populacao



# main

populacao = []

tamanho_populacao = 4
tamanho_individuo = 22
numero_geracoes = 5
taxa_crossover = 0.6
taxa_mutacao = 0.01
selecao = 'c'   # 't' para torneio; 'c' para classificação

# gera população
populacao = gera_populacao(tamanho_populacao, tamanho_individuo)
print('população inicial: ', populacao)

# executa conforme o número de gerações
for g in range(numero_geracoes):
    print('Geração: ', g+1)

    if selecao == 'c':
        populacao.sort(reverse=True)
    else:
        populacao = torneio(populacao, tamanho_populacao)

    print('população após seleção: ', populacao)

    # realiza crossover
    populacao = crossover(populacao, taxa_crossover)
    print('população após crossover: ', populacao)

    # realiza mutação
    populacao = mutacao(populacao, taxa_mutacao)
    print('população após mutação:  ', populacao)

    #imprime a aptião dos indivíduos
    print('População apta: ')
    for individuo in populacao:
        # -1 e 2 são o intervalo a que x pertence
        print(aptidao(get_x(-1, 2, individuo)))

