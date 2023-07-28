def parameters():
    # total trace to analyze
    # tot = 20
    tot = "max"

    # gamma = 0 e beta = 0.75 -> best values by experiments in gap gen and gap move terms
    beta = 0.25 # 0.25 0.5 0.75
    gamma = 0 # 0 o 1
    T = 500
    iter = 50 # lascia 50, però tieni a mente che dipende dagli altri parametri. Se k=10 oscilla molto.
    # Vedere quando converge e poi capire se sia il caso di modificarlo
    # Lanciare su una decina di tracce esperimenti con iter = 100 variando i parametri e poi vedendo a che k si stabilizza
    a = 0.8 # maggiore alpha più è probabile l'accettazione
    k = 2 # aumentare, provando 2-(4)-6-(8)-10 (4 e 8 per ora no)
    return tot, T, iter, a, k, beta, gamma


def search_path():
    # npath = "andreaHelpdesk_petriNet.pnml"
    # lpath = "andreaHelpdesk.xes"

    # npath = "BPI2017Denied_petriNet.pnml"
    # lpath = "BPI2017Denied.xes"

    npath = "testBank2000NoRandomNoise_petriNet.pnml"
    lpath = "testBank2000NoRandomNoise.xes"

    # npath = "BPI2012_SE_08.pnml"
    # lpath = "BPI.xes"

    return npath, lpath


def format_final_data(d):
    if type(d) is tuple:
        gen = d.pop()
        res = d.pop()
        if res:
            res = "t_out"
        else:
            res = "no_pt"
    else:
        gen = d
        res = '-'

    return gen, res
