from _csv import writer

import numpy
from matplotlib import pyplot as plt
from pm4py.objects.petri_net.importer import importer as pnml_importer
from pm4py.visualization.petri_net import visualizer as pn_visualizer
import graphviz
import os


def division(num, den, dec):
    if den == 0:
        return 0
    else:
        return round(num / den, dec)


def file_print(path, text, mode='a'):
    # text = list of any type of data I want to save on file
    if type(text) is list or type(text) is tuple:
        string = ''
        for t in text:
            string += str(t) + ';'
    else:
        string = str(text)
    string = string.replace('.', ',')
    with open(path, mode, newline='') as filep:
        writer_object = writer(filep, delimiter=";")
        writer_object.writerow([string])
        filep.close()


def save_graph(fname, nodes, arcs, check=False):
    if check:
        file_print(fname, 'XP', 'w')
    else:
        file_print(fname, 'XP', 'a')
    for v in nodes:
        string = 'v ' + str(v[0]) + ' ' + v[1]
        file_print(fname, string)
    for w in arcs:
        string = 'e ' + str(w[0][0]) + ' ' + str(w[1][0]) + ' ' + w[0][1] + ' ' + w[1][1]
        file_print(fname, string)

def save_graph_traceid(fname, nodes, arcs, trace, check=False):
    if check:
        file_print(fname, 'XP ' + str(trace), 'w')
    else:
        file_print(fname, 'XP ' + str(trace), 'a')
    for v in nodes:
        string = 'v ' + str(v[0]) + ' ' + v[1]
        file_print(fname, string)
    for w in arcs:
        string = 'e ' + str(w[0][0]) + ' ' + str(w[1][0]) + ' ' + w[0][1] + ' ' + w[1][1]
        file_print(fname, string)

def import_graph(path):
    print("\nRead ig from file ")
    with open(path) as file:
        node_id = 0
        nodes = []
        edges = []
        while True:
            line = file.readline()
            if not line:
                break
            elif line.strip() == 'XP' or line.strip() == '':
                continue
            else:
                line = line.strip().replace("\n", '')
                dat = line.split(' ')
                if dat[0] == 'v':
                    nodes.append((node_id, dat[2]))
                    node_id += 1
                elif dat[0] == 'e':
                    n_in_id = int(dat[1])
                    n_out_id = int(dat[2])
                    n_in = nodes[n_in_id]
                    n_out = nodes[n_out_id]
                    edges.append((n_in, n_out))

    print("lista di nodi:", nodes)
    print("lista di archi:", edges)
    return nodes, edges

def import_graph_big(path):
    print("\nRead ig from file ")
    with open(path) as file:
        node_id = 0
        nodes = []
        edges = []
        while True:
            line = file.readline()
            if not line:
                break
            elif line.strip() == 'XP' or line.strip() == '':
                continue
            else:
                line = line.strip().replace("\n", '')
                dat = line.split(' ')
                if dat[0] == 'v':
                    nodes.append((node_id, str(dat[1]) + '_' + str(dat[2])))
                    node_id += 1
                elif dat[0] == 'e':
                    n_in_id = int(dat[1])
                    n_out_id = int(dat[2])
                    n_in = nodes[n_in_id]
                    n_out = nodes[n_out_id]
                    edges.append((n_in, n_out))

    print("lista di nodi:", nodes)
    print("lista di archi:", edges)
    return nodes, edges

def import_graph_bpi(path):
    print("\nRead ig from file ")
    with open(path) as file:
        node_id = 0
        nodes1 = []
        edges1 = []
        nodes2 = []
        edges2 = []
        nodes3 = []
        edges3 = []
        seed = 0
        while True:
            line = file.readline()

            if not line:
                break
            elif line.strip() == 'XP' or line.strip() == '':
                continue
            elif line.strip() == '*** Seed: 1 ***':
                seed = 1
                node_id = 0
                continue
            elif line.strip() == '*** Seed: 2 ***':
                seed = 2
                node_id = 0
                continue
            elif line.strip() == '*** Seed: 3 ***':
                seed = 3
                node_id = 0
                continue
            else:
                line = line.strip().replace("\n", '')
                dat = line.split(' ')
                if dat[0] == 'v':
                    if seed == 1:
                        nodes1.append((node_id, str(dat[1]) + '_' + str(dat[2])))
                    if seed == 2:
                        nodes2.append((node_id, str(dat[1]) + '_' + str(dat[2])))
                    if seed == 3:
                        nodes3.append((node_id, str(dat[1]) + '_' + str(dat[2])))
                    node_id += 1
                elif dat[0] == 'e':
                    n_in_id = int(dat[1])
                    n_out_id = int(dat[2])
                    if seed == 1:
                        n_in = nodes1[n_in_id]
                        n_out = nodes1[n_out_id]
                        edges1.append((n_in, n_out))
                    if seed == 2:
                        n_in = nodes2[n_in_id]
                        n_out = nodes2[n_out_id]
                        edges2.append((n_in, n_out))
                    if seed == 3:
                        n_in = nodes3[n_in_id]
                        n_out = nodes3[n_out_id]
                        edges3.append((n_in, n_out))

    print("lista di nodi1:", nodes1)
    print("lista di archi1:", edges1)
    print("lista di nodi2:", nodes2)
    print("lista di archi2:", edges2)
    print("lista di nodi3:", nodes3)
    print("lista di archi3:", edges3)
    return nodes1, edges1, nodes2, edges2, nodes3, edges3

def draw_graph(nodes, edges, path):
    nodes_ = []
    edges_ = []

    for n in nodes:
        nodes_.append(n[1])

    for e in edges:
        edges_.append([e[0][1], e[1][1]])

    dot = graphviz.Digraph(comment='Prova')

    for n in nodes_:
        dot.node(n)

    for e in edges_:
        dot.edge(e[0], e[1], constraint='true')

    # print(nodes_)
    # print(edges_)

    print(dot.source)
    print(graphviz.__file__)
    dot.render('ig/big/' + path + '.gv', view=True)

    return

def draw_petri_net(net_path):

    net, initial_marking, final_marking = pnml_importer.apply(net_path)

    parameters = {pn_visualizer.Variants.WO_DECORATION.value.Parameters.FORMAT: "svg"}
    gviz = pn_visualizer.apply(net, initial_marking, final_marking, parameters=parameters)
    pn_visualizer.view(gviz)

def graph_metric(trace_id, list, seed, metric):
    # funzione usata per graficare i valori della generalizzazione della traccia i-esima ad ogni iterazione
    # x axis values
    iterations = []
    for i in range(0, 50):
        iterations.append(i)

    # plotting the points
    plt.plot(iterations, list)
    # naming the x axis
    plt.xlabel('iteration')
    # naming the y axis
    plt.ylabel(metric)

    # giving a title to my graph
    plt.title('Trace ' + str(trace_id) + ' Seed ' + str(seed))

    if metric == 'generalization':
        plt.yticks(numpy.arange(0, 100000, 10000.0))
    if metric == 'fo':
        plt.yticks(numpy.arange(0, 100000, 10000.0))

    plt.savefig('test\\' + metric + '\\trace' + str(trace_id) + 'seed' + str(seed) + '.png')
    # function to show the plot
    #plt.show()


