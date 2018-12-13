import random

def probabilidade_caras(n, p, quant_caras, seguidos):
    # Cria lista e peso conforme a probabilidade p
    lados = ['CARA', 'COROA']
    pesos = [p, 1-p]

    total_lancamentos = 0

    for i in range(0, n):
        numero_caras   = 0 
        caras_seguidos = 0

        lancamentos    = 0

        while(True):
            r = random.choices(lados, pesos)
            lancamentos += 1
            if r[0] == 'CARA':
                caras_seguidos += 1
                numero_caras   += 1
            else:
                caras_seguidos  = 0

            if(seguidos and caras_seguidos == quant_caras):
                break

            if((not seguidos) and numero_caras == quant_caras):
                break

        total_lancamentos += lancamentos

    # Retorna a média de lançamentos em n iterações
    return total_lancamentos/n


# Primeiras perguntass
p2sobre3_5 = probabilidade_caras(100, 2/3, 5, False)
print('O número médio de lançamentos até obter 5 caras foi ', p2sobre3_5, ' em ', 100, ' iterações')

p2sobre3_2seguidos = probabilidade_caras(100, 2/3, 2, True)
print('O número médio de lançamentos até obter 2 caras seguidos foi ', p2sobre3_2seguidos, ' em ', 100, ' iterações')

#separador
for x in range(0,50): print('#', end='')
print('')

# Variando o P
nivel_variacao = 10
for i in range(nivel_variacao, 0, -1):
    p = 1/i
    res          = probabilidade_caras(100, p, 5, False)
    res_seguidos = probabilidade_caras(100, p, 2, True)
    print('Resultado para: ', 'p = 1/', i)
    print('Numéro médio de lançamentos para 5 caras: ', res)
    print('Numéro médio de lançamentos para 2 caras seguidos: ', res_seguidos)

    #separador
    for x in range(0,50): print('#', end='')
    print('')