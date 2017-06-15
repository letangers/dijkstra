#构造图
def make_graph():
    graph={}
    
    f=open('data.txt')
    a=f.read().split('\n')
    f.close()

    #处理文件中的数据
    for b in a:
        temp={}

        #列表a的末尾可能有  “”
        if b == '':
            continue

        c=b.split()

        #在win下读取文件可能会出现这种情况
        if '\xef\xbb\xbf' in c[0]:
            c[0]=c[0].replace('\xef\xbb\xbf','')

        #将c[0]的邻接点的信息存储在temp中    
        for i in range(1,len(c),2):
            temp[c[i]]=c[i+1]
            
        graph[c[0]]=temp

        
    return graph

def dijkstra(begin,graph):
    rea={}
    
    #初始化距离数组m
    m=[]
    temp={}
    for i in graph:
        if i==begin:  
           continue
        temp[i]=float('inf') 
    for i in range(len(graph)-1):
        m.append(temp)


    tmp=begin
    for i in range(len(m)):

        for j in graph[tmp]:
            if j == begin:
                continue
            
            if i==0:
                m[i][j]=graph[tmp][j]
                m[i][j]=eval(m[i][j])
            else:
                m[i][j]=min(m[i-1][j],rea[tmp]+eval(graph[tmp][j]))

        mmin=float('inf')
        for mm in m[i]:
            if m[i][mm]>0 and m[i][mm]<=mmin:
                mmin=m[i][mm]
                tmp=mm
        rea[tmp]=m[i][tmp]
        m[i][tmp]=-1
    return rea

if __name__ == "__main__":
    graph=make_graph()
    result=dijkstra('a',graph)
    print (result)
