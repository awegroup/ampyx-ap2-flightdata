import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append(r"/usr/local/casadi-py27-v3.3.0/")
sys.path.append('/Users/elenama/Box Sync/Code/Kitemodel/Dragonfly/Validation')
sys.path.append('/Users/elenama/Box Sync/Code/Kitemodel/Dragonfly/Pumping')
import importlib
import modelstruct
import plots
import sys
import casadi as ca


# --- Load data
# plt.close('all')

 # mat   = scipy.io.loadmat('/Users/elenama/Box Sync/Write/AWEmodel_paper/scripts/validationDataFC114/validationDataFC114_1_v2_pc.mat') #1power cycles
def createinit(mat,d,N,nk):
    # get winch data
    winch   = scipy.io.loadmat('logData_FCC114_1.mat') #1power cycles
    tetherTension = winch['logData_FCC114_1']['WinchData'][0,0]['packetData'][0,0]['tether_tension'][0,0][35552:38019]
    tetherspeed = winch['logData_FCC114_1']['WinchData'][0,0]['packetData'][0,0]['tether_speed'][0,0][35552:38019]

    # get controls, 1xtime values
    controls    = mat['validationData']['controls'][0,0]
    aileron     = controls['aileron'][0][0][0]
    elevator    = controls['elevator'][0][0][0]
    rudder      = controls['rudder'][0][0][0]
    windx, windy, windz    = controls['wind'][0][0][0:3]
    times       = controls['times'][0][0][0]

    # get response 3xtime, 1xtime or 3x3xtime values
    response  = mat['validationData']['response'][0,0]
    p0,p1,p2  = response['p'][0][0][0:3]
    v0,v1,v2  = response['v'][0][0][0:3]
    R         = response['R'][0][0][0:9]
    w0,w1,w2  = response['w'][0][0][0:3]
    dltet     = response['tetherSpeed'][0][0][0]

    par = dict()
    par['times']     = times
    par['q']         = response['p'][0][0][0:3]
    par['ltet']      = np.array([np.linalg.norm(par['q'][:,k]) for k in range(par['q'].shape[1]) ] )
    par['dq']        = response['v'][0][0][0:3]
    par['R']         = response['R'][0][0][0:9]
    par['w']         = response['w'][0][0][0:3]
    par['coeff']     = np.array([controls['aileron'][0][0][0], controls['elevator'][0][0][0], controls['rudder'][0][0][0]] )
    par['dltet']     = np.concatenate(tetherspeed)#response['tetherSpeed'][0][0][0]
    par['AoA']       = response['angleOfAttack'][0][0][0]
    par['sslip']     = response['sideSlip'][0][0][0]
    par['ttens']     = np.concatenate(tetherTension)#response['tetherTension'][0][0][0]
    par['mechwork']  = par['ttens'] * par['dltet'] #response['mechanicalWork'][0][0][0][] # tether tension times speed
    par['RPY']       = response['rollPitchYaw'][0][0][0:3]
    par['v_body']    = response['velocityBody'][0][0][0:3]
    par['airspeed']  = response['airspeed'][0][0][0]
    par['wind']      = controls['wind'][0][0][0:3]
    par['v_app']     = response['v'][0][0] - controls['wind'][0][0]

    # --- determine descretisation steps
    dt = times[-1]/(len(times)-1) # delta t of measured data
    nvalues        = N
    discretisation = float(nvalues)/float(nk)
    if discretisation==int(discretisation):
        dn = int(discretisation)
    else: print 'NOTE: discretisation', discretisation, 'is not an integer. Choose another number of nodes nnodes'

    # --- get casadi struct in the correct format
    x = modelstruct.CasadiStruct(nk,d)
    init = x.V()
    pnum = x.P()

    for k in range(nk):
        init['Xd',k,:,'coeff'] = ca.DM([aileron[0:nvalues:dn][k], elevator[0:nvalues:dn][k], rudder[0:nvalues:dn][k] ])
        init['Xd',k,:,'q']     = ca.DM([ p0[0:nvalues:dn][k]  ,  p1[0:nvalues:dn][k]   , p2[0:nvalues:dn][k] ])
        qnorm                      = np.linalg.norm(init['Xd',k,0,'q'])
        init['Xd',k,:,'dq']    = ca.DM([ v0[0:nvalues:dn][k]  ,  v1[0:nvalues:dn][k]   , v2[0:nvalues:dn][k] ])
        init['Xd',k,:,'w']     = ca.DM([ w0[0:nvalues:dn][k] ,   w1[0:nvalues:dn][k]  , w2[0:nvalues:dn][k] ])
        init['XA',k,:]             = ca.DM( par['ttens'][0:nvalues:dn][k] / qnorm)
        init['Xd',k,:,'R',0:3]     = ca.DM([ R[0][0,0:nvalues:dn][k], R[1][0,0:nvalues:dn][k], R[2][0,0:nvalues:dn][k]]  )
        init['Xd',k,:,'R',3:6]     = ca.DM([ R[0][1,0:nvalues:dn][k], R[1][1,0:nvalues:dn][k], R[2][1,0:nvalues:dn][k]]  )
        init['Xd',k,:,'R',6:9]     = ca.DM([ R[0][2,0:nvalues:dn][k], R[1][2,0:nvalues:dn][k], R[2][2,0:nvalues:dn][k]]  )
        init['XA',k,:]             = ca.DM( par['ttens'][0:nvalues:dn][k] / qnorm)
        init['Xd',k,:,'dltet']     = ca.DM( par['dltet'] [0:nvalues:dn][k])
        init['Xd',k,:,'AoA']       = ca.DM( par['AoA'][0:nvalues:dn][k])
        init['Xd',k,:,'sslip']     = ca.DM( par['sslip'][0:nvalues:dn][k])
        init['Xd',k,:,'wind']       = ca.DM([ windx[0:nvalues:dn][k]  ,  windy[0:nvalues:dn][k]   , windz[0:nvalues:dn][k] ])

        init['Xd',k,:,'ltet']  = qnorm
        pnum['p',k,:,'windx']  =  ca.DM( windx[0:nvalues:dn][k])
        pnum['p',k,:,'windy']  =  ca.DM( windy[0:nvalues:dn][k])
    tf = float(N)/len(times)*times[-1]
    # tf = nk*mdata*0.02
    return init, nk, tf, pnum, par



# m = 41
# d = 3

def getC(d,m):
    """ getC(d,m) creates matrix for creating the data time grid as a linear combination of the collocation points
    inputs: d = Collocation points, m = data points in each finite interval """
    # Choose collocation points
    dt_data = 0.02
    dt_coll = m * dt_data

    tau_root = ca.collocation_points(d, 'radau')
    tau_root = ca.veccat(0, tau_root)
    data_grid = np.arange(0, (m+1) * dt_data , dt_data)
    data_grid_scaled = data_grid/data_grid[-1]

    # Coefficients for the data grid
    C = np.zeros((d+1,m+1))

    # For all collocation points
    tau = ca.SX.sym('tau')
    for j in range(d+1):
        # Construct Lagrange polynomials to get the polynomial basis at the collocation point
        L = 1
        for r in range(d+1):
            if r != j:
                L *= (tau-tau_root[r])/(tau_root[j]-tau_root[r])
        lfcn = ca.Function('lfcn', [tau],[L])
        # calculate coefficients for data grid
        for r in range(m+1):
            C[j][r] = lfcn(data_grid_scaled[r])

    return C




# mat   = scipy.io.loadmat('/Users/elenama/Box Sync/Write/AWEmodel_paper/scripts/validationDataFC114/validationDataFC114_1_v2_pc.mat') #1power cycles
mat   = scipy.io.loadmat('validationDataFC114_1_v2_pc.mat') #1power cycles


d=3
N = 30 ;nk = 10
init, nk, tf, wind, par = createinit(mat,d,N,nk)
# # plt.close('all')
# tgrid_x, tgrid_u, tgrid_xa = plots.xgrid(nk,d,tf)
# plt.ion()
# plots.plottraj(init,init)


#--- CHECK the wind shear rule on their data
controls    = mat['validationData']['controls'][0,0]; response  = mat['validationData']['response'][0,0]
windx       = controls['wind'][0][0][0]
windy       = controls['wind'][0][0][1]
windnorm    = [np.linalg.norm([windx[k], windy[k]]) for k in range(len(windx))]
p2  = -par['q'][2]
windspeed_shear = [7.5 * (h/5.5)**0.2 for h in p2]

# get retractrion phase
retractIdx = []
a =  par['dltet'] <= 0
for k in range(len(a)):
    if a[k] == True: retractIdx.append(k)

par['dltet']


# import plots
# plt.close('all')
# plots.draw(range(len(p2)),windnorm,range(len(p2)),windspeed_shear,'wind')

# sortedIdx = np.argsort(p2)
# plt.figure()
# plt.plot([windnorm[i] for i in sortedIdx],[p2[i] for i in sortedIdx] ,'o')
# plt.plot([windnorm[i] for i in retractIdx],[p2[i] for i in retractIdx] ,'or')
# plt.ylabel('height [m]'); plt.xlabel('wind speed [m/s]')


#
# mat   = scipy.io.loadmat('/Users/elenama/Box Sync/Write/AWEmodel_paper/scripts/validationDataFC114/validationDataFC114_1_v2_pc.mat') #1power cycles
# controls    = mat['validationData']['controls'][0,0]
# aileron     = controls['aileron'][0][0][0]
# elevator    = controls['elevator'][0][0][0]
# rudder      = controls['rudder'][0][0][0]
# # get response 3xtime, 1xtime or 3x3xtime values
# response  = mat['validationData']['response'][0,0]
# w0,w1,w2  = response['w'][0][0][0:3]
# R         = response['R'][0][0][0:9]
# times       = controls['times'][0][0][0]
# par = dict()
# par['AoA']       = response['angleOfAttack'][0][0][0]
# par['sslip']     = response['sideSlip'][0][0][0]
# par['v_body']    = response['velocityBody'][0][0][0:3]
# par['airspeed']  = response['airspeed'][0][0][0]
# par['v_app'] = response['v'][0][0] - controls['wind'][0][0]
#
# import pickle
# import aero_validation as aero
# from validation_par import initial_params
# from validation_par import initial_params
# params = initial_params()
#
# F_aero = []; M_aero = []; CDn = []; CLn = []
# F_aeroc = []; M_aeroc = []; CDnc = []; CLnc = []; aoac = []
# for k in range(len(w0)):
#     # Calculate AoA
#     v_app_body = ca.mul(R[:,:,k].T,par['v_app'][:,k])
#     AoA       = v_app_body[2]/v_app_body[0]
#     sslip     = v_app_body[1]/v_app_body[0]
#     omega = ca.DM([w0[k], w1[k], w2[k]])
#     coeff = ca.DM([aileron[k], elevator[k], rudder[k]])
#     CF, CM, CD, CL = aero.aero_coeffs_ampyx(par['AoA'][k], par['sslip'][k], par['v_app'][:,k], omega,  coeff , params)
#     CFc, CMc, CDc, CLc = aero.aero_coeffs_ampyx(AoA, sslip, par['v_app'][:,k], omega,  coeff , params)
#     F_aero.append(CF); M_aero.append(CM); CDn.append(CD); CLn.append(CL)
#     F_aeroc.append(CFc); M_aeroc.append(CMc); CDnc.append(CDc[0][0]); CLnc.append(CLc[0][0])
#     aoac.append(AoA)


# print with AoA offset
# with open('/Users/elenama/Box Sync/Code/Kitemodel/Dragonfly/Validation/Faero_data.dat','w') as f:
#     pickle.dump((F_aero, M_aero, CDn, CLn),f)
# with open('/Users/elenama/Box Sync/Code/Kitemodel/Dragonfly/Validation/Faero_datac.dat','w') as f:
#     pickle.dump((F_aeroc, M_aeroc, CDnc, CLnc),f)
# raw = scipy.io.loadmat('/Users/elenama/Box Sync/Write/AWEmodel_paper/scripts/validationDataFC114/validationDataFC114_1_v2_pc_raw.mat')
# AoAoffset = raw['data']['NavigationData'][0][0]['packetData'][0][0]['angleOfAttackOffset'][0][0]
# plt.ion()
# datapoints = len(times)
# plots.draw3(times, [F_aero[k][0] for k in range(datapoints)], times, [F_aeroc[k][0] for k in range(datapoints)], \
#             times, [F_aero[k][1] for k in range(datapoints)], times, [F_aeroc[k][1] for k in range(datapoints)], \
#             times, [F_aero[k][2] for k in range(datapoints)], times, [F_aeroc[k][2] for k in range(datapoints)], 'measured Aoa (blue) Vs calculated AoA in FAero')
# plt.savefig('F_aero.eps', format = 'eps',dpi = 300)
# plots.draw(times,CDn, times, CDnc, 'CD (measured Aoa (blue) Vs calculated AoA)')
# plt.savefig('CD.eps', format = 'eps',dpi = 300)
# plots.draw(times,CLn, times, CLnc, 'CD (measured Aoa (blue) Vs calculated AoA)')
# plt.savefig('CL.eps', format = 'eps',dpi = 300)
# plots.draw(times,aoac, times, par['AoA'], 'measured AoA(blue) vs caluclated Aoa')
# plt.savefig('AoA.eps', format = 'eps',dpi = 300)
# plots.draw(times,aoac-ca.veccat([AoAoffset])[:-1], times, par['AoA'], 'measured AoA(blue) vs caluclated Aoa-offset')
# plt.savefig('AoA_withoffset.eps', format = 'eps',dpi = 300)
