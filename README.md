# Iterated Local Search metaheuristic

Questo repository contiene l'approccio implementato di
"Iterated Local Search metaheuristic".

Gli autori: Domenico Potena, Martina Pioli, Ornella Pisacane

## Istruzioni per l'utilizzo

Il progetto è formato da diversi file:
- main.py : funzione principale della metaeuristica e main
- configuration.py : file di configurazione, dove impostare i parametri desiderati per l'esecuzione
- instantgraph.py : funzioni che operano sugli instancegraph (finCausalRelationship, findDependency, ExtractInstanceGraph, ecc)
- admissible.py : funzioni utilizzate per valutare l'ammissibilità di un instance graph (soundness, fitting)
- generalization_function.py : funzioni utilizzate per calcolare la funzione obiettivo e valutare l'istance graph da prendere ad ogni iterazione
- move_function.py : funzioni richiamate nella fase di local search per effettuare dei cambiamenti nell'istance graph
- test_function.py : funzioni di utility per scrivere un instance graph su file oppure importarlo
- big_v1.py : implementazione dell'algoritmo BIG (https://rdcu.be/cU3zH) pubblicato attualmente
- big_v2.py : implementazione dell'algoritmo BIG migliorato

Per rendere lo script funzionante è necessario inserire nella stessa cartella dei file sopra elencati le seguenti cartelle:
- log : al suo interno deve essere inserita una rete di petri in formato ".pnml" ed un log ad essa associato in formato ".xes"
- output : verranno inseriti i dati stampati a fine esecuzione
- ig : dove vengono salvati gli ig prodotti dall'esecuzione

Lo script nel reporitory è quello utilizzato nella fase di sperimetazione. L'esecuzione viene ripetuta tre volte per ogni traccia analizzata, ogni volta con un seed diverso.

La cartella experimentation è dedicata alla sperimentazione. Al suo interno è necessario creare una cartella col nome del log da analizzare e in questa cartella bisogna:
- inserire i file multiseeds che si vogliono analizzare,
- creare la sottocartella iterations, in cui inserire i corrispettivi (stessi set di parametri dei file multiseeds) file IterationData,
- creare tre file con il nome del log seguito da un underscore e dai numeri da 1 a 3, quindi un file per ogni seed (ad esempio andreaHelpdesk_1, andreaHelpdesk_2, andreaHelpdesk_3). Creare un foglio chiamato recap in ciascuno di questi tre file.
Per generare i dati della sperimentazione basterà lanciare il file test_multiseeds.py, avendo l'accortezza di modificare opportunamente le variabili log, parameters e iter.
