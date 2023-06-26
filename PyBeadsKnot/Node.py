from math import cos, sin, pi, atan2

class Node:
	this_is_node=True
	
	def __init__(self, _x, _y, _p):
		self.x=_x
		self.y=_y
		self.parent=_p
		self.theta=0## argument
		self.neighbors=[None, None, None, None]# four edges from this node
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
		elif edge.nodeB==self:
			return edge.nodeA
		return None
	def modifyAngle(self):
		pass

class midJoint(Node):
	this_is_midjoint=True
	def __init__(self, _x, _y, _p):
		super().__init__( _x, _y, _p)
		self.isMidJoint=True

	def modifyAngle(self):
		if self.neighbors[0]!=None and self.neighbors[2]!=0:
			edge0 = self.neighbors[0]
			node0=None
			node0R=-1
			if getattr(edge0,'this_is_edge', False):
				if edge0.nodeA==self:
					node0=edge0.nodeB
					node0R=edge0.rB
				elif edge0.nodeB==self:
					node0=edge0.nodeA
					node0R=edge0.rA
			if node0==None:
				return
			x0=node0.edge_x(node0R)
			y0=node0.edge_y(node0R)
			edge1 = self.neighbors[2]
			node1=None
			node1R=-1
			if getattr(edge1,'this_is_edge', False):
				if edge1.nodeA==self:
					node1=edge1.nodeB
					node1R=edge0.rB
				elif edge1.nodeB==self:
					node1=edge1.nodeA
					node1R=edge1.rA
			if node1==None:
				return
			x1=node1.edge_x(node1R)
			y1=node1.edge_y(node1R)
			argument=atan2(y0-y1, x0-x1)
			if self.theta-pi>=argument:
				argument += 2*pi
			elif self.theta+pi<argument:
				argument -= 2*pi
			if self.theta-pi/2>=argument:
				argument += pi
			elif self.theta+pi/2<argument:
				argument -= pi
			self.theta = 0.9 * self.theta + 0.1 * argument






