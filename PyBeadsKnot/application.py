import tkinter as tk
import math

from utils import mousePosition, isNear
from KnotGraph import knotGraph
from Node import Node, midJoint
from Edge import Edge
from file import fileIO

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
		self.nextNodeID=0
		self.nextEdgeID=0
		self.nodeRadius=5# radius of node in canvas
		self.edgeWidth=3
		self.beadsInterval=10
		#self.file=fileIO(self)
		#self.file.loadFile()

		##sample data
		sampleND1=midJoint(450, 66, self, theta=3.14)#2.678)
		sampleND2=midJoint(450, 412, self, theta=3.14)
		sampleND3=Node(300, 435, self, theta=2.896)
		sampleND4=Node(600, 435, self, theta=-2.896+1.57)##-1.464)##
		#sampleND5=Node(500, 500, self)
		self.kg.addNode(sampleND1)
		self.kg.addNode(sampleND2)
		self.kg.addNode(sampleND3)
		self.kg.addNode(sampleND4)
		#self.kg.addNode(sampleND5)
		sampleEG1=Edge(sampleND1, 0, sampleND3, 1, self)
		sampleEG2=Edge(sampleND1, 2, sampleND4, 0, self)
		sampleEG3=Edge(sampleND2, 0, sampleND3, 2, self)
		sampleEG4=Edge(sampleND4, 3, sampleND2, 2, self)
		self.kg.addEdge(sampleEG1)
		self.kg.addEdge(sampleEG2)
		self.kg.addEdge(sampleEG3)
		self.kg.addEdge(sampleEG4)
		self.draw()

	pass


	def update_coordinates(self, event):
		self.mp.x=event.x
		self.mp.y=event.y

		pass

	def buttonDragging(self, event):
		#self.canvas.delete("all")
		self.update_coordinates(event)
		if self.mp.magneticND!=None and getattr(self.mp.magneticND, 'this_is_node', False)==True:
			self.mp.magneticND.x=self.mp.x
			self.mp.magneticND.y=self.mp.y
			self.mp.magneticND.drawNode(self.canvas)
		for node in self.kg.nodes:
			node.modifyAngle()
			#for edge in self.kg.edges:
			#	edge.scalingShapeModifier()
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
		for edge in self.kg.edges:
			edge.scalingShapeModifier()
		self.kg.drawAllEdges(self.canvas)
		for node in self.kg.nodes:
			node.modifyAngle()
		self.kg.drawAllNodes(self.canvas)

		self.root.after(10, self.draw)
		pass

