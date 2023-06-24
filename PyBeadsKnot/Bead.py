class Bead:
	this_is_bead=True
	def __init__(self, _x, _y, _p):
		self.x=_x
		self.y=_y
		self.id=_p.nextBeadID
		_p.nextBeadID += 1
	pass