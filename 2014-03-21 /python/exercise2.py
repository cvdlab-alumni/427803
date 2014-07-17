from larcc import *
from pyplasm import *
from exercise1 import *



#Creo muro sinistro
v_muro_sx = [[1.75,1.75],[8,1.75],[1.75,1.75],[1.75,1.75],[8,1.75],[1.75,21],[1.75,21],[9,21],[1.75,21],[9,21]]
f_muro_sx = [[0,1,4,3,2],[2,3,6,5],[5,6,7,9,8]]

muro_sx_lat = CUBOID([0,5.5,4])
#VIEW(muro_sx_lat)
muro_sx_lat = T([1,2,3])([9.75,17.5,2])(muro_sx_lat)
muro_sx_lat_sup = T(1)(0.25)(muro_sx_lat)
muro_sx_lat_f = STRUCT([muro_sx_lat,muro_sx_lat_sup])
#VIEW(muro_sx_lat_f)
#muri interni
m1 = T([1,2,3])([2,18,2])(CUBOID([7.75,0,4]))
m1d = T(2)(0.1)(m1)
m1f = STRUCT([m1d, m1])
#VIEW (m1f)

#porte
#p1 = COLOR(GRAY)(T([1,2,3])([8,18,2])(PROD([CUBOID([1,0.1]), Q(4)])))
#p2 = COLOR(GRAY)(T([1,2,3])([6,20,2])(PROD([CUBOID([0.1,1]), Q(4)])))
#p3 = COLOR(GRAY)(T([1,2,3])([7,21.8,2])(PROD([CUBOID([0.9,0.1]), Q(4)])))
#p4 = COLOR(GRAY)(T([1,2,3])([8,22,2])(PROD([CUBOID([0.1, 0.7]), Q(4)])))

m2 = T([1,2,3])([6,18.1,2])(CUBOID([0,4.9,4]))
m2d = T(1)(0.1)(m2)
m2f = STRUCT ([m2,m2d])
#VIEW(m2f)


m3 = T([1,2,3])([6.1,21.8,2])(CUBOID([3.65,0,4]))
m3d = T(2)(0.1)(m3)
m3f = STRUCT ([m3,m3d])
#VIEW (m3f)


m4 = T([1,2,3])([8,21.8,2])(CUBOID([0,1.2,4]))
m4d = T(1)(0.1)(m4)
m4f = STRUCT ([m4,m4d])

#VIEW(m2)
#m1_porta = DIFFERENCE([T([1,2,3])([2,18,2])(m1),p1])
#m2_porta = DIFFERENCE([T([1,2,3])([6,18.1,2])(m2),p2])
#m3_porta = DIFFERENCE([m3,p3])
#m4_porta = DIFFERENCE([m4,p4])
interno = COLOR([0.8,0.8,0.8])(STRUCT([m1f,m2f,m3f,m4f]))

#VIEW(interno)

muro_sx_parz = T(3)(2)(PROD([STRUCT(MKPOLS((v_muro_sx,f_muro_sx))), Q(4)]))
#VIEW(muro_sx_parz)

muro_sx = COLOR([0.95,0.90,0.87])(STRUCT([muro_sx_lat_f, muro_sx_parz]))
#VIEW(muro_sx)

#Creo Vasche
vasca = COLOR([0,0.85,0.95])(PROD([CUBOID([20,9]), Q(0)]))
vascaT= SCALE(3)(0.9)(T([1,2,3])([2,2,2.3])(vasca))
vasca2 = COLOR([0,0.85,0.95])(PROD([CUBOID([4,11]), Q(0)]))
vasca2T= SCALE(3)(0.9)(T([1,2,3])([48,5.75,2.01])(vasca2))

#VIEW(vascaT)

#Creo Muro-Panca
mP = PROD([CUBOID([18.5,0]), Q(4)])
mPt = COLOR([0.95,0.90,0.87])(T([1,2,3])([8.75,16.25,2])(mP))
#VIEW(mPt)

#Creo Muro-vasca
mV = PROD([CUBOID([9.7,0]), Q(4)])
mVt = COLOR([0.15,0.20,0.20])(T([1,2,3])([26.2,8.25,2])(mV))
#VIEW(mVt)

#Creo Muro-panca
m5 = PROD([CUBOID([10,0]), Q(4)])
m5t = COLOR([0.4,0.4,0.4])(SKELETON(1)(T([1,2,3])([30,15.1,2])(m5)))



#Creo Muro-dx
nord = PROD([CUBOID([13.4,0]), Q(4)])
nordT = T([1,2])([39,17.25])(nord)
#VIEW(nordT)


est = PROD([CUBOID([0,11]), Q(4)])
estT = T([1,2])([52.4,6.25])(est)

sud = PROD([CUBOID([10,0]), Q(4)])
sudT = T([1,2])([42.4,6.5])(sud)

muro_dx = T(3)(2)(STRUCT([nordT,estT,sudT]))
muro_dx = COLOR([0.15,0.22,0.2])(T([1,2])([-0.5,-0.5])(muro_dx))

#Muro in mezzo
m6 = PROD([CUBOID([6,0]), Q(4)])
m6t = COLOR([0.9,0.60,0.30])(T([1,2,3])([37, 12.45,2])(m6))

#Vetri-doppi
vd0 = PROD([CUBOID([0.1,3.375]), Q(4)])
vd1 = PROD([CUBOID([0.1,3.375]), Q(4)])
vd = STRUCT([vd0,T(2)(3.375)(vd1)])

vdt = COLOR([0.4,0.4,0.4])(SKELETON(1)(T([1,2,3])([32,8.25,2])(vd)))
vdt2 = COLOR([0.4,0.4,0.4])(SKELETON(1)(T([1,2,3])([33,8.25,2])(vd)))

#Vetri Sx
vS0 = PROD([CUBOID([3.68,0.1]), Q(4)])
vSx = STRUCT([vS0, T(1)(3.68)] * 3)
vSxT = COLOR([0.4,0.4,0.4])(SKELETON(1)(T([1,2,3])([31,6,2])(vSx)))

#VIEW(vSx)

#Vetri Dx
vD0 = PROD([CUBOID([0.1,0.9]), Q(4)])
vDx = STRUCT([vD0, T(2)(0.9)] * 8)
vDxT = COLOR([0.4,0.4,0.4])(SKELETON(1)(T([1,2,3])([45.8,8,2])(vDx)))


#Copertura sx
c_sx = PROD([CUBOID([9,11]), Q(0)])
c_sxt = COLOR(WHITE)(T([1,2,3])([1,14,6])(c_sx))

#Copertura dx
c_dx = PROD([CUBOID([23,13]), Q(0)])
c_dxEsterna = PROD([CUBOID([23.2,13.2]), Q(0)])
#VIEW(c_dxEsterna)

c_dxt = COLOR(WHITE)(T([1,2,3])([25,5,6])(c_dx))
c_dxtEsterna = T([1,2,3])([24.9,4.9,6.4])(c_dxEsterna)

apertura = T([1,2,3])([33,10,6])(PROD([CUBOID([1,3]), Q(0)]))
pad2_5 = STRUCT([piano_base, interno, muro_sx,muro_dx,vascaT,mPt,mVt,m5t,m6t,c_sxt,c_dxt])
VIEW(pad2_5)


