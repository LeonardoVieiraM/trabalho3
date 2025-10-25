import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(graph, hamiltonian_path=None, title="Grafo", filename="graph_visualization.png"):
    """
    Visualiza um grafo e destaca o caminho hamiltoniano se existir
    
    Args:
        graph: networkx Graph ou DiGraph
        hamiltonian_path: lista de nós representando o caminho hamiltoniano
        title: título do gráfico
        filename: nome do arquivo para salvar a imagem
    """
    plt.figure(figsize=(12, 8))
    
    # Determinar layout do grafo
    pos = nx.spring_layout(graph, seed=42)
    
    # Desenhar o grafo original
    node_color = 'lightblue'
    edge_color = 'gray'
    node_size = 800
    font_size = 12
    
    # Desenhar nós
    nx.draw_networkx_nodes(graph, pos, 
                          node_color=node_color, 
                          node_size=node_size)
    
    # Desenhar arestas
    nx.draw_networkx_edges(graph, pos, 
                          edge_color=edge_color, 
                          arrows=graph.is_directed(),
                          arrowsize=20,
                          arrowstyle='->',
                          connectionstyle="arc3,rad=0.1")
    
    # Desenhar labels dos nós
    nx.draw_networkx_labels(graph, pos, 
                           font_size=font_size, 
                           font_weight='bold')
    
    # Desenhar labels das arestas
    edge_labels = {(u, v): f"{u}-{v}" for u, v in graph.edges()}
    nx.draw_networkx_edge_labels(graph, pos, 
                                edge_labels=edge_labels,
                                font_size=8)
    
    # Destacar caminho hamiltoniano se existir
    if hamiltonian_path:
        # Destacar nós do caminho
        nx.draw_networkx_nodes(graph, pos, 
                              nodelist=hamiltonian_path,
                              node_color='red', 
                              node_size=node_size)
        
        # Destacar arestas do caminho
        path_edges = []
        for i in range(len(hamiltonian_path) - 1):
            u, v = hamiltonian_path[i], hamiltonian_path[i + 1]
            # Verificar se a aresta existe na direção correta
            if graph.has_edge(u, v):
                path_edges.append((u, v))
            elif not graph.is_directed() and graph.has_edge(v, u):
                path_edges.append((v, u))
        
        if path_edges:
            nx.draw_networkx_edges(graph, pos, 
                                  edgelist=path_edges,
                                  edge_color='red', 
                                  width=3,
                                  arrows=graph.is_directed(),
                                  arrowsize=25,
                                  arrowstyle='->',
                                  connectionstyle="arc3,rad=0.1")
        
        title += f"\nCaminho Hamiltoniano: {' → '.join(map(str, hamiltonian_path))}"
    else:
        title += "\n❌ Nenhum caminho hamiltoniano encontrado"
    
    plt.title(title, fontsize=14, fontweight='bold', pad=20)
    plt.axis('off')
    
    # Adicionar legenda
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='lightblue', markersize=10, label='Nó'),
        plt.Line2D([0], [0], color='gray', linewidth=2, label='Aresta'),
    ]
    
    if hamiltonian_path:
        legend_elements.extend([
            plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Nó do Caminho'),
            plt.Line2D([0], [0], color='red', linewidth=3, label='Aresta do Caminho')
        ])
    
    plt.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))
    
    # Salvar imagem
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Imagem salva como: {filename}")

if __name__ == "__main__":
    # Exemplo de uso direto
    G = nx.cycle_graph(5)
    path = [0, 1, 2, 3, 4]
    visualize_graph(G, path, "Exemplo de Grafo", "exemplo_grafo.png")