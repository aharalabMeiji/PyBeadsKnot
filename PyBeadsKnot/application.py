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
		self.canvas.bind("<Motion>", self.updateCoordinates) # 
		self.kg=knotGraph(self)
		self.nextNodeID=0
		self.nextEdgeID=0
		self.nodeRadius=5# radius of node in canvas
		self.edgeWidth=3
		self.beadsInterval=10

		self.cx=0
		self.cy=0
		self.zoom=1.0

		self.file=fileIO(self)
		#self.file.loadFile()

		##sample data
		sampleData=0
		if sampleData==1:
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
		#self.draw()

	pass


	def updateCoordinates(self, event):
		self.mp.x, self.mp.y=self.canvas2World( event.x, event.y)

		pass

	def buttonDragging(self, event):
		self.canvas.delete("all")
		self.updateCoordinates(event)
		if self.mp.magneticND!=None and getattr(self.mp.magneticND, 'this_is_node', False)==True:
			self.mp.magneticND.x=self.mp.x
			self.mp.magneticND.y=self.mp.y
			for ed in self.mp.magneticND.neighbors:
				if getattr(ed, 'this_is_edge', False):
					ed.scalingShapeModifier()
			self.mp.magneticND.modifyAngle()
		self.drawAll(self.canvas)
	# 

	def buttonPressed(self, event):
		self.updateCoordinates(event)
		for node in self.kg.nodes:
			if node.inUse and isNear(self.mp.x, self.mp.y, node.x, node.y, 10):
				self.mp.magneticND=node
				#self.mp.magneticND.drawNode(self.canvas)
	

	def buttonReleased(self, event):
		self.updateCoordinates(event)
		self.mp.magneticND=None
		self.drawAll(self.canvas)



	def draw(self):
		self.root.after(10, self.draw)
		pass

	def keyPressed(self, event):
		if event.keysym=="Up":
			self.cy -= 10
			self.drawAll(self.canvas)		
			pass
		elif event.keysym=="Down":
			self.cy += 10
			self.drawAll(self.canvas)		
			pass
		elif event.keysym=="Right":
			self.cx += 10
			self.drawAll(self.canvas)		
			pass
		elif event.keysym=="Left":
			self.cx -= 10
			self.drawAll(self.canvas)		
			pass
		elif event.keysym=="1":
			self.zoom *= 1.1
			self.drawAll(self.canvas)		
			pass
		elif event.keysym=="0":
			self.zoom /= 1.1
			self.drawAll(self.canvas)		
			pass
		elif event.keysym=='o':
			self.file.loadFile()
			self.drawAll(self.canvas)		
			pass
		elif event.keysym=='s':
			self.file.saveFile()
			self.drawAll(self.canvas)		
			pass


	def world2Canvas(self, x,y):
		return self.cx+self.zoom * (x -500) + 500, self.cy+self.zoom * (y-500) + 500

	def canvas2World(self, x,y):
		return -self.cx+ (x -500) / self.zoom + 500 , -self.cy+ (y-500)/self.zoom + 500

	def drawAll(self, canvas):
		self.canvas.delete("all")
		self.kg.drawAllEdges(self.canvas)
		self.kg.drawAllNodes(self.canvas)
