def findMaxMin(myList):
	if max(myList) == min(myList):
		return [min(myList)]
	return [min(myList),max(myList)]