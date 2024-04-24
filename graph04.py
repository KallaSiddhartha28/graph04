graph=[(1,2),(2,3),(3,4),(4,5),(3,5)]
vertexset=set()
adj_mat=[]
for edge in graph:
    vertexset.add(edge[0])
    vertexset.add(edge[1])
nv=len(vertexset)
print("no of vertices=",nv)
adj_list={i:[] for i in vertexset}
for item in adj_list.items():
    print(item[0],item[1])
for edge in graph:
    adj_list[edge[0]].append(edge[1])
    adj_list[edge[1]].append(edge[0])
print("adj list")
for item in adj_list.items():
    print(item[0],item[1])
    
    
