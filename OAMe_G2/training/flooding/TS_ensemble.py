import numpy as np

unbound_cut = 1.3
bound_cut = 0.8

for i in range(1,14):
    f1 = open('ts_data/data_%d'%i,'w')
    l = np.loadtxt('run%d/descriptors'%i)
    #exclude portions beyond the bound cut and unbound cut
    for j in range(len(l)):
        if l[j,13] <= unbound_cut and l[j,13] >= bound_cut:
            for k in range(14):
                print(l[j,k],end=' ',file=f1)
            print('',file=f1) 

    f1.close()
    print('traj_%d Done'%i)
