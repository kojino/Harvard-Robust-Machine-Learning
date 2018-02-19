from graphviz import Digraph

def tf_to_dot(graph):
    "Visualize TensorFlow graphs on jupyter notebook"

    dot = Digraph()

    for n in graph.as_graph_def().node:
        dot.node(n.name, label=n.name)

        for i in n.input:
            dot.edge(i, n.name)

    return dot
