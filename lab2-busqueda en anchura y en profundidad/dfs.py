graph={
    'M':['I','E'],
    'I':['L','P'],
    'E':['Z','R'],
    'L':[],
    'P':[],
    'Z':['A','H'],
    'R':['W','N'],
    'A':['X','Y'],
    'H':['U','D'],
    'W':['Q','C'],
    'N':['B','G'],
    'X':[],
    'Y':['F','K'],
    'U':[],
    'D':['J'],
    'Q':[],
    'C':[],
    'B':[],
    'G':[],
    'F':[],
    'K':[],
    'J':[]
    
}



frontier=[]
reached=[]
f=open("dfs.txt","w")



def dfs(graph, raiz, nodo):
    k=1
    frontier.append(raiz)
    marca=0
    
    while frontier:
        print('Paso ',k,': ')
        print('Frontier: ',frontier)
        print('Reached: ',reached,'\n')
        f.write('Paso '+str(k)+'\n')
        f.write('Frontier: '+str(frontier)+'\n')
        f.write('Reached: '+str(reached)+'\n\n')
        s=frontier.pop(0)
        if marca==1:
            break
        
        
        if s==nodo:
            print('si esta')
            marca+=1
        else:
            reached.append(s)
            f.write('Reached: '+str(reached)+'\n')
            
        i=0
        for neighbour in graph[s]:
            frontier.insert(i,neighbour)
            i+=1
        k+=1
            
print('DFS-Nodo seleccionado: K')
print('Alumno: Jhon Ismael Flores Pacheco')
f.write('BFS-Nodo seleccionado: K\n')
f.write('Alumno: Jhon Ismael Flores Pacheco\n\n')
dfs(graph,'M','K')
f.close()

