#Variáveis Built-Ins 
#tipos Built-Ins- Priemeiro tipo é o tipo lista, uma lista normal
Lista_convidados = ["joao", "Gustavo", "Paulo", "lucca", "Breno"] #abriu e fechou couchetes= delarei lista vazia
#a lista é uma variavel mutavel, consegue adicionar e remover elemetos dessa listas

print(Lista_convidados)

Lista_convidados.append("igor")
#para adicionar elemetos

print(Lista_convidados)

Lista_convidados.remove("joao")
#para remover um elemento 

print(Lista_convidados)

#conseguimos acessar os valores individualmente da lista, depois que removi o joao, quero pegar o primeiro elemento, 
# antes de remover o joão, ele era o primeiro elemento, quando remover o joão, o gustavo sera o segundo elemento

print(Lista_convidados[0])
#para pegar esse primeiro elemento, vai fazer o print, passa o cochete e uma posição
#no python o 1º elemento é [0], o 2º elemento é [1], o 3º elemento é [2]

print(Lista_convidados[-1])
#conseguimos pegar o ultimo elemento de uma forma mais simples, sem precisar saber quantos elementos 
#a lista tem, no caso usa a posição [-1] que ai ele vai do final da lista, decendo e pegar o elemento da posição 

Lista_convidados.append(50)
#uma caracteristca importante é que carregamos nossa lista somente com o tipo primitivo string, 
# mas podemos adicionar outros valores na lista, não recomendo muito pois o mix de valores pode acabar prejudicando se formos 
#tentar aplicar uma logica nessa lista. podemos adiconar varios tipos de valores diferentes em uma lista no python, ele é dinamico. 

print(Lista_convidados)

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
# O python tem tipos mutaveis e imutaveis, e um outro tipo que a tuple, é uma especie de lista não mutavel,
#  apartir de criado, não concegue adicionar ou remover elementos nela, algumas operações pode fazer nela,como somar 
# duas tuples, onde ele pega os elementos da 1º tuple, mais os elementos da outra, criar uma 3º tupla e retornar para mim
###para declarar tupla é parenteses ()

print(tuple1)

Tuple3= tuple1 + tuple2

print(Tuple3)
#como as tuples são imutaveis, o acesso a elas é mais rapido, porque ele sabe que não precisa se preocupa com um novo elemento,
#  a vantagem dela com a lista é que se formos adiconar muitos elementos posterior a craiação do valor/variavél porque é interessante 
# usar a lista pois a tuple a gente não consegue adicionar valores, é interessante usar a lista, ja que a tupla não aciona valores, mas 
# se tiver muita leitura, as vezes compensa criar uma tuple, se for o caso até recriar a tuple em um dado momento

#ultimo tipo é o tipo de sonario, um mapeamento de chave para valor 
#chave -> valor

dados_pessoais= {"nome": "marta", "cidade": "gabriel monteiro"}
#para declarar dicionario, abre e feche {} cochete, 
#adiciona a chave nome e a cidade 

print(dados_pessoais)

dados_pessoais["veiculo"] = "gol"
#o dicionario é mutavel e consegue fazer operações nele, dai ele aciona a nova chave valor ao print

print(dados_pessoais)

del dados_pessoais ["cidade"]
#para remover é um pouco diferente não tem bem uma função para remover, precisa usar a palvara reservada do python que é
#  "del"

print(dados_pessoais)
#a lista voce consegue chamar a função  REMOVE, para remover um elemento, passa o elemento a se remover
# -No dicionario de python o DEL deleta o conteudo de uma variavel
