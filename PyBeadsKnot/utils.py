import tkinter as tk
import math

class mousePosition:
	x=0
	y=0
	magneticND=None

def atan2vec(a,c,p,q):
	b = -c;
	d = a;
	s = (p * d - b * q) / (a * d - b * c);
	t = (a * q - p * c) / (a * d - b * c);
	ret = math.atan2(t, s);
	if (ret < 0) :
		ret += 2*math.pi;	
	return ret;


def dist(a,b,c,d):
	return math.sqrt((a-c)*(a-c)+(b-d)*(b-d))


def isNear(a,b,c,d,threshold):
	if (a-c)*(a-c)+(b-d)*(b-d)<=threshold*threshold:
		return True
	return False



