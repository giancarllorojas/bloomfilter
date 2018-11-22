import hashlib
import uuid
import math

def add_word(word):
    global salts_array, bloom_array
    # Gera as hashes
    hashes = [int(hashlib.sha256((str(salt) + str(word)).encode()).hexdigest(), 16) % m for salt in salts_array]

    for i in hashes:
        bloom_array[i] = 1

def word_is_present(word):
    global salts_array, bloom_array
    # Gera as hashes
    hashes = [int(hashlib.sha256((str(salt) + str(word)).encode()).hexdigest(), 16) % m for salt in salts_array]
    is_false = False

    for i in hashes:
        if(bloom_array[i] == 0):
            is_false = True
            break

    return not is_false

# n = Numero de palavras que vão ser inseridas
# m = Tamanho do array de bits
# k = Quantidade de funções hashes
# Calcula a probabilidade de falso positivo dado os parametros do BloomFilter
def probability_false_positive(n, m, k):
    return math.pow(1 - math.pow((1 - (1/m)), k*n), k)

# n = Numero de palavras que vão ser inseridas
# p = Numero de 0 a 1 que indica a desejada probabilidade de falsos positivos
# Retorna o tamanho ótimo para a desejada probaiblidade de falsos positivos p
def optimal_bit_array_size(n,p):
    return math.ceil(-(n*math.log(p))/math.pow((math.log(2)),2))

# n = Numero de palavras que vão ser inseridas
# m = Tamanho do array de bits
# Retorna um número ótimo para k
def optimal_number_of_hashes(m,n):
    return math.ceil((m/n)*math.log(2))

n = 1000
m = optimal_bit_array_size(n,0.0000000001) # Tamanho do array de bits
k = 1  # Quantidade de Funções Hashes

print(m,k)

bloom_array = [0 for i in range(0,m)]

# Gera k salt's aleatorias para compor as k hashes
salts_array = [uuid.uuid4().hex for i in range(0,k)]

# Lê o arquivo com as palavras para o teste e adiciona ao BloomFilter
words = open('100kwords.txt', 'r').readlines()
for w in words:
    add_word(w)

#print(bloom_array)


# Lê o arquivo com as palavras para teste, contendo 50% de palavras contidas no dataset de palavras
# adicionadas ao BloomFilter e testa para ver se elas estão presentes
words_test = open('words_test.txt', 'r').readlines()
words_present = 0
words_not     = 0
for w in words_test:
    is_present = word_is_present(w)
    if(not is_present):
        print('false')
    words_present += int(is_present)
    words_not     += int(not is_present)

print(words_present, words_not)