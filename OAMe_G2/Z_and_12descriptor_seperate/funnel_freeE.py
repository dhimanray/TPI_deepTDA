import numpy as np

fesfile = 'fes_Z'

zmin_bound = 4.0
zmax_bound = 12.0

zmin_unbound = 14.0
zmax_unbound = 16.0

funnel_radius = 2.0

def binding_free_energy(fesfile,zmin_bound,zmax_bound,zmin_unbound,zmax_unbound,funnel_radius):
    T = 300.0
    kT = 0.008273338*T #kJ/mol
    C_0 = 1.0/1660.0 #in Angstrom^3
    l = np.loadtxt(fesfile)
    z = 10*l[:,0] #nm to Angstrom conversion
    fes_z = l[:,1]
    
    bound_z = []
    bound_fes = []
    for i in range(len(z)):
        if z[i] >= zmin_bound and z[i] <= zmax_bound:
            bound_z.append(z[i])
            bound_fes.append(fes_z[i])
    bound_z = np.array(bound_z)
    bound_fes = np.array(bound_fes)

    unbound_fes = []
    for i in range(len(z)):
        if z[i] >= zmin_unbound and z[i] <= zmax_unbound:
            unbound_fes.append(fes_z[i])
    unbound_fes = np.array(unbound_fes)
    wz_ref = np.mean(unbound_fes)

    integrant = np.exp(-(1/kT)*(bound_fes - wz_ref))
    Kb = np.pi * funnel_radius**2 * np.trapz(integrant,bound_z)
    delta_G = -kT*np.log(C_0*Kb)

    return delta_G

G_kJ = binding_free_energy(fesfile,zmin_bound,zmax_bound,zmin_unbound,zmax_unbound,funnel_radius)
G_kcal = G_kJ/4.1855

print('Binding free energy: ',G_kJ,' kJ/mol ',G_kcal,' kcal/mol ')
    

