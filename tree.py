# Copyright 2015,  Jean-Baptiste Assouad et Artemis Mucaj
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.

# Tree structure for IAC algorithm
class node(object):
	"""node for tree stucture"""
	def __init__(self, cutval,dimCutVal,data,n1,n2,LE,LEM):
		super(node, self).__init__()
		self.cutval = cutval
		self.dimCutVal = dimCutVal
		self.n1 = n1
		self.n2 = n2
		self.data = data
		self.LE = LE
		self.LEM = LEM

	def display(self):
		print "cutval =",self.cutval
		print "n1 =",self.n1
		print "n2 =",self.n2
		print "data =",self.data
		pass

# Prints tree structure
def status(tree,nbTab=0):
	for x in range(0,nbTab):
		print '    ',
		pass
	print '<',nbTab,':','tree.cutval', tree.cutval,'tree.dimCutVal', tree.dimCutVal
	for x in range(0,nbTab):
		print '    ',
		pass
	print 'size data =',len(tree.data),'size LE',len(tree.LE)
	if tree.cutval != -1:
		for x in range(0,nbTab):
			print '    ',
			pass
		print nbTab,'n1 :'
		status(tree.n1,nbTab+1)
		for x in range(0,nbTab):
			print '    ',
			pass
		print nbTab,'n2 :'
		status(tree.n2,nbTab+1)

	for x in range(0,nbTab):
		print '    ',
		pass
	print nbTab,'>'
	pass

'''
test = node(10,1,1,1)
test.display()
'''
