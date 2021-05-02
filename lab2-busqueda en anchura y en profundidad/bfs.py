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


reached=[]
frontier=[]#Es una cola fifo
f=open("bfs.txt","w")

def bfs(graph, reached, nodo , raiz):
    reached.append(raiz)
    frontier.append(raiz)
    i=1
    marca=0
    
    while frontier:
        print('Paso ',i,': ')
        print('Frontier: ',frontier)
        print('Reached: ',reached,'\n')
        f.write('Paso '+str(i)+'\n')
        f.write('Frontier: '+str(frontier)+'\n')
        f.write('Reached: '+str(reached)+'\n\n')
        s=frontier.pop(0)
        for neighbour in graph[s]:
            if neighbour==nodo:
                print('El nodo buscado sí se encuentra')
                marca=1
                break
            if neighbour not in reached:
                reached.append(neighbour)
                frontier.append(neighbour)
                
        i+=1
        if marca==1:
            break


print('BFS-Nodo seleccionado: K')
print('Alumno: Jhon Ismael Flores Pacheco')
f.write('BFS-Nodo seleccionado: K\n')
f.write('Alumno: Jhon Ismael Flores Pacheco\n\n')

bfs(graph,reached,'K','M')

f.close()
    
    
    
