

class fileIO:
	def __init__(self):
		self.filename="untitled"


	def loadFile(self):
		pass

	def loadBeadsKnotFile(self):
		PrintWriter file; 
		file = createWriter(file_name);
		file.println("BeadsKnot,0");
		file.println("Nodes,"+graph.nodes.size());
		for (int nodeID=0; nodeID<graph.nodes.size(); nodeID++) {
			Node nd = graph.nodes.get(nodeID);
			if (nd.inUse) {
				file.print(nd.x+","+nd.y+","+nd.theta+",");
				file.println(nd.r[0]+","+nd.r[1]+","+nd.r[2]+","+nd.r[3]);
			} else {
				file.print(0+","+0+","+0+",");
				file.println(10+","+10+","+10+","+10);
			}
		}
		file.println("Edges,"+graph.edges.size());
		for (int edgeID=0; edgeID<graph.edges.size(); edgeID++) {
			Edge ed = graph.edges.get(edgeID);
			file.println(ed.ANodeID+","+ed.ANodeRID+","+ed.BNodeID+","+ed.BNodeRID);
		}

		pass

	def loadImageFile(self):
		pass

	def loadDowkerFile(self):
		pass

	def loadRolfsenKnot(self):
		pass

	def saveFile(self):
		pass

	def saveBeadsKnotFile(self):
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
