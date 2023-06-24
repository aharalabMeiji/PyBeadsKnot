import tkinter as tk
from KnotGraph import knotGraph
from Node import Node
from Edge import Edge

import math

class mousePosition:
	x=0
	y=0
	magneticND=None


class Application:
	def __init__(self, root):
		self.root = root
		self.canvas = tk.Canvas(root, width=1000, height=1000)
		self.canvas.pack()
		self.mp=mousePosition()
		self.canvas.bind("<B1-Motion>", self.buttonDragging)  # 
		self.canvas.bind("<Button-1>", self.buttonPressed)  # 
		self.canvas.bind("<ButtonRelease-1>", self.buttonReleased)  # 
		self.canvas.bind("<Motion>", self.update_coordinates) # 
		self.kg=knotGraph(self)
		self.nextBeadID=0
		self.nextNodeID=0
		self.nextEdgeID=0

		sampleND1=Node(500, 500, self)
		sampleND2=Node(300, 400, self)
		self.kg.addNode(sampleND1)
		self.kg.addNode(sampleND2)
		sampleEG1=Edge(sampleND1, 2, sampleND2, 0, self)

		self.draw()

	pass


	def update_coordinates(self, event):
		self.mp.x=event.x
		self.mp.y=event.y

		pass

	def buttonDragging(self, event):
		self.update_coordinates(event)
		if self.mp.magneticND!=None and getattr(self.mp.magneticND, 'this_is_node', False)==True:
			self.mp.magneticND.x=self.mp.x
			self.mp.magneticND.y=self.mp.y
			self.mp.magneticND.drawNode(self.canvas)
	# 

	def buttonPressed(self, event):
		self.update_coordinates(event)
		for node in self.kg.nodes:
			if isNear(self.mp.x, self.mp.y, node.x, node.y):
				self.mp.magneticND=node
				self.mp.magneticND.drawNode(self.canvas)
	

	def buttonReleased(self, event):
		self.update_coordinates(event)
		self.mp.magneticND=None


	def draw(self):
		self.canvas.delete("all")
		self.kg.drawAllNode(self.canvas)
		self.root.after(10, self.draw)
		pass



def dist(a,b,c,d):
	return math.sqrt((a-c)*(a-c)+(b-d)*(b-d))


def isNear(a,b,c,d):
	if (a-c)*(a-c)+(b-d)*(b-d)<=100:
		return True
	return False



