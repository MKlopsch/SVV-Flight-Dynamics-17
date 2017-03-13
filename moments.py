# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 15:55:39 2017

@author: thom
"""
###### imports #######
import matplotlib.pyplot as plt
import numpy as np

#def momentplot():
massp= []
for i in range(100,5100,100):
    i = float(i)
    massp.append(i)
massp1 = np.array(massp)

###### REAL DATA ######
momentip = np.array([298.16, 591.18,879.08,1165.42,1448.40,1732.53,2014.80,2298.84,2581.92,
            2866.30,3150.18,3434.52,3718.52,4003.23,4287.76,4572.24,4856.56,5141.16,
            5425.64,5709.90,5994.04,6278.47,6562.82,6846.96,7131.00,7415.33,7699.60,
            7984.34,8269.06,8554.05,8839.04,9124.80,9410.62,9696.97,9983.40,10270.08,
            10556.84,10843.87,11131.00,11418.20,11705.50,11993.31,12281.18,12569.04,
            12856.86,13144.73,13432.48,13720.56,14008.46,14320.34])
##### LINEAR INTERPOLATION ######
checky = []
for i in range(0,len(momentip)):
    y = ((14320.34-298.16)/4900)*massp[i]
    checky.append(y)
check = np.array(checky) 
###### ERROR #######
error= momentip-check

#PLOT TO CHECK ERROR : can use the equation
#plt.plot(massp1,check)
plt.plot(massp1,momentip)
plt.plot(massp1,error)
plt.show()

#MOMENT AROUND
#3_right_loc is 288. for normal flight, 145. when close to the pilots

def momentcalc(BEMlocation, BEM, fuel, right3loc, pilot1, pilot2, coordinator, left1, right1, left2, right2, left3, right3 ):
    Mfuel = ((14320.34-298.16)/4900.)*fuel
    Mpassengers = 131.*(pilot1+pilot2) + 170.*coordinator + 214.+(left1+right1) + 251.*(left2+right2) + 288.*(left3) + right3loc*right3
    MBEM = 2677847.5
    
    m = Mfuel + Mpassengers + MBEM
    return m
    
    
    