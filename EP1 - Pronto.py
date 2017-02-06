import random
from time import time

# Função Principal
def main():
    #Variaveis Inteiros globais
    global vetor 
    global elemento_pesquisa  
    global inicio_algoritmo
    global fim_algoritmo

    #Inicializando variaveis globais
    elemento_pesquisa = 0
    quant_elementos = 0
    inicio_algoritmo = time()
    fim_algoritmo = time()
    tempo_ordenacao = [4]
    passos = [0,0,0,0]

    imprimir()
    
    while(fim_algoritmo - inicio_algoritmo < 30):
        quant_elementos = quant_elementos + 2000
        vetor = gerarVetor(quant_elementos)      
        num = random.randint(0, len(vetor)) 
        tempo_ordenacao = [cronometra_quicksort(),cronometra_mergesort(),cronometra_insercao(),cronometra_selecao()]  
        
        i = 0
        
        while(i<4):
            passos[i] += contarTempo(tempo_ordenacao[i],vetor,num)
            i+=1
       
        print("| %d  |  %.2f  |  %.2f  |  %.2f |  %.2f  |   %d  |  %d  |  %d  |  %d  |" %(quant_elementos, float(tempo_ordenacao[0]),float (tempo_ordenacao[1]),float(tempo_ordenacao[2]),float(tempo_ordenacao[3]),passos[0],passos[1],passos[2],passos[3]))
        print("|-----------------------------------------------------------------------------|")
        fim_algoritmo = time()


#Função de Impressão
def imprimir():
    print("|------------------------[EP1 - Vale a pena ordenar?]-------------------------|\n"
        "|          Aluno: Aline Dominique da Silva Santos - FATEC - SJC               |\n"
        "|                   Estrutura de Dados - Analise e Desenvolvimento de Sistemas|\n"
        "|           Algoritmo escolhido: Todos                                        |\n"
        "|             Tempos de Ordenacao                   Numero de Buscas          |\n"          
        "|-----------------------------------------------------------------------------|\n"
        "|   n   | Quick. Merge. Insercao  Selecao  |  Quick. Merge. Insercao  Selecao |\n"
        "|-------|---------------------------------------------------------------------|")


#Função do Vetor
def gerarVetor(n):
    copia_vetor =[]
    copia_vetor = list(range(0,n))
    random.shuffle(copia_vetor)
    return copia_vetor

#Inicio das Funções de Ordenação
#Função de Inserção
def insercao(vet):
    for i in range(1, len(vet)):
        val = vet[i]
        j = i - 1
        while(j >= 0) and(vet[j] > val):
            vet[j+1] = vet[j]
            j = j - 1
        vet[j+1] = val

#Função de Seleção
def selecao(vet):
    n=len(vet)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if(vet[j]<vet[mini]):
                mini=j
        vet[i],vet[mini]=vet[mini],vet[i]

#Começa o MergeSort
def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(vet):
    if len(vet) <= 1:
        return vet
    else:
        meio = len(vet) // 2
        menor = mergesort(vet[:meio])
        maior = mergesort(vet[meio:])
        return merge(menor, maior)

def separa(p, r, v):
    k = t = 0
    c = v[r]
    k = j = p
    while k < r:
        if(v[k] <= c):
           t = v[j]
           v[j] = v[k]
           v[k] = t
           j += 1
        k += 1
    v[r] = v[j]
    v[j] = c
    return j
# Termina o Mergesort

#Inicia o Quicksort
def quicksort(v):
    if len(v) <= 1: 
        return v
    pivô = v[0]
    iguais = [x for x in v if x == pivô]
    menores = [x for x in v if x <  pivô]
    maiores = [x for x in v if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)
# Termina Quicksort


#Funções de obtenção dos tempos das Ordenações
#Obtendo tempo das funções de ordenação

def cronometra_quicksort():
     tempo_quicksort = time()
     quicksort(vetor)
     return time() - tempo_quicksort
    
def cronometra_insercao():
    tempo_insercao = time()
    insercao(vetor)
    return time() - tempo_insercao

def cronometra_selecao():
    tempo_selecao  = time()
    selecao(vetor)
    return  time() - tempo_selecao

def cronometra_mergesort():
    tempo_megersort = time()
    mergesort(vetor)
    return  time() - tempo_megersort


#Método de Busca Sequencial
def BuscaSequencial(v, x):
    j = 0
    while j < len(v) and v[j] < x:
        j += 1
    return j

#Método de Busca Binaria
def BuscaBinaria(v, x):
    e = -1
    d = len(v)
    while e < d - 1: 
          m = (e + d)//2
          if (v[m] < x):
              e = m
          else:
              d = m
    return d

#Funções de obtenção dos tempos das buscas
#Obtendo tempo das funções de buscas
def cronometra_BuscaSequencial(v,x):
    comeca = time()
    BuscaSequencial(v,x)
    return time() - comeca

def cronometra_BuscaBinaria(v,x):
    comeca = time()
    BuscaBinaria(v,x)
    return time() - comeca


# Função contar o Tempo
def contarTempo(tempo_Ordenacao,vetor,num):
    total_Binaria = 0
    total_Sequencial = 0
    numeroBuscas = 0
    i = 0
    
    while (total_Sequencial<tempo_Ordenacao + total_Binaria):
        tempo_Sequencial = cronometra_BuscaSequencial(vetor,num)
        tempo_Binaria = cronometra_BuscaBinaria(vetor,num)
            
        total_Binaria+=tempo_Binaria
        total_Sequencial+= tempo_Sequencial

        numeroBuscas+=1
            
    return numeroBuscas
        
# Fim das funções de tempo de Busca


#chamada da função principal
main()

