#variável que guarda a tabela 
tabela = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#função que imprime a tabela 
def imprime_tabela(tb):
    '''
    obs: acima, tb significa que a variável trazida pra dentro da função vai 
    ser chamada de tb. 
    '''    
    #a cada 3 linhas, imprimir uma sequência de ---- para dividir a tabela 
    for i in range(len(tabela)):
        if i%3==0 and i!=0: 
            print("- - - - - - - - - - - - ")
    
        for j in range(len(tb[0])):
            '''
            agora pegamos o tamanho do primeiro elemento vetor do vetor tabela 
            e nele passamos o nosso contador j 
            '''
            if j%3==0 and j!=0:
                print(" | ", end="")
            
            '''
            agora, imprimimos o ultimo elemento caso o contador seja igual a 8
            e logo em seguida, os outros elementos, atraves do acesso da  
            '''
            if j == 8 : 
                print(tb[i][j])
            else: 
                print(str(tb[i][j]) + " ", end="")

#função que encontra o elemento vazio na tabela, represendato como 0
def encontra_vazio(tb):
    '''
    rodar um contador que vai passar por toda a matriz
    '''
    for i in range(len(tb)):
        for j in range(len(tb[0])):
            '''
            caso o valor do elemento seja 0, a função irá retornar a posição 
            do mesmo. 
            '''
            if tb[i][j] == 0:
                return(i, j)

#função que valida a tabela
#variaveis inseridas sao tabela, numero a ser checado e posição
def valida_tabela(tb, num, pos):
    '''
    primeiro, iremos checar as linhas, o algoritmo irá passar e confirmar
    se existe algum número igual na linha. 
    '''
    for i in range(len(tb[0])):
        if tb[pos[0]][i] == num and pos[1] != i:
            return False 

    '''
    agora, iremos checar as colunas, da mesma maneira.
    '''
    for i in range(len(tb)): 
        if tb[i][pos[1]] == num and pos [0] != 1: 
            return False 

    '''
    por último, checaremos as 3 caixas 3x3 na tabela do sudoku
    '''
    caixa_x = pos[1]//3 
    caixa_y = pos[0]//3

    for i in range(caixa_y*3, caixa_y*3+3):
        for j in range(caixa_x*3, caixa_x*3+3):
            if tb[i][j] == num and (i,j) != pos:
                return False 
    
    #se nenhum destas checagens derem 0, retorna-se True 
    return True 

#função que resolve o sudoku
def resolve(tb):

    '''
    primeiro, chamaremos a função que encontra o número vazio
    '''
    encontra = encontra_vazio(tb)
    if not encontra: 
        '''caso não encontre elemento vazio, significa 
        que a tabela está resolvida'''
        return True
    else:
        '''
        caso encontre o vazio, as variáveis linha e coluna receberão os
        valores retornados da função encontra_vazio 
        '''
        linha, coluna = encontra
        
    for i in range(1,10):
        '''
        o contador i irá passar de 1 a 9 e passará na função de 
        validação de tabela
        '''
        if valida_tabela(tb, i, (linha,coluna)):
            '''
            caso o retorno seja True, o valor do elemento nulo passa a ser 
            o mesmo valor de i enquanto sendo contado 
            '''
            tb[linha][coluna] = i 
            
            '''
            e então utilizamos a recursividade da função resolve para verificar
            a validade da tabela
            '''
            if resolve(tb):
                '''
                caso seja válido, retorna True
                '''
                return True
            '''
            caso não seja, o elemento da matriz se torna nulo (0) novamente
            '''
            tb[linha][coluna] = 0 
    
    return False       


imprime_tabela(tabela) 
resolve(tabela)
print("_______________________")
imprime_tabela(tabela)

