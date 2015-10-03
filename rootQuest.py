#usr/bin/python

from random import random

def generate():
	rand = int(100*random())
	return rand

def equation(r1,r2):
	a = 1
	b = r1 + r2
	c = (r1)*(r2)
	return "x^2 + %dx + %d" % (b, c)

def selectionMixture(a, b, c, d):
	rand = int(4*random())
	if rand == 0:
		return a
	elif rand == 1:
		return b
	elif rand == 2:
		return c
	else:
		return d

def answersPool(a, b, c, d):
	place1 = selectionMixture(a, b, c, d)
	while True:
		place2 = selectionMixture(a, b, c, d)
		if place1 != place2:
			break
	while True:
		place3 = selectionMixture(a, b, c, d)
		if place1 != place2 and place2 != place3 and place1 != place3:
			break
	while True:
		place4 = selectionMixture(a, b, c, d)
		if place1 != place4 and place2 != place4 and place3 != place4:
			break
	return "1)%d 2)%d 3)%d 4)%d" % (place1, place2, place3, place4)

 
def main():
	root1 = generate()
	root2 = generate()
	fakeRoot1 = generate()
	fakeRoot2 = generate()
	
	Equation = equation(root1, root2)
	answersPool(root1, root2, fakeRoot1, fakeRoot2)
	print "************************************************************"
	print "your equation is %s" % Equation	
	print """
select 2 roots that you think to be valid for above equation
"""
	print answersPool(root1,root2,fakeRoot1,fakeRoot2)
	print "*************************************************************"
	userIn1 = input("first root: ")
	userIn2 = input("second root: ")
	
	if (root1 == userIn1 or root1 == userIn2) and (root2 == userIn1 or root2 == userIn2):
		print "you're correct!"
	else:
		print "nope, try again"


	answer = raw_input("do you want to try again(y/n): ")
	if answer == 'y' or answer == 'Y':
		main()
	else:
		print "program exits" 

if __name__ == "__main__":
	main()
		
