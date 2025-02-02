from final_score.graphs import (
    complete_bipartite_graph_k88,
    complete_bipartite_graph_k_nn,
    cubic_graph_3_16,
    cycle_graph_c8,
    expander_graph_n,
    random_connected_graph_16,
    regular_graph_4_8,
    triangle_graph
)

graph1 = cycle_graph_c8()
graph2 = complete_bipartite_graph_k88()
graph3 = complete_bipartite_graph_k_nn(5)
graph4 = regular_graph_4_8()
graph5 = cubic_graph_3_16()
graph6 = random_connected_graph_16(p=0.18)
graph7 = expander_graph_n(16)
graph8 = triangle_graph()

GRAPH = graph8
SHOTS = 100_000
LR = 0.1
