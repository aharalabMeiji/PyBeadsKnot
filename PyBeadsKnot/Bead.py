class Bead:
	this_is_bead=True
	def __init__(self, _x, _y, _p):
		self.x=_x
		self.y=_y
		self.parent=_p
		self.id=_p.nextBeadID
		_p.nextBeadID += 1
		self.parent.kg.beads.append(self)
		self.c=0# ???
		self.neighbors=[None,None,None,None]
		## 0 : east overcrossing  ## 1 : south undercrossing  
		## 2 : west overcrossing  ## 3 : north undercrossing
		self.oriID=-1## �����Â������邽�߂̃r�[�Y�̒ʂ��ԍ�
		self.inUse=False##���������g�p���Ă��邩�ǂ����D
		self.isJoint=False##crossing���ǂ���
		self.parentNode=None
		self.isMidJoint=None##�o�R�n
		self.closeJoint=None###crossing�����ڂ̃r�[�Y
		##self.treated###�摜��͂̂Ƃ��̂ݎg�p
		##self.bandJoint###Joint�̒��ł�����\��Ƃ��Ɏg���A��{�I�ɎO�{����ɂȂ�
		##self.bandJoint_flag##	pass
		
	def deleteBead(self):
		self.parent.beads.delete(self)

	def otherside(self, p):
		if p==None:
			return None
		for i in range(4):	
			if p==self.neighbors[i]:
				return self.neighbors[(i+2)%4]
		return None

	def drawBead(self, canvas):
		canvas.create_oval(self.x-self.parent.beadRadius, self.y-self.parent.beadRadius, self.x+self.parent.beadRadius, self.y+self.parent.beadRadius, fill="blue")
