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

muro_sx_lat = PROD([CUBOID([0.25,6.25]), Q(8)])
#VIEW(muro_sx_lat)
muro_sx_lat = T([1,2])([9.75,16.75])(muro_sx_lat)
#VIEW(muro_sx_lat)

#muri interni
m1 = PROD([CUBOID([7.75,0.1]), Q(8)])
#VIEW(m1)
m2 = PROD([CUBOID([0.1,4.9]), Q(8)])
#VIEW(m2)
interno = STRUCT([T([1,2])([2,18])(m1),T([1,2])([6,18.1])(m2)])
#VIEW(interno)

muro_sx_parz = PROD([STRUCT(MKPOLS((v_muro_sx,f_muro_sx))), Q(8)])
#VIEW(muro_sx_parz)

muro_sx = STRUCT([muro_sx_lat, muro_sx_parz])
#VIEW(muro_sx)

#Creo Vasca
vasca = COLOR(BLUE)(PROD([CUBOID([20,9]), Q(1.8)]))
vascaT= T([1,2,3])([2,2,0.2])(vasca)
VIEW(vascaT)


base_scala_vasca = DIFFERENCE([base_scala, T([1,2,3])([2,2,0.2])(vasca)])
VIEW(base_scala_vasca)
lato_sin = STRUCT([muro_sx,base_scala,interno,vascaT])
VIEW(lato_sin)




