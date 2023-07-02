from Node import Node, midJoint
from Edge import Edge
from KnotGraph import knotGraph
from pixel import pixel

import os
import cv2
from tkinter import filedialog

class fileIO:
	def __init__(self, p):
		self.filename="untitled.bdk"
		self.ext="bdk"
		self.parent=p#application

	def loadFile(self):
		fTyp = [("", "*"),("", "bdk"),("", "png,PNG")]
		iDir = os.path.abspath(os.path.dirname(__file__))
		file_name = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
		print(file_name)
		self.filename=file_name
		if ".bdk" in file_name[-4:]:
			self.loadBeadsKnotFile()
		elif ".png" in file_name[-4:] or ".PNG" in file_name[-4:]:
			self.loadImageFile()
		pass

	def loadBeadsKnotFile(self):
		self.parent.kg.nodes=[]
		self.parent.kg.edges=[]
		f = open(self.filename, 'r')
		self.kg=knotGraph(self)
		self.parent.nextNodeID
		datalist = f.readlines()
		if "BeadsKnot,0" in datalist[0]:
			line=1
			texts=datalist[line].split(',')
			line +=1
			if 'Nodes' in texts[0]:
				lenNodes=int(texts[1])
				for i in range(lenNodes) :
					texts=datalist[line].split(',')
					line +=1
					x=float(texts[0])
					y=float(texts[1])
					theta=float(texts[2])
					r0=float(texts[3])
					r1=float(texts[4])
					r2=float(texts[5])
					r3=float(texts[6])
					if r1==5.0 and r3==5.0:
						newND=midJoint(x,y,self.parent)
					else:
						newND=Node(x,y,self.parent)
					newND.theta=theta
					newND.r[0]=r0
					newND.r[1]=r1
					newND.r[2]=r2
					newND.r[3]=r3
					self.parent.kg.addNode(newND)
			texts=datalist[line].split(',')
			line +=1
			for node in self.parent.kg.nodes:
				node.inUse=False
				pass
			if 'Edges' in texts[0]:
				lenEdges=int(texts[1])
				for i in range(lenEdges) :
					texts=datalist[line].split(',')
					line +=1
					nA=int(texts[0])
					rA=int(texts[1])
					nB=int(texts[2])
					rB=int(texts[3])
					#if rA==3:
					#	rA=1
					#elif rA==1:
					#	rA=3
					#if rB==3:
					#	rB=1
					#elif rB==1:
					#	rB=3
					self.parent.kg.nodes[nA].inUse=True
					self.parent.kg.nodes[nB].inUse=True
					newED=Edge(self.parent.kg.nodes[nA],rA,self.parent.kg.nodes[nB],rB, self.parent)
					self.parent.kg.addEdge(newED)
		f.close()
		self.parent.canvas.delete("all")
		self.parent.kg.drawAllEdges(self.parent.canvas)
		for node in self.kg.nodes:
			node.modifyAngle()
		self.parent.kg.drawAllNodes(self.parent.canvas)

		pass

	
	def loadImageFile(self):
		im0 = cv2.imread(self.filename)
		width, height, x = im0.shape
		gray = cv2.cvtColor(im0, cv2.COLOR_BGR2GRAY)
		_, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)		
		image = cv2.bitwise_not(gray)
		# THINNING_ZHANGSUEN
		skeleton1 = cv2.ximgproc.thinning(image, thinningType=cv2.ximgproc.THINNING_ZHANGSUEN)
		
		cv2.imshow("caption",skeleton1)
		cv2.waitKey(0) 
		pixels=[]
		for w in range(width):
			for h in range(height):
				if skeleton1[w][h]==255:
					newPixel=pixel(w,h)
					pixels.append(newPixel)
					for (i,j) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
						if skeleton1[w+i][h+j]==255:
							newPixel.next.append((w+i,h+j))
		for p in pixels:
			for q in pixels:
				if (q.x, q.y) in p.next:
					p.neighbors.append(q)
			if len(p.next)==1:
				p.end=True
			elif len(p.next)>=3:
				p.trivalent=True
		ends = [p for p in pixels if p.end==True]

		pass

	def findTangetAtEndpoint(self):
		pass

	def dismissCluster():
		"""
		ì_ÇÃâÚÇèúãéÇ∑ÇÈ"""
		pass


	def removeThrone():
		"""
		Ç∆Ç∞Çî≤Ç≠"""
		#for (int u=0; u<points.size (); u++) {
		#	Bead bdU = getBead(u);
		#	if (bdU==null) {
		#		continue;
		#	}
		#	if ( getBead(u).c==1) {
		#		for (int i=nbhds.size ()-1; i>=0; i--) {
		#			Nbhd n=getNbhd(i);
		#			if (n!=null) {
		#				if (n.a==u) {
		#					Bead bdNB = getBead(n.b); 
		#					if (bdNB!=null && bdNB.c==3) {
		#						removePoint(u);
		#						bdNB.c=2;
		#					}
		#				} 
		#				if (n.b==u) {
		#					Bead bdNA = getBead(n.a);
		#					if (bdNA!=null && bdNA.c==3) {
		#						removePoint(u);
		#						bdNA.c=2;
		#					}
		#				}
		#			}
		#		}
		#	}
		#}
	}
		pass


	def loadDowkerFile(self):
		pass

	def loadRolfsenKnot(self):
		pass

	def saveFile(self):
		fTyp = [("", "*")]
		iDir = os.path.abspath(os.path.dirname(__file__))
		file_name = filedialog.asksaveasfilename(filetypes=fTyp, initialdir=iDir)
		print(file_name)
		self.filename=file_name
		if ".bdk" in file_name[-4:]:
			self.saveBeadsKnotFile()
		pass

	def saveBeadsKnotFile(self):
		self.ext="bdk"
		f = open(self.filename, 'w')
		f.write("BeadsKnot,0\n")
		lenNodes = len(self.parent.kg.nodes)
		f.write("Nodes,%d\n"%(lenNodes))
		for i in range(lenNodes) :
			nd = self.parent.kg.nodes[i]
			if nd.inUse:
				f.write("%f,%f,%f,%f,%f,%f,%f\n"%(nd.x,nd.y,nd.theta,nd.r[0],nd.r[1],nd.r[2],nd.r[3]))
			else :
				f.write("0,0,0,0,0,0,0\n")
		lenEdges = len(self.parent.kg.edges)
		f.write("Edges,%d\n"%(lenEdges))
		for i in range(lenEdges):
			ed = self.parent.kg.edges[i]
			nA=self.parent.kg.nodes.index(ed.nodeA)
			rA=ed.rA
			nB=self.parent.kg.nodes.index(ed.nodeB)
			rB=ed.rB
			f.write("%d,%d,%d,%d\n"%(nA,rA,nB,rB))
		f.close()
		pass

	def saveImageFile(self):
		pass

	def saveDowkerFile(self):
		pass


	knot_3_1=""
	knot_4_1=""
	knot_5_1=""
	knot_5_2=""
	knot_6_1=""
	knot_6_2=""
	knot_6_3=""
