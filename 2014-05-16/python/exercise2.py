from pyplasm import *
import os,sys
sys.path.insert(0, '/Users/toucherjay/Desktop/lar-cc/lib/py')
from larcc import *
from sysml import *
from splines import *
from exercise1 import *

GRID = COMP([INSR(PROD),AA(QUOTE)])

#giardino
controlpoints = [[0, 2.3], [0.3, 5.00], [5.19, 5], [5.38, 2.43]]
dom = larDomain([3])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
garden = STRUCT(MKPOLS(obj))
garden = STRUCT([garden,POLYLINE([[0,3.3],[0,0],[8.4,0]])])
garden3D = DIFFERENCE([PROD([SOLIDIFY(garden),Q(0.3)]),CUBOID([8.4,.1,.3])])
#VIEW (SOLIDIFY(garden),Q(0.3))
#recinto
controlpoints = [[1, 3.45], [1.78, 5.05], [4.02, 5.05], [4.82, 3.6]]
dom = larDomain([64])
mapping = larBezierCurve(controlpoints)
obj = larMap(mapping)(dom)
fence = STRUCT(MKPOLS(obj))
fence = STRUCT([fence,POLYLINE([[.01,3.4],[0,0],[8.51,.1]])])
fence3D = PROD([SOLIDIFY(fence),Q(1)])
fence3D = DIFFERENCE([fence3D,PROD([SOLIDIFY(garden),Q(1)])])
garden3D = COLOR([0.012,0.753,0.234])(garden3D)

out = T([1,2])([4.5,7.6])(STRUCT([garden3D,fence3D]))



#ALTRI PIANI


DRAW = COMP([VIEW,STRUCT,MKPOLS])

#appartamento

master = assemblyDiagramInit([7,15,2])([[.3,2,.3,4,.3,1.5,.05],[.3,1,0.3,0.2,.05,3,.1,2,.1,.4,.05,1.3,.1,3,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))

#in cyan i numeri delle celle
casa = cellNumbering (master,hpc)(range(len(CV)),CYAN,1)
#VIEW(casa)

#RIMOZIONE CELLE
remove = [0,1,2,3,30,31,32,33,150,151,152,153,180,181,182,183,154,155,184,185,156,157,186,187,178,179,176,177,174,175,172,173,203,202,204,205,206,207,208,209]

#cubicroom
roomsToRemove = [37,41,45,49,53,57,93,97,101,105,109,113,117,161,163,165,167,169]

#pareti
wallsToRemove = [39,43,47,51,55,69,67,71,95,99,111]
#pavimenti
#floorsToRemove = [130,152,174,196,218,128,216,150,172,194,238,240]

toRemove = roomsToRemove + wallsToRemove + remove 


#in CV di master inserisco solo le celle NON da rimuovere
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)


#CREAZIONE PORTE E FINESTRE NELLE PARETI
#porta d'entrata (cella 27)
diagram = assemblyDiagramInit([2,1,2])([[1.7,.3],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,27)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)

#porta camera (cella 53)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.5,1,.5],[2.2,.5]])
#diagram = assemblyDiagramInit([1,1,2])([[.3],[1],[2.2,.5]])
master = diagram2cell(diagram,master,52)


#VIEW(hpc)
#porta bagno (cella 61)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.15,.7,.15],[2.2,.5]])
master = diagram2cell(diagram,master,59)

#VIEW(hpc)
#porta camera-letto (cella 65)
diagram = assemblyDiagramInit([1,3,2])([[.3],[1,1,1],[2.2,.5]])
master = diagram2cell(diagram,master,62)

#VIEW(hpc)

#finestra soggiorno/balcone (cella 99)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.8,1.4,.8],[2.2,.5]])
master = diagram2cell(diagram,master,95)

#VIEW(hpc)

#finestra camera/balcone (cella 103)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.65,.7,.65],[2.2,.5]])
master = diagram2cell(diagram,master,98)

#VIEW(hpc)
#finestra1 bagno (cella 111)
diagram = assemblyDiagramInit([1,3,3])([[.3],[.625,.7,.625],[1,1.4,.3]])
master = diagram2cell(diagram,master,105)


#VIEW(hpc)
#finestra2 camera (cella 115)
diagram = assemblyDiagramInit([1,3,3])([[.3],[.8,1.4,.8],[1,1.4,.3]])
master = diagram2cell(diagram,master,108)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)



#balcone

#RIMOZIONE PORTE E FINESTRE
porte = [133,139,145,151]
finestre = [180,171]
balconi = [163, 157]
balcone = [110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132]
toRemove2 = porte + finestre + balconi + balcone
master0 = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove2)]
DRAW(master0)

floor0 = STRUCT(MKPOLS(master0))
floor1 = T(3)(3)(STRUCT(MKPOLS(masterF)))
floor2 = T(3)(3)(floor1)
floor3 = T(3)(3)(floor2)
floor4 = T(3)(3)(floor3)
#tetto = COLOR([0.545,0.27,0])(T([1,3])([-1,15])(CUBOID([14,11,.3])))
alaE = STRUCT([floor0,floor1,floor2,floor3,floor4])
VIEW(alaE)
alaO = T(1)(0)(R([2,2])(3/2*(PI))(alaE))
ala1 = STRUCT([alaO,alaE])
ala2 = R([1,2])(PI)(ala1)
portone = T(2)(-1)(CUBOID([8.45,2,2.7]))
pianerottolo = COLOR([0.9,0.85,0.1])(T([1,2])([-5,-1.5])(CUBOID([15,3,.3])))
muro_androne = CUBOID([4.3,0.3,3])
m_andr_sx = T([1,2])([2.6,-1.5])(muro_androne)
m_andr_dx = T([1,2])([2.6,1.2])(muro_androne)
palazzo = STRUCT([ala1,ala2])
ala_scale = T([1,2])([-6.9,-1.3])(CUBOID([.3,2.6,15]))

palazzo_ingresso = DIFFERENCE([palazzo,portone])
palazzo_scale = DIFFERENCE([palazzo_ingresso,ala_scale])
VIEW(palazzo_scale)


#SCALE
DRAW = COMP([VIEW,STRUCT,MKPOLS])
master_scale = assemblyDiagramInit([2,1,2])([[.3,6.3],[2.6],[.3,2.7]])
V,CV = master_scale
hpc = SKEL_1(STRUCT(MKPOLS(master_scale)))
hpc = cellNumbering (master_scale,hpc)(range(len(master_scale[1])),RED,1)
VIEW(hpc)

toRemoveScale = [3]
master_scale = master_scale[0], [cell for k,cell in enumerate(master_scale[1]) if not (k in toRemoveScale)]

#Finestre scale
diagram = assemblyDiagramInit([1,3,3])([[.3],[.6,1.4,.6],[1,1.4,.3]])
master_scale = diagram2cell(diagram,master_scale,1)

hpc = SKEL_1(STRUCT(MKPOLS(master_scale)))
hpc = cellNumbering (master_scale,hpc)(range(len(master_scale[1])),RED,1)
VIEW(hpc)

#Rimuove finestre
removeFinestre = [6]
master_scale = master_scale[0], [cell for k,cell in enumerate(master_scale[1]) if not (k in removeFinestre)]

DRAW(master_scale)

piano_scale = T([1,2])([-6.9,-1.3])(STRUCT(MKPOLS(master_scale)))
pscale0 = T(3)(3)(piano_scale)
pscale1 = T(3)(3)(pscale0)
pscale2 = T(3)(3)(pscale1)
pscale3 = T(3)(3)(pscale2)

scale = STRUCT([piano_scale,pscale0,pscale1,pscale2,pscale3])

VIEW(STRUCT([palazzo_ingresso,pianerottolo,m_andr_dx,m_andr_sx,scale]))




