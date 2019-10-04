#Here's where calculating all the stats in the fun world can come in

def mean(array):
	
	return (sum(array) / len(array))

def median(array):
	
	middle = ((len(array) / 2) + 0.5)
	array.sort()
	middle = int(middle)
	if(len(array) % 2) == 0:
		median = (float(array[middle]) + float(array[middle - 1])) / 2.0
		#median = array[middle]
	else:
		median = array[middle]
	return median

def min(array):
	array.sort()
	return array[0]

def max(array):
	array.sort()
	return array[-1]