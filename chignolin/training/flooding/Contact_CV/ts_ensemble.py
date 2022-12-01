import numpy as np

stateA_cut = -5
stateB_cut = 5

f2 = open('ts_data/all_data','w')
for i in range(1,21):
    f1 = open('ts_data/data_%d'%i,'w')
    l = np.loadtxt('run%d/COLVAR'%i)
    #l = l[::4]
    l_flipped = np.flip(l,axis=0)
    #exclude portions beyond the unfolded cut and folded cut
    for j in range(len(l_flipped)):
        #print(l_flipped[j,3])
        if l_flipped[j,5] < stateB_cut and l_flipped[j,5] > stateA_cut:
            for k in l_flipped[j,6:51]:
                print(k,end=' ',file=f1)
                print(k,end=' ',file=f2)
            print(file=f1)
            print(file=f2)
            #print(l_flipped[j,5])
        if l_flipped[j,5] <= stateA_cut:
            break




    f1.close()
    print('traj_%d Done'%i)
f2.close()
