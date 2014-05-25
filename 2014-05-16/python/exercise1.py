from pyplasm import *
import os,sys
sys.path.insert(0, '/Users/toucherjay/Desktop/lar-cc/lib/py')
from larcc import *
from sysml import *

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

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)
#porta bagno (cella 61)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.15,.7,.15],[2.2,.5]])
master = diagram2cell(diagram,master,59)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)
#porta camera-letto (cella 65)
diagram = assemblyDiagramInit([1,3,2])([[.3],[1,1,1],[2.2,.5]])
master = diagram2cell(diagram,master,62)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)

#porta corridoio/camera1 (cella 90)
#diagram = assemblyDiagramInit([3,1,2])([[1.25,.5,1.25],[.3],[2.2,.5]])
#master = diagram2cell(diagram,master,89)

#finestra soggiorno/balcone (cella 99)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.8,1.4,.8],[2.2,.5]])
master = diagram2cell(diagram,master,95)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)

#finestra camera/balcone (cella 103)
diagram = assemblyDiagramInit([1,3,2])([[.3],[.65,.7,.65],[2.2,.5]])
master = diagram2cell(diagram,master,98)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)
#finestra1 bagno (cella 111)
diagram = assemblyDiagramInit([1,3,3])([[.3],[.625,.7,.625],[1,1.4,.3]])
master = diagram2cell(diagram,master,105)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)
#finestra2 camera (cella 115)
diagram = assemblyDiagramInit([1,3,3])([[.3],[.8,1.4,.8],[1,1.4,.3]])
master = diagram2cell(diagram,master,108)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),RED,1)
#VIEW(hpc)


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),GREEN,1)
VIEW(hpc)

#balcone

#RIMOZIONE PORTE E FINESTRE
porte = [133,139,145,151]
finestre = [180,171]
balconi = [163, 157]
balcone = [111,120,122,124,126,128,130,132,118]
toRemove2 = porte + finestre + balconi + balcone
masterF = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove2)]
DRAW(masterF)


