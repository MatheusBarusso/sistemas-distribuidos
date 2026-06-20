# Aplicação paralela por MPI

## Descrição do Problema

Implementação de aplicação que pode ser escolhida, utilizando paralelização via MPI.

O problema escolhido é baseado no **Método de Monte Carlo para $\pi$**. É um método para cálculo do valor de $\pi$ usando um círculo inscrito em um quadrado de lado 2r e valores gerados aleatoriamente:
- A área do quadrado $A_{sqr} = (2r)^2 = 4r^2$
- A área do círculo é $A_{cir} = \pi r^2$
- A razão entre a área do circulo e a área do quadrado é:
  $$\frac{A_{cir}}{A_{sqr}} = \frac{\pi r^2}{4r^2} = \frac{\pi}{4}$$
- Se um número muito grande de pontos aleatório $(x,y)$ for gerado dentro desse quadrado e testarmos quantos caem dentro do círculo por meio da equação da circuferência $x^2 + y^2 \leq r^2$ teremos:
  $$\frac{\text{Pontos dentro do círculo}}{\text{Pontos totais}} = \frac{\pi}{4}$$
- E portanto:
  $$\pi \approx 4 \times \frac{\text{Pontos dentro do círculo}}{\text{Pontos totais}}$$


## Requisitos

- Deve ter implementação serial e paralela para comparação de desempenho.
- Paralelização precisa ser relevante (ou seja, não basta abrir trabalhos paralelos que não contribuam ou paralelizar um problema que não tenha sentido).
- Não pode utilizar solução usada em sala (Contar números primos e Somar Vetores) e nem algoritmo de teste de senha por dicionário.


## Execução

Na execução do programa 2 flags devem ser inseridas, a primeira relacionada ao tipo de execução (serial ou paralela) e a segunda relacionada ao número total de pontos do Método de Monte Carlo.

### 1 - Execução Serial

Em um terminal, execute:

```bash
python3 main.py serial NUMERO_PONTOS
```
Exemplo Serial para 100.000.000 pontos:

```bash
python3 main.py serial 100000000
```

### 2 - Execução Paralela

Em um terminal, execute:

```bash
mpirun -np NUMERO_PARALELIZAÇÃO python3 main.py paralelo NUMERO_PONTOS
```

Exemplo Paralelo separado em 8 processos para 100.000.000 pontos:

```bash
mpirun -np 8 python3 main.py paralelo 100000000
```

### 2.1 - Execução Paralela utilizando threads lógicas

O MPI Python utiliza por padrão o número de núcleos físicos do processador e pode acusar erro quando a flag de processos é maior que o número de cores. Para "contornar" isso por meio threads lógicos em um terminal, execute:

```bash
mpirun --use-hwthread-cpus -np NUMERO_PARALELIZAÇÃO python3 main.py paralelo NUMERO_PONTOS
```

Exemplo Paralelo separado em 16 processos para 100.000.000 pontos:

```bash
mpirun --use-hwthread-cpus -np 16 python3 main.py paralelo 100000000
```
