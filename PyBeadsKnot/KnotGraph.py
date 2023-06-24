from Node import Node

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
	
	def drawAllNode(self, canvas):
		for node in self.nodes:
			node.drawNode(canvas)


	pass



