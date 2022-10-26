# Classe da Lista de Prioridade do professor por tempo de IFCE.
class ListaPrioridade:

    #  Método para criar uma lista de prioridades.
    def __init__(self):
        self.lista_prioridade = []
    

    #  Método para Adicionar um Professor na lista.
    def push(self, professor):
        self.lista_prioridade.append(professor)
    

    #  Método para verificar se a lista está vazia ou não.
    def empty(self):
        if self.lista_prioridade == []:

            return True
        else:
            return False
    
    
    #  Método para remover sempre o primeiro na prioridade da lista de professores.
    def pop(self):
        self.lista_prioridade = sorted(self.lista_prioridade, key=lambda professor: professor.tempo_ifce, reverse=True)

        self.lista_prioridade.pop(0)

    #  Método para organizar os professores na lista de professores por tempo de IFCE
    def __str__(self):
        self.lista_prioridade = sorted(self.lista_prioridade, key=lambda professor: professor.tempo_ifce, reverse=True)

        mostrar_lista_prioridade = ""

        for professor in self.lista_prioridade:
            mostrar_lista_prioridade += str(professor) + "\n"

        return mostrar_lista_prioridade
        