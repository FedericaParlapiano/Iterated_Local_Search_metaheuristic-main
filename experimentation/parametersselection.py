from statistics import mean

import numpy
import pandas as pd

if __name__ == '__main__':

    log = 'testBank2000NoRandomNoise'

    param1 = 'a0.8_b0.25_g1_T500_iter50_k6'
    param2 = 'a0.8_b0.25_g1_T500_iter50_k2'

    df_1 = pd.read_excel(log + '_recap\iterations\IterationData_' + param1 + "_" + log + '.xlsx')
    df_2 = pd.read_excel(log + '_recap\iterations\IterationData_' + param2 + "_" + log + '.xlsx')

    df_1_time = df_1["time"].tolist()
    df_2_time = df_2["time"].tolist()
    tot_time1 = 0
    tot_time2 = 0

    for i in range(0, len(df_1_time)):
        if str(df_1_time[i]) != 'nan' and str(df_2_time[i]) != 'nan':
            tot_time1 = tot_time1 + df_1_time[i]
            tot_time2 =  tot_time2 + df_2_time[i]

    print('Tot time for parameter configuration' + param1 + ': ' + str(tot_time1))
    print('Tot time for parameter configuration' + param2 + ': ' + str(tot_time2) + '\n')

    df_1_of_now = df_1["fo now"].tolist()
    df_2_of_now = df_2["fo now"].tolist()

    df_1_of_curr = df_1["fo curr"].tolist()
    df_2_of_curr = df_2["fo curr"].tolist()

    df_1_gen = df_1["gen"].tolist()
    df_2_gen = df_2["gen"].tolist()

    smaller_1_of = 0
    smaller_2_of = 0
    equal_fo = 0

    smaller_1_gen = 0
    smaller_2_gen = 0
    equal_gen = 0

    inf = 0
    sup = 49

    iterations1 =[]
    iterations2 = []

    while sup < len(df_1_of_now):
        temp_1_of_now_ = df_1_of_now[inf:(sup + 1)]
        temp_2_of_now_ = df_2_of_now[inf:(sup + 1)]

        temp_1_of_curr_ = df_1_of_curr[inf:(sup + 1)]
        temp_2_of_curr_ = df_2_of_curr[inf:(sup + 1)]

        temp_1_gen = df_1_gen[inf:(sup + 1)]
        temp_2_gen = df_2_gen[inf:(sup + 1)]

        temp_1_of_now = []
        temp_2_of_now = []

        temp_1_of_curr = []
        temp_2_of_curr = []

        for elem in temp_1_of_now_:
            if type(elem) is str:
                temp_1_of_now.append(numpy.nan)
            else:
                temp_1_of_now.append(elem)

        for elem in temp_2_of_now_:
            if type(elem) is str:
                temp_2_of_now.append(numpy.nan)
            else:
                temp_2_of_now.append(elem)

        for elem in temp_1_of_curr_:
            if type(elem) is str:
                temp_1_of_curr.append(numpy.nan)
            else:
                temp_1_of_curr.append(elem)

        for elem in temp_2_of_curr_:
            if type(elem) is str:
                temp_2_of_curr.append(numpy.nan)
            else:
                temp_2_of_curr.append(elem)

        #temp_1_of[:] = (value for value in temp_1_of if type(value) != str)
        #temp_2_of[:] = (value for value in temp_2_of if type(value) != str)

        min_1_of = 0
        min_2_of = 0

        iter1 = 0
        iter2 = 0

        if min(temp_1_of_curr) < min(temp_1_of_now):
            min_1_of = min(temp_1_of_curr)
            iterations1.append(temp_1_of_curr.index(min(temp_1_of_curr)))
            iter1 = temp_1_of_curr.index(min(temp_1_of_curr))

        else:
            min_1_of = min(temp_1_of_now)
            iterations1.append(temp_1_of_curr.index(min(temp_1_of_curr)) + 1)
            iter1 = temp_1_of_curr.index(min(temp_1_of_curr)) + 1

        if min(temp_2_of_curr) < min(temp_2_of_now):
            min_2_of = min(temp_2_of_curr)
            iterations2.append(temp_2_of_curr.index(min(temp_2_of_curr)))
            iter2 = temp_2_of_now.index(min(temp_2_of_now))
        else:
            min_2_of = min(temp_2_of_now)
            iterations2.append(temp_2_of_now.index(min(temp_2_of_now)) + 1)
            iter2 = temp_2_of_now.index(min(temp_2_of_now)) + 1

        if min_1_of > min_2_of:
            smaller_2_of = smaller_2_of + 1
        elif min_1_of < min_2_of:
            smaller_1_of = smaller_1_of + 1
        else:
            equal_fo = equal_fo + 1

        print ('Min parameter configuration ' + param1 + ': ' + str(min_1_of) + ' at iteration ' + str(iter1))
        print ('Min parameter configuration ' + param2 + ': ' + str(min_2_of) + ' at iteration ' + str(iter2)+ '\n')


        sup = sup + 50
        inf = inf + 50

    print('Objective function results')
    print('Smaller case for parameter configuration '+ param1 + ': ' + str(smaller_1_of))
    print('Smaller case for parameter configuration '+ param2 + ': ' + str(smaller_2_of))
    print('Equal case: ' + str(equal_fo))
    print('\n')

    print('Iterations for parameter configuration ' + param1 + ': ' + str(iterations1))
    print("Mean: " + str(mean(iterations1)))

    print('Iterations for parameter configuration ' + param2 + ': ' + str(iterations2))
    print("Mean: " + str(mean(iterations2)))

    iterations1_df = pd.DataFrame(iterations1, columns=["iteration"])
    iterations2_df = pd.DataFrame(iterations2, columns=["iteration"])

    with pd.ExcelWriter("iterations_" + param1 +".xlsx") as writer:
        iterations1_df.to_excel(writer, index=True, header=True)

    with pd.ExcelWriter("iterations_" + param2 +".xlsx") as writer:
        iterations2_df.to_excel(writer, index=True, header=True)










