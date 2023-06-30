from math import cos, sin, pi, atan2

class Node:
	this_is_node=True
	
	def __init__(self, _x, _y, _p, theta=0.0):
		self.x=_x
		self.y=_y
		self.parent=_p
		self.theta=theta## argument
		self.neighbors=[None, None, None, None]# four edges from this node
		self.r=[5.0,5.0,5.0,5.0];#four length of arms
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
		return self.y - self.r[i] * sin(self.theta+pi/2*i)
	def edge_sx(self, i, s) :
		return self.x + s * cos(self.theta+pi/2*i)
	def edge_sy(self, i, s) :
		return self.y - s * sin(self.theta+pi/2*i)

	def getR(self, i):
		if isinstance(i, int):
			return self.r[i%4]
	def setR(self, i, rr):
		if isinstance(i, int) and isinstance(rr, float):
			self.r[i%4]=rr

	def drawNode(self, canvas):
		if self.inUse:
			xx0,yy0=self.parent.world2Canvas(self.x-self.parent.nodeRadius,self.y-self.parent.nodeRadius)
			xx1,yy1=self.parent.world2Canvas(self.x+self.parent.nodeRadius,self.y+self.parent.nodeRadius)
			canvas.create_oval(xx0,yy0,xx1,yy1, fill='red')
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
		edges=[]
		nodes=[]
		nodeR=[]
		x=[]
		y=[]
		for i in range(4):
			if self.neighbors[i]==None:
				return
			edges.append(self.neighbors[i])
			nodes.append(None)
			nodeR.append(-1)
			if getattr(edges[-1],'this_is_edge', False):
				if edges[-1].nodeA==self:
					nodes[-1]=edges[-1].nodeB
					nodeR[-1]=edges[-1].rB
				elif edges[-1].nodeB==self:
					nodes[-1]=edges[-1].nodeA
					nodeR[-1]=edges[-1].rA
			if nodes[-1]==None:
				return
			x.append(nodes[-1].edge_sx(nodeR[-1],10))
			y.append(nodes[-1].edge_sy(nodeR[-1],10)) 
		theta0=-atan2(y[0]-y[2],x[0]-x[2])
		theta1=-atan2(y[1]-y[3],x[1]-x[3])

		if theta1<theta0:
			theta1+=2*pi
		theta=(theta0+theta1)*0.5-pi/4
		##print("%f, %f, %f"%(theta0, theta1, theta))
		self.theta = 0.99 * self.theta + 0.01 * theta

		pass

class midJoint(Node):
	this_is_midjoint=True
	def __init__(self, _x, _y, _p, theta=0.0):
		super().__init__( _x, _y, _p, theta=theta)
		self.isMidJoint=True

	def modifyAngle(self):
		"""  """
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
			x0=node0.edge_sx(node0R,10)
			y0=node0.edge_sy(node0R,10)
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
			x1=node1.edge_sx(node1R,10)
			y1=node1.edge_sy(node1R,10)
			argument=-atan2(y0-y1, x0-x1)
			if self.theta-pi>=argument:
				argument += 2*pi
			elif self.theta+pi<argument:
				argument -= 2*pi
			if self.theta-pi/2>=argument:
				argument += pi
			elif self.theta+pi/2<argument:
				argument -= pi
			self.theta = 0.9 * self.theta + 0.1 * argument






