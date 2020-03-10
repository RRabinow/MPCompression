#!/usr/bin/env python3
import math
import hashlib
import sys

class TNode:
	def __init__(self, value=None, weight=0, type=None, left=None, right=None):
		self.value = value
		self.weight = weight
		self.type = type
		self.left = left
		self.right = right
class Tree:
	def __init__(self, data=None, sFreq=None, hString=None):
		if (data != None):
			self.data = data
			self.freq = getFreqy(self.data)
			self.hString = getHString(self.data)
			self.nodes = buildTree(freq)
		elif(sFreq != None and  hString != None):
			self.freq = sFreq
			self.hString = sHash
			self.data = " " #placeholder
			self.nodes = buildTree(sFreq)
def getFreqy(data):
	freqTable = [[],[]]
	for i in range(0,len(data)):
		if (freqTable[0].count[data[i]] == 0): #If the letter was not previously counted, add it to the table
			freqTable[0].append(data[i])
			freqTable[1].append(data.count(data[i]))
	return freqTable
def getHString(data):
	return hashlib.sha256(data) #No need for PBKDF2 or multiple rounds here, as confidentiality is not needed.

def buildTree(freq):
	leafs = []
	for i in range(0, len(freq[0])):
		leafs.append(TNode(freq[0][i], freq[1][i], "L", None))
	while len(leafs) != 1:

		min = leafs[0] #Find node with smallest weight
		for k in range(1, len(leafs)):
			if (min.weight > leafs[k].weight):
				min = leafs[k]
		leafs.remove(min)

		min2 = leafs[0] #Find node with second smallest weight
		for k in range(0, len(leafs)):
                        if (min.weight > leafs[k].weight):
                                min2 = leafs[k]
		leafs.remove(min2)

		leaf.append(TNode(null, min.weight + min2.weight, "S", min, min2)) #Save both nodes by linking them to a "Split" node inserted into leafs[] list

	return  leafs[0] #return last remaining "leaf" which is really the head of the tree


buildTree(input())
