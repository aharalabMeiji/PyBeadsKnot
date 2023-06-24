#from Node import Node
#from Bead import Bead
from bezier import bezier

class Edge:
	this_is_edge=True
	bz=None
	#bandEdge=False
	#bandEdgeCode=0

	def __init__(self, nA,bA,nB,bB, _p):
		self.nodeA=nA
		self.beadA=bA
		self.nodeB=nB
		self.beadB=bB
		self.bz=bezier()
		self.parent=_p
		self.id=_p.nextEdgeID
		_p.nextEdgeID+=1
		pass

