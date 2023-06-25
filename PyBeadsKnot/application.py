import tkinter as tk
import math

from utils import mousePosition, isNear
from knotGraph import knotGraph
from Node import Node
from Edge import Edge

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
		self.nodeRadius=10# radius of node in canvas
		self.beadRadius=5
		self.beadsInterval=10
		self.showEdge=True

		##sample data
		sampleND1=Node(500, 300, self)
		sampleND2=Node(300, 500, self)
		sampleND1.theta=math.pi/6
		self.kg.addNode(sampleND1)
		self.kg.addNode(sampleND2)
		sampleEG1=Edge(sampleND1, 1, sampleND2, 0, self)
		self.kg.addEdge(sampleEG1)
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
			if isNear(self.mp.x, self.mp.y, node.x, node.y, 10):
				self.mp.magneticND=node
				self.mp.magneticND.drawNode(self.canvas)
	

	def buttonReleased(self, event):
		self.update_coordinates(event)
		self.mp.magneticND=None


	def draw(self):
		self.canvas.delete("all")
		self.kg.drawAllNode(self.canvas)
		for edge in self.kg.edges:
			edge.scalingShapeModifier()
		if self.showEdge:
			self.kg.drawAllEdge(self.canvas)
		self.root.after(10, self.draw)
		pass
