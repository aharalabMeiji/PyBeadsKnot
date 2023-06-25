
class knotGraph:
	#knotExtract:de 
	#table=[];
	#disp=None
	def __init__(self, _p):
		self.nodes=[]
		self.edges=[]
		self.beads=[]
		self.parent=_p

	def addNode(self, nd):
		if getattr(nd,'this_is_node', False):
			self.nodes.append(nd)
	
	def drawAllNodes(self, canvas):
		for node in self.nodes:
			node.drawNode(canvas)

	def addEdge(self, ed):
		if getattr(ed, 'this_is_edge', False):
			self.edges.append(ed)

	def drawAllEdges(self, canvas):
		for edge in self.edges:
			edge.drawEdge(canvas)

	def drawAllBeads(self, canvas):
		for bead in self.beads:
			bead.drawBead(canvas)


	pass



