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

def ssd(array):
	c = mean(array)
	ss = sum((float(x)-c)**2 for x in array)
	return ss

def stddev(array,ddof=0.0):
	n = len(array)
	ss = ssd(array)
	pvar = float(ss)/(float(n)-ddof)
	return pvar**0.5
	
def ci(array,zval):
	
	std = stddev(array)
	sqrt_pop = float(len(array)) ** (1.0 / 2.0)
	ci_l = mean(array) - zval * (float(std)/sqrt_pop)
	ci_h = mean(array) + zval * (float(std)/sqrt_pop)
	return ci_l,ci_h