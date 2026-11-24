from colors_ansi import cores
nota1 = float(input('Digite a primeira nota do aluno (1/4): '))
nota2 = float(input('Digite a segunda nota do aluno (2/4): '))
nota3 = float(input('Digite a terceira nota do aluno(3/4): '))
nota4 = float(input('Digite a quarta nota do aluno(4/4): '))
maxima = float(input('Digite a nota máxima das provas: '))
medial = (nota1 + nota2 + nota3 + nota4) / 4
mediap = (maxima / 2) + 1
recup = (maxima / 2) - 1
reprov = (maxima / 2) - 1.5
if medial >= mediap:
    print('A média do aluno é de {:.1f} e ele está:'.format(medial))
    print('{}APROVADO{}'.format(cores['verde'], cores['limpa']))
    print('Acima da média de {:.1f}'.format(mediap))
elif recup <= medial > reprov:
    print('A média do aluno é de {:.1f} e ele está:'.format(medial))
    print('{}DE RECUPERAÇÃO{}'.format(cores['amarelo'], cores['limpa']))
    print('Abaixo da média de {:.1f}, porém acima da média de reprovação que é {:.1f}'.format(mediap, reprov))
else:
    print('A média do alundo é de {:.1f} e ele está:'.format(medial))
    print('{}REPROVADO{}'.format(cores['vermelho'], cores['limpa']))
    print('Dentro da média de reprovação que é de {:.1f} para baixo'.format(reprov))
print(' ')
print('{}Agradeçemos a preferencia aos nossos serviços!{}'.format(cores['azul'], cores['limpa']))
