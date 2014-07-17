from larcc import *
from pyplasm import *
from exercise2 import *

#Creo Ambiente

#Terreno nord
VT = [[-20,-20],[100,-20],[-20,30],[100,30]]
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

#Monte Scale
#Palazzo

#Edificio

ed = COLOR([0.5,0.5,0.5])(CUBOID ([15,10,10]))
edT = T([1,2])([80,-10])(ed)
edT2 = T([1,2])([60, -10])(ed)
edifici = STRUCT([edT,edT2])
pad_con_edifici = STRUCT([terreno,padiglione,monte_t,vialeto, edifici])

