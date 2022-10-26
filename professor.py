# Classe Professor
class Professor:

    # Atributos do Professor
    def __init__(self, nome, matricula, subarea, campus_atual, campus_removido, tempo_ifce, idade, nota_concurso):
        self.nome = nome
        self.matricula = matricula
        self.subarea = subarea
        self.campus_atual = campus_atual
        self.campus_removido = campus_removido
        self.tempo_ifce = tempo_ifce
        self.idade = idade
        self.nota_concurso = nota_concurso


    #  Função para verificar qual professor tem tempo maior de IFCE
    def __repr__(self):
        return repr((self.nome_professor, self.tempo_ifce))
    
    
    # Função para mostrar as variaveis do professor e não a possição que estar na memoria.
    def __str__(self):
        return f"{self.nome}"

    #  Função para cadastrar o professor com os inputs
    @staticmethod
    def cadastro():
        nome_professor = input('Digite o nome do professor: ')
        matricula_professor = int(input('Digite a matricula do professor: '))
        sub_area_professor = input('Digite a sub área do professor: ')
        campus_atual_professor = input('Digite o campus atual do professor: ')
        campus_removido_professor = input('Digite o campus de remoção do professor: ')
        tempo_ifce_professor = int(input('Digite o tempo de IFCE do professor: '))
        idade_professor = int(input('Digite a Idade do professor: '))
        nota_concurso_professor = float(input('Digite a nota do concurso do professor: '))

        return Professor(nome_professor, matricula_professor, sub_area_professor, campus_atual_professor, campus_removido_professor, tempo_ifce_professor, idade_professor, nota_concurso_professor)

