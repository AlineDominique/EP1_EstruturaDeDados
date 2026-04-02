# 🎓 EP1 - Estrutura de Dados: Vale a pena ordenar?

> **Curso:** Análise e Desenvolvimento de Sistemas (3º Semestre) -  FATEC São José dos Campos

> **Tópico:** Analise de Algoritmo e Performace do Sortinge

Este repositório contém o código do primeiro Exercício Prático (EP1) da disciplina de Estrutura de Dados. O objetivo do projeto foi realizar uma análise empírica comparando algoritmos de ordenação e busca para responder a uma pergunta clássica: *Quando o custo de ordenar um vetor é compensado pela eficiência da busca binária?*

## 🧠 O Experimento
O programa executa um benchmark automatizado que:
1. Gera vetores aleatórios com tamanhos progressivos ($n$).
2. Cronometra o tempo de execução de quatro algoritmos de ordenação.
3. Calcula quantas buscas são necessárias para que o tempo "gasto" na ordenação seja recuperado pela performance da **Busca Binária** frente à **Busca Sequencial**.

## 🛠 Algoritmos Implementados
O estudo abrange diferentes classes de complexidade:
- **Ordenação:** QuickSort, MergeSort, Insertion Sort e Selection Sort.
- **Busca:** Busca Sequencial ($O(n)$) e Busca Binária ($O(\log n)$).

## 📊 Resultados Esperados
Através da tabela gerada pelo script, é possível visualizar o crescimento da ineficiência dos algoritmos $O(n^2)$ (Inserção/Seleção) em comparação aos de dividir e conquistar $O(n \log n)$ (Quick/Merge), conforme o volume de dados aumenta.

---

**Matéria:** Estrutura de Dados e Análise de Algoritmos

**Professor:** Fernando Masanori Ashikaga

**Estudante:** Aline Dominique da Silva Santos  

**Linguagem:** Python 3.x (Compatível com versões 3.0+)
