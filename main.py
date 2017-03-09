####### BASE IMPORTS ########
import numpy as np
from math import *
import matplotlib.pyplot as plt
import Cit_par


####### OWN PROGRAMS IMPORT #######


####### BASE DATA #######


# Old Symmetric EOM
def sym_eom(muc,c,Vtas,CZa,Cmadot, KY2,CXu,CXa,CZ0,CXq,CZu,CX0,CZq,Cmu,Cma,Cmq,CXde,CZde, Cmd, CZadot ):

    C1s = np.matrix([[-2.*muc*c/(Vtas**2), 0., 0., 0.],[ 0. ,(CZadot - 2.*muc)*(c/Vtas), 0., 0.],[0., 0. ,-(c/Vtas) ,0.],[ 0., Cmadot*(c/Vtas), 0., -2.*muc*KY2*((c**2)/(Vtas**2))]])
    C2s = np.matrix([[CXu/Vtas, CXa, CZ0, CXq*(c/Vtas)],[ CZu/Vtas ,CZa ,-CX0 ,(CZq +2.*muc)*(c/Vtas)],[ 0., 0., 0. ,c/Vtas],[ Cmu/Vtas, Cma ,0. ,Cmq*(c/Vtas)]])
    C3s = np.matrix([[CXde],[ CZde],[0.],[Cmd]])

    return C1s,C2s,C3s

# Old Asymmetric EOM
def asym_eom(CYbdot, mub, b,Vtas, KX2, KXZ, KZ2, CYb, CL, CYp,CYr, Clp, Clb, Clr, Cnb,Cnp, Cnr, CYda, CYdr, Clda, Cldr,Cnda, Cndr, Cnbdot):
    C1a = np.matrix([[(CYbdot - 2.*mub)*(b/Vtas), 0., 0., 0. ],[ 0. ,(-b/(2.*Vtas)) ,0. ,0. ],[ 0. ,0. ,-2.*mub*KX2*(b**2/Vtas**2) ,2.*mub*KXZ*b**2/(Vtas**2)],[ Cnbdot*(b/Vtas), 0., 2.*mub*KXZ*(b**2/Vtas**2), -2.*mub*KZ2*(b**2/Vtas**2)]])
    C2a = np.matrix([[CYb, CL, (CYp *b)/(2*Vtas), (CYr - 4*mub)*b/(2*Vtas) ],[0., 0., b/(2*Vtas), 0. ],[ Clb, 0. ,Clp*b/(2*Vtas), Clr*b/(2*Vtas) ],[ Cnb ,0., Cnp*b/(2*Vtas), Cnr*b/(2*Vtas)]])
    C3a = np.matrix([[CYda, CYdr],[ 0., 0. ],[ Clda, Cldr],[ Cnda, Cndr]])
    return C1a,C2a,C3a

