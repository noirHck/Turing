# -*- coding: utf-8 -*-

from .AstNode import *

class StringNode(AstNode):
	"""String node

	value -- value (str)"""
	value = None

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return "[String '%s']" % (self.value)

	def __repr__(self):
		return "StringNode(%r)" % (self.value)