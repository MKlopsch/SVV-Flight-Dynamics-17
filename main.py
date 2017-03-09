########## BASE IMPORTS ########
import numpy as np
import math
import matplotlib.pyplot as plt
import Cit_par


####### OWN PROGRAMS IMPORT #######


####### BASE DATA #######


# Symmetric EOMs Matrices
def sym_c123(mu_c, c_bar, V, C_Z_alpha, C_m_a_dot, K_Y, C_X_u, C_X_alpha, C_Z_0, C_X_q, C_Z_u, C_X_0, C_Z_q, C_m_u, C_m_alpha, C_m_q, C_X_deltae, C_Z_deltae, C_m_deltae, C_Z_a):

    C1 = np.matrix([[-2.0 * mu_c * c_bar / (V**2), 0.0, 0.0, 0.0], [0.0, (C_Z_a - 2.0 * mu_c) * (c_bar / V), 0.0, 0.0], [0.0, 0.0, -(c_bar / V), 0.0], [0.0, C_m_a_dot * (c_bar / V), 0.0, -2.0 * mu_c * (K_Y**2) * (c_bar**2 / V**2)]])
    C2 = np.matrix([[C_X_u / V, C_X_alpha, C_Z_0, C_X_q * (c_bar / V)], [C_Z_u / V, C_Z_a, -C_X_0, (C_Z_q + 2.0 * mu_c) * (c_bar / V)], [0.0, 0.0, 0.0, c_bar / V], [C_m_u / V, C_m_alpha, 0.0, C_m_q * (c_bar / V)]])
    C3 = np.matrix([[C_X_deltae], [C_Z_deltae], [0.0], [C_m_deltae]])

    return C1, C2, C3

# Asymmetric EOMs Marices
def asym_c123(C_Y_beta_dot, mu_b, b, V, K_X, K_XZ, K_Z, C_Y_beta, C_L, C_Y_p, C_Y_r, C_l_p, C_l_beta, C_l_r, C_n_beta, C_n_p, C_n_r, C_Y_delta_alpha, C_Y_deltar, C_l_delta_alpha, C_l_deltar, C_n_delta_alpha, C_n_deltar, C_n_beta_dot):
    C1 = np.matrix([[(C_Y_beta_dot - 2.0 * mu_b) * (b / V), 0.0, 0.0, 0.0], [0.0, -(b / (2.0 * V)), 0.0, 0.0], [0.0, 0.0, -2.0 * mu_b * K_X**2 * (b**2 / V**2), 2.0 * mu_b * K_XZ * b**2 / (V**2)], [C_n_beta_dot * (b / V), 0.0, 2.0 * mu_b * K_XZ * (b**2 / V**2), -2.0 * mu_b * K_Z**2 * (b**2 / V**2)]])
    C2 = np.matrix([[C_Y_beta, C_L, (C_Y_p * b) / (2.0 * V), (C_Y_r - 4.0 * mu_b) * b / (2.0 * V)], [0.0, 0.0, b / (2 * V), 0.0], [C_l_beta, 0.0, C_l_p * b / (2.0 * V), C_l_r * b / (2.0 * V)], [C_n_beta, 0.0, C_n_p * b / (2.0 * V), C_n_r * b / (2.0 * V)]])
    C3 = np.matrix([[C_Y_delta_alpha, C_Y_deltar], [0.0, 0.0], [C_l_delta_alpha, C_l_deltar], [C_n_delta_alpha, C_n_deltar]])

    return C1, C2, C3

# State-Space Matrices
def SS_matrices(C1, C2, C3):
    A = -1.0 * np.dot(np.linalg.inv(C1), C2)
    B = -1.0 * np.dot(np.linalg.inv(C1), C3)

    return A, B
