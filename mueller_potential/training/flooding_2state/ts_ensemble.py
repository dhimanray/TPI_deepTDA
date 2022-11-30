import numpy as np

stateA_cut = -3.5
stateB_cut = 2.0

for i in range(1,31):
    f1 = open('ts_data/data_%d'%i,'w')
    l = np.loadtxt('run%d/COLVAR'%i)
    #l = l[::4]
    l_flipped = np.flip(l,axis=0)
    #exclude portions beyond the unfolded cut and folded cut
    for j in range(len(l_flipped)):
        #print(l_flipped[j,3])
        if l_flipped[j,3] < stateB_cut and l_flipped[j,3] > stateA_cut:
            for k in range(len(l_flipped[j])):
                print(l_flipped[j,k],end=' ',file=f1)
            print(file=f1)
            print(l_flipped[j,3])
        if l_flipped[j,3] <= stateA_cut:
            break




    f1.close()
    print('traj_%d Done'%i)
