# Importando as Classes e seus métodos.
from professor import Professor
from prioridade import ListaPrioridade

# Cadastrando um professor na lista
professor = Professor.cadastro()
professor2 = Professor.cadastro()

# Criando uma lista e atribuindo a lista de prioridade de professores.
lista = ListaPrioridade()

# Adicionando dois professores
lista.push(professor)
lista.push(professor2)

# Excluindo o professor que está na posição 0.
lista.pop()

# Exibindo a lista com os professores cadastrados.
print(lista)