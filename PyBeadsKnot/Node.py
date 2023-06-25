from math import cos, sin, pi
from Bead import Bead

class Node:
	this_is_node=True
	
	def __init__(self, _x, _y, _p):
		self.x=_x
		self.y=_y
		self.parent=_p
		self.theta=0## argument
		self.center=Bead(self.x, self.y, self.parent)
		self.center.isJoint=True
		self.r=[];#four length of arms
		for i in range(4):
			self.r.append(10)
			newBD=Bead(self.edge_sx(i, 20), self.edge_sy(i, 20), self.parent)
			self.center.neighbors[i]=newBD
			newBD.neighbors[0]=self.center
		self.isJoint=False##is it a Joint node_?
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
	pass

	def drawNode(self, canvas):
		canvas.create_oval(self.x-self.parent.nodeRadius, self.y-self.parent.nodeRadius, self.x+self.parent.nodeRadius, self.y+self.parent.nodeRadius, fill='red')
		pass


class midJoint(Node):
	def __init__(self):
		super().__init__()
		self.center.isMidJoint=True
		self.neighbor[1]=None
		self.neighbor[3]=None