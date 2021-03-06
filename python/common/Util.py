SMALL_POSITIVE_NUMBER = 0.0000001
BIG_NUMBER = 1000000000
BIG_NEGATIVE_NUMBER = -1000000000

def Clamp(_val, _min, _max):
	return max(min(_val, _max), _min)

def IdentityMatrix44():
	return [[1., 0., 0., 0.] \
		   ,[0., 1., 0., 0.] \
		   ,[0., 0., 1., 0.] \
		   ,[0., 0., 0., 1.]]

def StrToDoubleList(_str):
	list = []
	values = _str.split(",")
	for i in range(0, len(values)):
		subList = []
		subValues = values[i].split(";")
		for j in range(0, len(subValues)):
			subList.append(float(subValues[j]))

		if len(subList) == 1:
			list.append(float(values[i]))
		else:
			list.append(subList)
	return list

def CreateEmptyList(_size):
	list = []
	for i in range(0, _size):
		list.append(0)
	return list

def StringToBooleanValue(_str):
	if _str == "T":
		return True
	return False

def BooleanValueToString(_bool):
	if _bool == True:
		return "T"
	return "F"