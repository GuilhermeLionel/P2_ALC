#SUDOKU

def imprimir_grade(grade):
    cabecalho = "   "
    for j in range (9):
        cabecalho = cabecalho + f" C{j+1}"
    print(cabecalho)

    for i in range (9):
        texto_linha = f"L{i+1} "
        for j in range (9):
            valor = grade[i][j]
            texto_linha = texto_linha + f" {valor} "
        print (texto_linha)

def montar_grade_9x9(blocos):
    grade = []
    for br in range (3):
        for r in range (3):
            linha = []
            for bc in range (3):
                bloco = blocos[br*3 + bc]
                linha.extend(bloco[r])
            grade.append(linha)
    return grade


def main ():
    f1 = [
        [5,3,4],
        [6,7,2],
        [1,9,8]
    ]
    f2 = [
        [6,7,8],
        [1,9,5],
        [3,4,2]
    ]
    f3 = [
        [9,1,2],
        [3,4,8],
        [5,6,7]
    ]
    f4 = [
        [8,5,9],
        [4,2,6],
        [7,1,3]
    ]
    f5 = [
        [7,6,1],
        [8,5,3],
        [9,2,4]
    ]
    f6 = [
        [4,2,3],
        [7,9,1],
        [8,5,6]
    ]
    f7 = [
        [9,6,1],
        [2,8,7],
        [3,4,5]
    ]
    f8 = [
        [5,3,7],
        [4,1,9],
        [2,8,6]
    ]
    f9 = [
        [2,8,4],
        [6,3,5],
        [1,7,9]
    ]

    grade = montar_grade_9x9([f1, f2, f3, f4, f5, f6, f7, f8, f9])
    imprimir_grade(grade)

main()