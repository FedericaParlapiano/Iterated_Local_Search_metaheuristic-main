import numpy
import csv
from decimal import Decimal

from matplotlib import pyplot as plt

from test_function import graph_metric

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

    plt.savefig(metric + '\\trace' + str(trace_id) + 'seed' + str(seed) + '.png')
    # function to show the plot
    plt.show()
    plt.close()

if __name__ == '__main__':


    seed1 = []
    seed2 = []
    seed3 = []

    with open("C:\\Users\\feder\\OneDrive - Università Politecnica delle Marche (1)\\ProgettoBDAML\\Iterated_Local_Search_metaheuristic-main\\IterationData.csv", newline='') as csvfile:

        iteration_data_reader = csv.reader(csvfile, delimiter=';')

        for row in iteration_data_reader:
            x = row[0].split(';')
            x.pop()

            if x[-1] == '1':
                seed1.append(x)
            elif x[-1] == '2':
                seed2.append(x)
            elif x[-1] == '3':
                seed3.append(x)

    prev = 0
    generalization_list = []
    fo_list = []
    for iteration in seed1:
        if iteration[0] == str(prev):
            try:
                generalization_list.append(int(iteration[7]))
            except:
                generalization_list.append(None)
            try:
                if len(iteration) > 8:
                    fo_list.append(Decimal(iteration[3].replace(',', '.')))
                else:
                    fo_list.append(None)
            except:
                fo_list.append(None)
        else:
            graph_metric(prev, generalization_list, 1, "generalization")
            graph_metric(prev, fo_list, 1, "fo")
            prev = iteration[0]
            generalization_list = []
            fo_list = []
            try:
                generalization_list.append(int(iteration[7]))
            except:
                generalization_list.append(None)
            try:
                fo_list.append(Decimal(iteration[3].replace(',', '.')))
            except:
                fo_list.append(None)
    graph_metric(prev, generalization_list, 1, "generalization")
    graph_metric(prev, fo_list, 1, "fo")

    prev = 0
    generalization_list = []
    fo_list = []
    for iteration in seed2:
        if iteration[0] == str(prev):
            try:
                generalization_list.append(int(iteration[7]))
            except:
                generalization_list.append(None)
        else:
            graph_metric(prev, generalization_list, 2, "generalization")
            prev = iteration[0]
            generalization_list = []
            try:
                generalization_list.append(int(iteration[7]))
            except:
                generalization_list.append(None)
    graph_metric(prev, generalization_list, 2, "generalization")

    prev = 0
    generalization_list = []
    for iteration in seed3:
        if iteration[0] == str(prev):
            try:
                generalization_list.append(int(iteration[7]))
            except:
                generalization_list.append(None)
        else:
            graph_metric(prev, generalization_list, 3, "generalization")
            prev = iteration[0]
            generalization_list = []
            try:
                generalization_list.append(int(iteration[7]))
            except:
                generalization_list.append(None)
    graph_metric(prev, generalization_list, 3, "generalization")










