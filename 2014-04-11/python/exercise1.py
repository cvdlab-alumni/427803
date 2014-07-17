

from larcc import *
from pyplasm import *
#Scrivo i vertici della pianta base
V =[[1,1],[40,1],[40,5],[1,5],[53,5],[1,18],[6,18],[11,18],[53,18],[1,24],[6,24],[11,24]]

#Scrivo le celle della pianta base
FV = [[0,1,3,2],[2,3,4,8,7,6,5],[5,6,10,9],[6,7,11,10]]

base_grezza = PROD([STRUCT(MKPOLS((V,FV))), Q(2)])

#VIEW(base_grezza)

#Creo la scala
pol_base_scala = [[37,2],[40,2],[37,5],[40,5]]
f_baseScala = [[0,1,3,2]]
base_scala = PROD([STRUCT(MKPOLS((pol_base_scala,f_baseScala))), Q(2)])
#VIEW(base_scala)

base = DIFFERENCE([base_grezza, base_scala ])
#VIEW(base)

v_scale = [[0,0],[3,0],[0,0.25],[2.625,0.25],[3,0.25],[0,0.5],[2.25,0.5],[2.625,0.5],[0,0.75],[1.875,0.75],[2.25,0.75],[0,1],[1.5,1],[1.875,1],[0,1.25],[1.125,1.25],[1.5,1.25],[0,1.5],[0.75,1.5],[1.125,1.5],[0,1.75],[0.375,1.75],[0.75,1.75],[0,2],[0.375,2]]
#f_scale = [[0,1,4,3,2],[2,3,6,5,4],[4,5,8,7,6],[6,7,10,9,8],[8,9,12,11,10],[10,11,14,13,12],[12,13,16,15,14],[14,15,18,17]]
f_scale = [[0,1,4,3,2],[2,3,7,6,5],[5,6,10,9,8],[8,9,13,12,11],[11,12,16,15,14],[14,15,19,18,17],[17,18,22,21,20],[20,21,24,23]]
scala_grezza = PROD([STRUCT(MKPOLS((v_scale,f_scale))), Q(3)])

scala = T(2)(3)(R([2,3])(PI/2)(scala_grezza))

base_scala = STRUCT([T([1,2])([37,2])(scala), base])

#VIEW(scala)
#VIEW(base_scala)

#Creo muro sinistro
v_muro_sx = [[1.75,1.75],[9,1.75],[1.75,2],[2,2],[9,2],[1.75,22.75],[2,22.75],[9.75,22.75],[1.75,23],[9.75,23]]
f_muro_sx = [[0,1,4,3,2],[2,3,6,5],[5,6,7,9,8]]

muro_sx_lat = PROD([CUBOID([0.25,5.5]), Q(6)])
#VIEW(muro_sx_lat)
muro_sx_lat = T([1,2])([9.75,17.5])(muro_sx_lat)
#VIEW(muro_sx_lat)

#muri interni
m1 = PROD([CUBOID([7.75,0.1]), Q(4)])

#Creo Muro-Panca
mP = PROD([CUBOID([18.5,0.25]), Q(4)])
mPt = COLOR([0.95,0.90,0.87])(T([1,2,3])([8.75,16,2])(mP))
#Creo Muro-vasca
mV = PROD([CUBOID([9.7,0.25]), Q(4)])
mVt = COLOR([0.15,0.20,0.20])(T([1,2,3])([26.2,8,2])(mV))

#Creo Muro-panca
m5 = PROD([CUBOID([10,0.1]), Q(4)])
m5t = COLOR([0.4,0.4,0.4])(SKELETON(1)(T([1,2,3])([30,15,2])(m5)))

#Creo Panca
panca = T(3)(0.7)(PROD([CUBOID([15.599,0.8]), Q(0.1)]))
pil = PROD([CUBOID([0.35,0.8]), Q(0.7)])
pil_fila = STRUCT([pil, T(1)(2.178)]*8) 
panca = STRUCT([panca,pil_fila])
panca_t = COLOR([0.9,0.9,0.9])(T([1,2,3])([9.1,15.1,2])(panca))
#VIEW(panca)

#porte
p1 = COLOR(GRAY)(T([1,2,3])([8,18,2])(PROD([CUBOID([1,0.1]), Q(4)])))
p2 = COLOR(GRAY)(T([1,2,3])([6,20,2])(PROD([CUBOID([0.1,1]), Q(4)])))
p3 = COLOR(GRAY)(T([1,2,3])([7,21.8,2])(PROD([CUBOID([0.9,0.1]), Q(4)])))
p4 = COLOR(GRAY)(T([1,2,3])([8,22,2])(PROD([CUBOID([0.1, 0.7]), Q(4)])))

m2 = PROD([CUBOID([0.1,4.9]), Q(4)])
m3 = T([1,2,3])([6.1,21.8,2])(PROD([CUBOID([3.65,0.1]), Q(4)]))
m4 = T([1,2,3])([8,21.8,2])(PROD([CUBOID([0.1,1.2]), Q(4)]))

#VIEW(m2)
m1_porta = DIFFERENCE([T([1,2,3])([2,18,2])(m1),p1])
m2_porta = DIFFERENCE([T([1,2,3])([6,18.1,2])(m2),p2])
m3_porta = DIFFERENCE([m3,p3])
m4_porta = DIFFERENCE([m4,p4])
interno = COLOR([0.4,0.4,0.4])(SKELETON(1)(STRUCT([m1_porta,m2_porta,m3_porta,m4_porta])))


muro_sx_parz = PROD([STRUCT(MKPOLS((v_muro_sx,f_muro_sx))), Q(6)])
#VIEW(muro_sx_parz)

muro_sx = COLOR([0.95,0.90,0.87])(STRUCT([muro_sx_lat, muro_sx_parz]))
#VIEW(muro_sx)

#Creo Vasche
vasca = COLOR([0,0.85,0.95])(PROD([CUBOID([20,9]), Q(1.8)]))
vascaT= SCALE(3)(0.9)(T([1,2,3])([2,2,0.2])(vasca))
vasca2 = COLOR([0,0.85,0.95])(PROD([CUBOID([4,11]), Q(1.8)]))
vasca2T= SCALE(3)(0.9)(T([1,2,3])([48,5.75,0.2])(vasca2))

#VIEW(vascaT)



#Creo Muro-dx
nord = PROD([CUBOID([13.4,0.25]), Q(6)])
nordT = T([1,2])([39,17])(nord)
#VIEW(nordT)


est = PROD([CUBOID([0.25,11]), Q(6)])
estT = T([1,2])([52.375,6.25])(est)

sud = PROD([CUBOID([10,0.25]), Q(6)])
sudT = T([1,2])([42.4,6.25])(sud)

muro_dx = STRUCT([nordT,estT,sudT])
muro_dx = COLOR([0.15,0.22,0.2])(T([1,2])([-0.5,-0.5])(muro_dx))

#Muro in mezzo
m6 = PROD([CUBOID([6,0.25]), Q(6)])
m6t = COLOR([0.9,0.60,0.30])(T([1,2])([37, 12.2])(m6))

#Creo Muro-panca
m5 = PROD([CUBOID([10,0.1]), Q(4)])
m5t = COLOR([0.4,0.4,0.4])(SKELETON(1)(T([1,2,3])([30,15,2])(m5)))

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
c_sx = PROD([CUBOID([9,11]), Q(0.5)])
c_sxt = COLOR(WHITE)(T([1,2,3])([1,14,6])(c_sx))

#Copertura dx
c_dx = PROD([CUBOID([23,13]), Q(0.5)])
c_dxt = COLOR(WHITE)(T([1,2,3])([25,5,6])(c_dx))
apertura = T([1,2,3])([33,10,6])(PROD([CUBOID([1,3]), Q(0.5)]))
#VIEW(apertura)
c_dxt = DIFFERENCE([c_dxt,apertura])
#VIEW(c_dxt)
c_dxEsterna = PROD([CUBOID([23.2,13.2]), Q(0.1)])

c_dxtEsterna = T([1,2,3])([24.9,4.9,6.4])(c_dxEsterna)

c_dxt = DIFFERENCE([c_dxt,apertura])
c_dxtEsterna = DIFFERENCE([c_dxtEsterna,apertura])
tetto = STRUCT([c_dxt,COLOR([0.3,0.3,0.3])(c_dxtEsterna)])



base_scala_vasca = DIFFERENCE([base_scala, T([1,2,3])([2,2,0.2])(vasca)])
base_scala_vasca_doppia = DIFFERENCE([base_scala_vasca, T([1,2,3])([48,5.75,0.2])(vasca2)])

base_scala_vasca_color = COLOR(GRAY)(base_scala_vasca)
base_scala_vasca_doppia_color = COLOR([0.95,0.90,0.87])(base_scala_vasca_doppia)
padiglione = STRUCT([muro_sx,base_scala_vasca_doppia_color,interno,vascaT,mPt,mVt,vasca2T,muro_dx,m6t,m5t,c_dxt,c_sxt,tetto,c_sxt,panca_t, vdt,vdt2, vDxT, vSxT])
VIEW(padiglione)



