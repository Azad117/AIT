import numpy as np
from numpy import inf

d = np.array([[0,10,12,11,14]
          ,[10,0,13,15,8]
          ,[12,13,0,9,14]
          ,[11,15,9,0,16]
          ,[14,8,14,16,0]])

iteration = 100
n_ants = 5
n_citys = 5

m = n_ants
n = n_citys
e = .5         
alpha = 1     
beta = 2       

visibility = 1/d
visibility[visibility == inf ] = 0

pheromne = .1*np.ones((m,n))

rute = np.ones((m,n+1))

for ite in range(iteration):
    
    rute[:,0] = 1         
    
    for i in range(m):
        
        temp_visibility = np.array(visibility)         
        
        for j in range(n-1):
            
            combine_feature = np.zeros(5)    
            cum_prob = np.zeros(5)            
            
            cur_loc = int(rute[i,j]-1)        
            
            temp_visibility[:,cur_loc] = 0     
            
            p_feature = np.power(pheromne[cur_loc,:],beta)         
            v_feature = np.power(temp_visibility[cur_loc,:],alpha)  
            
            p_feature = p_feature[:,np.newaxis]                     
            v_feature = v_feature[:,np.newaxis]                     
            
            combine_feature = np.multiply(p_feature,v_feature)     
                        
            total = np.sum(combine_feature)                        
            
            probs = combine_feature/total   
            
            cum_prob = np.cumsum(probs)    
            #print(cum_prob)
            r = np.random.random_sample()   
            #print(r)
            city = np.nonzero(cum_prob>r)[0][0]+1       
            #print(city)
            
            rute[i,j+1] = city              
           
        left = list(set([i for i in range(1,n+1)])-set(rute[i,:-2]))[0]    
        
        rute[i,-2] = left                   
       
    rute_opt = np.array(rute)               
    
    dist_cost = np.zeros((m,1))             
    for i in range(m):
        
        s = 0
        for j in range(n-1):
            
            s = s + d[int(rute_opt[i,j])-1,int(rute_opt[i,j+1])-1]   
        
        dist_cost[i]=s                     
       
    dist_min_loc = np.argmin(dist_cost)             
    dist_min_cost = dist_cost[dist_min_loc]        
    
    best_route = rute[dist_min_loc,:]               
    pheromne = (1-e)*pheromne                       
    
    for i in range(m):
        for j in range(n-1):
            dt = 1/dist_cost[i]
            pheromne[int(rute_opt[i,j])-1,int(rute_opt[i,j+1])-1] = pheromne[int(rute_opt[i,j])-1,int(rute_opt[i,j+1])-1] + dt   

print('route of all the ants at the end :')
print(rute_opt)
print()
print('best path :',best_route)
print('cost of the best path',int(dist_min_cost[0]) + d[int(best_route[-2])-1,0])
