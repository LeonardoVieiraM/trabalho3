import networkx as nx
from view import visualize_graph

class HamiltonianPathFinder:
    def __init__(self, graph):
        """
        Inicializa o finder de caminhos hamiltonianos
        
        Args:
            graph: networkx Graph ou DiGraph
        """
        self.graph = graph
        self.n = len(graph.nodes())
        self.nodes = list(graph.nodes())
        
    def find_hamiltonian_path(self, start_node=None):
        """
        Encontra um caminho hamiltoniano no grafo
        
        Args:
            start_node: nó inicial (opcional)
            
        Returns:
            list: caminho hamiltoniano ou None se não encontrado
        """
        if start_node is None:
            start_node = self.nodes[0]
            
        path = [start_node]
        visited = set([start_node])
        
        if self._hamiltonian_util(path, visited):
            return path
        else:
            # Tenta outros nós iniciais se o primeiro não funcionar
            for node in self.nodes:
                if node != start_node:
                    path = [node]
                    visited = set([node])
                    if self._hamiltonian_util(path, visited):
                        return path
            return None
    
    def _hamiltonian_util(self, path, visited):
        """
        Função utilitária recursiva para encontrar caminho hamiltoniano
        """
        if len(path) == self.n:
            return True
            
        current_node = path[-1]
        
        # Para grafos direcionados, usa sucessores
        if self.graph.is_directed():
            neighbors = list(self.graph.successors(current_node))
        else:
            neighbors = list(self.graph.neighbors(current_node))
            
        for neighbor in neighbors:
            if neighbor not in visited:
                path.append(neighbor)
                visited.add(neighbor)
                
                if self._hamiltonian_util(path, visited):
                    return True
                    
                # Backtrack
                path.pop()
                visited.remove(neighbor)
                
        return False

def create_example_graphs():
    """
    Cria grafos de exemplo para teste
    """
    graphs = {}
    
    # Exemplo 1: Grafo não orientado simples com caminho hamiltoniano
    G1 = nx.Graph()
    G1.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
    graphs["Grafo Não Orientado 1"] = G1
    
    # Exemplo 2: Grafo completo K5 
    G2 = nx.complete_graph(5)
    # Renomear nós para letras
    mapping = {i: chr(65 + i) for i in range(5)}
    G2 = nx.relabel_nodes(G2, mapping)
    graphs["Grafo Completo K5"] = G2
    
    # Exemplo 3: Grafo orientado com caminho hamiltoniano
    G3 = nx.DiGraph()
    G3.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A'), ('A', 'C')])
    graphs["Grafo Orientado 1"] = G3
    
    # Exemplo 4: Grafo ciclo 
    G4 = nx.cycle_graph(6)
    graphs["Grafo Ciclo C6"] = G4
    
    # Exemplo 5: Grafo sem caminho hamiltoniano
    G5 = nx.Graph()
    G5.add_edges_from([(1, 2), (2, 3), (1, 3)])  # Triângulo
    G5.add_edges_from([(4, 5), (5, 6), (4, 6)])  # Outro triângulo desconectado
    graphs["Grafo Sem Caminho Hamiltoniano"] = G5
    
    return graphs

def main():
    """
    Função principal
    """
    print("=== Encontrando Caminhos Hamiltonianos ===")
    print()
    
    graphs = create_example_graphs()
    
    for graph_name, graph in graphs.items():
        print(f"Analisando: {graph_name}")
        print(f"Número de nós: {len(graph.nodes())}")
        print(f"Número de arestas: {len(graph.edges())}")
        print(f"É orientado: {'Sim' if graph.is_directed() else 'Não'}")
        
        finder = HamiltonianPathFinder(graph)
        hamiltonian_path = finder.find_hamiltonian_path()
        
        if hamiltonian_path:
            print(" Caminho Hamiltoniano encontrado:")
            print(" → ".join(map(str, hamiltonian_path)))
            
            # Visualizar o grafo com o caminho destacado
            filename = f"hamiltonian_path_{graph_name.replace(' ', '_').lower()}.png"
            visualize_graph(graph, hamiltonian_path, graph_name, filename)
            print(f" Visualização salva como: {filename}")
        else:
            print(" Nenhum caminho hamiltoniano encontrado")
            
            # Visualizar o grafo mesmo sem caminho
            filename = f"no_hamiltonian_path_{graph_name.replace(' ', '_').lower()}.png"
            visualize_graph(graph, None, graph_name, filename)
            print(f" Visualização salva como: {filename}")
        
        print("-" * 50)
        print()

if __name__ == "__main__":
    main()