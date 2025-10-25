Projeto Hamiltonian Path Finder
O Hamiltonian Path Finder é um projeto Python desenvolvido para encontrar e visualizar caminhos hamiltonianos em grafos orientados e não orientados. Um caminho hamiltoniano é um caminho em um grafo que visita cada vértice exatamente uma vez.

O Problema do Caminho Hamiltoniano
Um caminho hamiltoniano em um grafo é um caminho que visita cada vértice exatamente uma vez. Diferente do ciclo hamiltoniano, o caminho não precisa retornar ao vértice inicial. Este problema é fundamental na teoria dos grafos e tem aplicações em roteamento, sequenciamento de DNA, e otimização de circuitos.

Algoritmo Implementado
Lógica do Algoritmo
O algoritmo implementado utiliza backtracking para explorar sistematicamente todos os possíveis caminhos no grafo:

python
def find_hamiltonian_path(self, start_node=None):
    if start_node is None:
        start_node = self.nodes[0]
        
    path = [start_node]
    visited = set([start_node])
    
    if self._hamiltonian_util(path, visited):
        return path
    else:
        # Tenta outros nós iniciais
        for node in self.nodes:
            if node != start_node:
                path = [node]
                visited = set([node])
                if self._hamiltonian_util(path, visited):
                    return path
        return None

def _hamiltonian_util(self, path, visited):
    if len(path) == self.n:  # Condição de parada: todos os nós visitados
        return True
        
    current_node = path[-1]
    
    # Obtém vizinhos (considerando direção do grafo)
    if self.graph.is_directed():
        neighbors = list(self.graph.successors(current_node))
    else:
        neighbors = list(self.graph.neighbors(current_node))
        
    for neighbor in neighbors:
        if neighbor not in visited:  # Verifica se o vizinho não foi visitado
            path.append(neighbor)    # Adiciona ao caminho
            visited.add(neighbor)    # Marca como visitado
            
            if self._hamiltonian_util(path, visited):  # Chamada recursiva
                return True
                
            # Backtrack: remove o nó se não levar à solução
            path.pop()
            visited.remove(neighbor)
            
    return False
Explicação Linha a Linha
Inicialização: Começa com um nó inicial e estruturas para rastrear o caminho e nós visitados

Verificação de Completude: Se o caminho contém todos os nós, retorna sucesso

Exploração de Vizinhos: Para cada nó atual, explora todos os vizinhos não visitados

Recursão: Chama recursivamente a função para continuar construindo o caminho

Backtracking: Se um caminho não leva à solução, desfaz a última escolha

Tentativa Alternativa: Se falhar com um nó inicial, tenta outros nós iniciais

Como Executar o Projeto
Dependências
Para rodar este projeto, instale as dependências:

bash
pip install networkx matplotlib
Ambiente Virtual (Recomendado)
Passo 1: Criar e ativar o ambiente virtual
Crie um ambiente virtual:

bash
python3 -m venv .venv
Ative o ambiente virtual:

macOS e Linux:

bash
source .venv/bin/activate
Windows:

bash
.venv\Scripts\activate
Instale as dependências:

bash
pip install networkx matplotlib
Passo 2: Executar o projeto
bash
python main.py
Estrutura dos Arquivos
main.py: Implementa o algoritmo de caminho hamiltoniano e fornece exemplos

view.py: Responsável pela visualização dos grafos e caminhos encontrados

requirements.txt: Lista de dependências do projeto

Relatório Técnico
Análise da Complexidade Computacional
Classes P, NP, NP-Completo e NP-Difícil
1. Classificação do Problema do Caminho Hamiltoniano:

O problema do Caminho Hamiltoniano se enquadra na classe NP-Completo.

2. Justificativa:

NP (Não-Determinístico Polinomial): Dado um candidato a caminho hamiltoniano, podemos verificar em tempo polinomial (O(n)) se ele visita cada vértice exatamente uma vez.

NP-Difícil: O problema é pelo menos tão difícil quanto os problemas mais difíceis em NP. A redução polinomial do Problema do Caixeiro Viajante (TSP) para o Caminho Hamiltoniano demonstra esta propriedade.

NP-Completo: O problema está em NP e é NP-Difícil, caracterizando-o como NP-Completo.

Relação com o Problema do Caixeiro Viajante (TSP):

TSP busca um ciclo hamiltoniano de custo mínimo

Podemos reduzir TSP para Caminho Hamiltoniano atribuindo peso 1 a todas as arestas e verificando se existe algum caminho hamiltoniano

Esta redução polinomial mostra que Caminho Hamiltoniano é pelo menos tão difícil quanto TSP

Análise da Complexidade Assintótica de Tempo
1. Complexidade Temporal do Algoritmo:

A complexidade no pior caso é O(n!) onde n é o número de vértices.

2. Método de Determinação:

Utilizamos contagem de operações baseada na estrutura recursiva do algoritmo:

python
T(n) = (n-1) × T(n-1) + O(n)
     = (n-1) × [(n-2) × T(n-2) + O(n)] + O(n)
     = O(n × (n-1) × (n-2) × ... × 1)
     = O(n!)
Cada chamada recursiva explora até (n-1) vizinhos, e a profundidade máxima da recursão é n.

Aplicação do Teorema Mestre
Não é possível aplicar o Teorema Mestre ao algoritmo de caminho hamiltoniano implementado porque:

O Teorema Mestre aplica-se apenas a recorrências da forma:

text
T(n) = aT(n/b) + f(n)
Nossa recorrência não segue este padrão, sendo uma recorrência de divisão por decremento linear

O algoritmo usa backtracking com exploração combinatorial, não divisão do problema em subproblemas menores de tamanho fixo

Análise dos Casos de Complexidade
1. Diferenças entre os Casos:

Melhor Caso (O(n)): O primeiro caminho tentado é hamiltoniano (grafos completos ou lineares)

Caso Médio (O(n!)): Requer exploração de uma fração significativa do espaço de busca

Pior Caso (O(n!)): Não existe caminho hamiltoniano ou ele é o último a ser verificado

2. Impacto no Desempenho:

Pior Caso: O crescimento fatorial torna o algoritmo impraticável para n > 20

Caso Médio: Ainda exponencial, mas pode encontrar soluções mais rapidamente em grafos esparsos

Melhor Caso: Raro na prática, mas demonstra que a solução pode ser encontrada rapidamente em certas configurações

Fatores que Influenciam o Desempenho:

Densidade do grafo: Grafos mais densos têm mais caminhos possíveis

Estrutura do grafo: Certas topologias (ciclos, árvores) têm comportamento previsível

Ordem de exploração: Heurísticas podem melhorar significativamente o desempenho

Exemplos Incluídos
O projeto inclui 5 grafos de exemplo:

Grafo Não Orientado simples

Grafo Completo K5 (sempre tem caminho hamiltoniano)

Grafo Orientado com ciclo

Grafo Ciclo C6 (sempre tem caminho hamiltoniano)

Grafo desconectado (sem caminho hamiltoniano)