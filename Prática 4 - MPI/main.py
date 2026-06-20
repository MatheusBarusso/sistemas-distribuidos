from mpi4py import MPI
import random
import time
import sys

modo = sys.argv[1] #le argumento serial ou paralelo
TOTAL_PONTOS = int(sys.argv[2])
SEED = 420 

if (modo == "paralelo"):
    comm = MPI.COMM_WORLD #representa processos
    rank = comm.Get_rank() #retorna id do processo
    size = comm.Get_size() #qnts processos
    random.seed(SEED + rank) #seed p maior aleatoriedade entre processos
    pontos_locais = TOTAL_PONTOS // size #qnts pontos p cada rank
    contador_local = 0

    comm.Barrier() #sincronizacao p comecarem juntos
    inicio = time.perf_counter() #inicia cronometro

    for i in range(pontos_locais):
        x = random.random()
        y = random.random()

        if (x*x + y*y <= 1):
            contador_local += 1

    comm.Barrier()
    #soma resultados locais em global, root = 0 faz rank 0 receber a contagem
    contador_global = comm.reduce(contador_local, op=MPI.SUM, root=0)

    fim = time.perf_counter() # finaliza cronometro
    tempo_gasto = fim - inicio # calcula tempo gasto

    if rank == 0:
        pi_calc = 4 * contador_global / TOTAL_PONTOS #se n ficar no if todos tentam acessar global e da erro
        print("Processos:", size)
        print("Pontos:", TOTAL_PONTOS)
        print("Dentro:", contador_global)
        print("Pi estimado:", pi_calc)
        print("Tempo:", tempo_gasto)


elif (modo == "serial"):
    contador = 0
    random.seed(SEED)

    inicio = time.perf_counter()
    for i in range(TOTAL_PONTOS):
        x = random.random()
        y = random.random()

        if (x*x + y*y <= 1):
            contador += 1
    fim = time.perf_counter()
    tempo_gasto = fim - inicio
    pi_calc = 4 * contador / TOTAL_PONTOS
    print("Pontos:", TOTAL_PONTOS)
    print("Dentro:", contador)
    print("Pi estimado:", pi_calc)
    print("Tempo:", tempo_gasto)

else:
    print("Modo selecionado inválido, utilize 'serial' ou 'paralelo'")

