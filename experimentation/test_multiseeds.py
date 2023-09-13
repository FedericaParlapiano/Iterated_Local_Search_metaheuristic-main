import numpy
import pandas as pd

def iterations(iterations_df, iter, param, log):
    inf = 0
    sup = iter - 1

    df_of_now = iterations_df["fo now"].tolist()
    df_of_curr = iterations_df["fo curr"].tolist()

    seed_list = iterations_df["seed"].tolist()
    id_list = iterations_df["trace id"].tolist()

    iterations_list = []

    i = 0

    while sup < len(df_of_now):
        temp_of_now_ = df_of_now[inf:(sup + 1)]
        temp_of_curr_ = df_of_curr[inf:(sup + 1)]

        temp_of_now = []
        temp_of_curr = []

        for elem in temp_of_now_:
            if type(elem) is str:
                temp_of_now.append(numpy.nan)
            else:
                temp_of_now.append(elem)

        for elem in temp_of_curr_:
            if type(elem) is str:
                temp_of_curr.append(numpy.nan)
            else:
                temp_of_curr.append(elem)

        if min(temp_of_curr) < min(temp_of_now):
            '''
            iterations_list[i].append(seed_list[temp_of_curr.index(min(temp_of_curr))])
            iterations_list[i].append(id_list[temp_of_curr.index(min(temp_of_curr))])
            iterations_list[i].append(temp_of_curr.index(min(temp_of_curr)))'''
            iterations_list.append([
                seed_list[inf],
                id_list[inf],
                temp_of_curr.index(min(temp_of_curr))
            ])
        else:
            iterations_list.append([
                seed_list[inf],
                id_list[inf],
                temp_of_now.index(min(temp_of_now)) + 1
            ])
            '''
            iterations_list[i].append(seed_list[temp_of_now.index(min(temp_of_now)) + 1])
            iterations_list[i].append(id_list[temp_of_now.index(min(temp_of_now)) + 1])
            iterations_list[i].append(temp_of_now.index(min(temp_of_now)) + 1)'''

        sup += iter
        inf += iter
        i += 1

    iterations_df = pd.DataFrame(iterations_list, columns=["seed", "trace id", "min iterations"])

    with pd.ExcelWriter(log + "_recap\\iterations\\" + log + "_min_iterations_" + param + ".xlsx") as writer:
        iterations_df.to_excel(writer, index=True, header=True)

def avg_iter(seed_iterations, meta_iterations):
    avg_iterations = [0, 0, 0]
    i = 0
    c = [0, 0, 0]

    for s in range(1, 4):
        while i < len(seed_iterations) and seed_iterations[i] == s:
            avg_iterations[s - 1] += meta_iterations[i]
            c[s - 1] += 1
            i += 1
        avg_iterations[s - 1] /= c[s - 1]

    return avg_iterations

def gen(gen_big, gen_meta):
    diff = []
    smaller_big_gen = 0
    smaller_meta_gen = 0
    equal_gen = 0

    i = 0

    while i < len(gen_meta):
        try:
            diff_gen = gen_big[i] - gen_meta[i]
            diff_pow = pow(diff_gen, 2)
            diff.append(diff_pow)
            traces.append([i, gen_big[i], gen_meta[i], diff_pow])

            if diff_gen < 0:
                smaller_big_gen += 1
            elif diff_gen > 0:
                smaller_meta_gen += 1
            else:
                equal_gen += 1
        except:
            diff.append(None)
            traces.append([i, gen_big[i], gen_meta[i], None])
        i += 1

    mse = 0
    n = 0
    for elem in diff:
        if elem != None:
            mse += elem
            n += 1

    mse /= n

    return smaller_big_gen, smaller_meta_gen, equal_gen, mse

def move(move_big, move_meta):
    i = 0
    smaller_big_move = 0
    smaller_meta_move = 0
    equal_move = 0
    meta_fail_move = 0

    while i < len(move_meta):
        if move_meta[i] != '-':
            diff_moves = move_big[i] - move_meta[i]
            traces[i].append(move_big[i])
            traces[i].append(move_meta[i])
            traces[i].append(diff_moves)
            if diff_moves < 0:
                smaller_big_move += 1
            elif diff_moves > 0:
                smaller_meta_move += 1
            else:
                equal_move += 1
        else:
            traces[i].append(move_big[i])
            traces[i].append(move_meta[i])
            traces[i].append(None)
            meta_fail_move += 1
        i += 1

    return smaller_big_move, smaller_meta_move, equal_move, meta_fail_move

def edges(edges_big, edges_meta):
    smaller_big_edges = 0
    smaller_meta_edges = 0
    equal_edges = 0

    avg_edges_big = 0
    avg_edges_meta = 0
    c1 = 0
    c2 = 0
    i = 0

    while i < len(edges_big):
        try:
            diff_edges = edges_big[i] - edges_meta[i]
            if diff_edges < 0:
                smaller_big_edges += 1
            elif diff_edges > 0:
                smaller_meta_edges += 1
            else:
                equal_edges += 1

            if edges_meta[i] != 0:
                avg_edges_meta += edges_meta[i]
                c1 += 1

            avg_edges_big += edges_big[i]
            c2 += 1

            traces[i].append(edges_big[i])
            traces[i].append(edges_meta[i])
            traces[i].append(diff_edges)
        except:
            traces[i].append(edges_big[i])
            traces[i].append(edges_meta[i])
            traces[i].append(None)
        i += 1

    avg_edges_meta /= c1
    avg_edges_big /= c2

    return smaller_big_edges, smaller_meta_edges, equal_edges, avg_edges_big, avg_edges_meta

def time(big_times_list, meta_times_list):
    tot_time_big = 0
    tot_time_meta = 0
    i = 0

    while i < len(meta_times_list):
        tot_time_big += big_times_list[i]
        tot_time_meta += meta_times_list[i]
        traces[i].append(big_times_list[i])
        traces[i].append(meta_times_list[i])
        traces[i].append(big_times_list[i] - meta_times_list[i])
        i += 1

    return tot_time_big, tot_time_meta

if __name__ == '__main__':

    log = "testBank2000NoRandomNoise"
    parameters = "a0.8_b0.75_g1_T500_iter50_k2"
    iter = 50

    iteration_data = pd.read_excel(log + "_recap\\iterations\\IterationData_" + parameters + "_" + log + ".xlsx")
    iterations(iteration_data, iter, parameters, log)
    iterations_data = pd.read_excel(log + "_recap\\iterations\\" + log + "_min_iterations_" + parameters + ".xlsx")
    meta_iterations = iterations_data["min iterations"].tolist()
    seed_iterations = iterations_data["seed"].tolist()

    avg_iterations = avg_iter(seed_iterations, meta_iterations)

    recap = []
    traces = []

    for seed in range(1, 4):

        multi_seeds = pd.read_excel(log + "_recap\\multi_seeds_" + parameters + "_" + log + ".xlsx", sheet_name="res_" + str(seed))

        big_times = pd.read_excel(log + "_recap\\big_times_" + log + ".xlsx", sheet_name="big_times")

        recap = []
        traces = []

        gen_meta = multi_seeds["gen meta"].tolist()
        gen_big = multi_seeds["gen big"].tolist()

        smaller_big_gen, smaller_meta_gen, equal_gen, mse = gen(gen_big, gen_meta)

        move_meta = multi_seeds["meta move"].tolist()
        move_big = multi_seeds["big move"].tolist()

        smaller_big_move, smaller_meta_move, equal_move, meta_fail_move = move(move_big, move_meta)

        move_align_big = multi_seeds["diff ig align big"].tolist()
        move_align_meta = multi_seeds["diff ig align meta"].tolist()

        smaller_big_move_align, smaller_meta_move_align, equal_move_align, meta_fail_move_ = move(move_align_big, move_align_meta)

        edges_meta = multi_seeds["meta edges"].tolist()
        edges_big = multi_seeds["big edges"].tolist()

        smaller_big_edges, smaller_meta_edges, equal_edges, avg_edges_big, avg_edges_meta = edges(edges_big, edges_meta)

        big_times_list = big_times["time"].tolist()
        meta_times_list = multi_seeds["time meta"].tolist()

        tot_time_big, tot_time_meta = time(big_times_list, meta_times_list)

        traces_df = pd.DataFrame(traces, columns=["trace id", "gen big", "gen meta", "diff gen",
                                                  "struct move big", "struct move meta", "diff struc move",
                                                  "align move big", "align move meta", "diff align move",
                                                  "edges big", "edges meta", "diff edges",
                                                  "time big", "time meta", "diff time"])
        with pd.ExcelWriter(log + "_recap\\" + log + '_' + str(seed) + ".xlsx", mode='a',
                            if_sheet_exists="replace") as writer:
            traces_df.to_excel(writer, sheet_name=parameters, index=False)

        recap.append(
            [parameters, smaller_big_gen, smaller_meta_gen, equal_gen, mse, smaller_big_move, smaller_meta_move,
             equal_move, smaller_big_move_align, smaller_meta_move_align, equal_move_align,
             meta_fail_move, avg_edges_big, avg_edges_meta, tot_time_big, tot_time_meta, avg_iterations[seed - 1]])

        recap_df = pd.DataFrame(recap,
                                columns=["parameters", "gen smaller big", "gen smaller meta", "gen equal", "MSE gen",
                                         "move smaller big", "move smaller meta", "move equal",
                                         "align move smaller big", "align move smaller meta", "align move equal",
                                         "meta failures",
                                         "avg edges big", "avg edges meta", "tot time big", "tot time meta",
                                         "avg iterations"])
        with pd.ExcelWriter(log + "_recap\\" + log + '_' + str(seed) + ".xlsx", engine='openpyxl', mode='a',
                            if_sheet_exists='overlay') as writer:
            recap_df.to_excel(writer, sheet_name='recap', startrow=writer.sheets["recap"].max_row, index=False,
                              header=False)







