from larcc import *
from pyplasm import *
from exercise3 import *

#Creo Ambiente

#Terreno nord
VT = [[-20,1],[100,5],[-20,30],[100,30]]
FT = [[0,1,2,3]]

terreno = COLOR([0,0.6,0.3])(PROD([STRUCT(MKPOLS((VT,FT))), Q(0)]))

#Vialetto
VV = [[25,18],[30,18],[25,30],[25,28],[30,28],[30,30],[100,30],[100,28]]
FV = [[0,1,4,5,2,3],[4,5,6,7]]
vialeto = COLOR([0.99,0.99,0.6])(PROD([STRUCT(MKPOLS((VV,FV))), Q(0)]))


#Monte
VM = [[0,0],[20,0],[20,8]]
FM = [[0,1,2]]
monte = COLOR([0,0.6,0.3])(PROD([STRUCT(MKPOLS((VM,FM))), Q(120)]))
#VIEW(R([1,2])(PI/2)(monte))
monte_t = T([1,2])([-20,30])(R([1,2])(PI/2)(R([2,3])(PI/2)(monte)))

#Strada
VV = [[65,-10],[65,-14],[69,-14],[69,-10],[100,-10],[100,-14]]
FV = [[0,3,2,1],[2,5,4,3]]
strada = COLOR([0.11,0.11,0.11])(PROD([STRUCT(MKPOLS((VV,FV))), Q(0)]))

#Lammpioni
cil_lamp = CYLINDER([0.25,4.5])(240)
sfera = COLOR(YELLOW)(SPHERE(0.5)([9,10]))
lamp = STRUCT ([T(3)(4.8)(sfera),cil_lamp])
#VIEW(lamp)
fila_cil1 = STRUCT([lamp, T(1)(6)] * 6)
fila_cil1 = T([1,2,3])([65,-14.5,0])(fila_cil1)
cils = COLOR([0.4,0.4,0.4])(STRUCT([fila_cil1, T(2)(7.6)]))

#Albero
cil = COLOR([0.5,0.30,0.1])(CYLINDER([1,5.50])(240))
sfera = COLOR([0,0.6,0.1])(SPHERE(5)([9,10]))
alb10 = STRUCT([T(3)(10)(sfera),cil])
#VIEW(alb10)
fila_alb = STRUCT([alb10, T(1)(12)] * 2)
fila_alb2 = STRUCT([alb10, T(1)(12)] * 4)

fila_alb = T([1,2])([-18,4])(fila_alb)
fila_alb2 = T([1,2])([60,10])(fila_alb2)

alb_sx = STRUCT([fila_alb, T(2)(12)] * 3)
alb_dx = STRUCT([fila_alb2, T(2)(12)] * 2)

VIEW(STRUCT([pad_con_edifici,alb_sx,alb_dx,strada,cils]))

