from math import cos, sin, pi

class Node:
	this_is_node=True
	
	def __init__(self, _x, _y, _p):
		self.x=_x
		self.y=_y
		self.parent=_p
		self.theta=0## argument
		self.neighbors=[None, None, None, None]
		self.r=[10,10,10,10];#four length of arms
		self.isJoint=True##is it a Joint node_?
		self.isMidJoint=False
		self.drawOn=False  ## show this node?
		self.id=self.parent.nextNodeID # ID of nodes
		self.parent.nextNodeID+=1
		self.inUse=True # is it in use?
		pass

	def edge_x(self, i) :
		return self.x + self.r[i] * cos(self.theta+pi/2*i)
	def edge_y(self, i) :
		return self.y + self.r[i] * sin(self.theta+pi/2*i)
	def edge_sx(self, i, s) :
		return self.x + s * cos(self.theta+pi/2*i)
	def edge_sy(self, i, s) :
		return self.y + s * sin(self.theta+pi/2*i)

	def getR(self, i):
		if isinstance(i, int):
			return self.r[i%4]
	def setR(self, i, rr):
		if isinstance(i, int) and isinstance(rr, float):
			self.r[i%4]=rr

	def drawNode(self, canvas):
		canvas.create_oval(self.x-self.parent.nodeRadius, self.y-self.parent.nodeRadius, self.x+self.parent.nodeRadius, self.y+self.parent.nodeRadius, fill='red')
		pass
	def otherside(self, p):
		if p==None:
			return None
		for i in range(4):	
			if p==self.neighbors[i]:
				return self.neighbors[(i+2)%4]
		return None

	def nextNode(self, i):
		if self.neighbors[i]==None:
			return None
		if getattr(self.neightbors[i], 'this_is_edge', False)==False:
			return None
		edge=self.neightbors[i]
		if edge.nodeA==self:
			return edge.nodeB
		if edge.nodeB==self:
			return edge.nodeA
		return None

class midJoint(Node):
	def __init__(self, _x, _y, _p):
		super().__init__( _x, _y, _p)
		self.isMidJoint=True

