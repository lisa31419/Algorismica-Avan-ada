import random

def min2time(m):
	hh = str(int(m/60))
	if len(hh) == 1:
		hh = '0' + hh
	mm = str(m % 60)
	if len(mm) == 1:
		mm = '0' + mm
	return hh + ':' + mm

def randomActivities(s, e, minimum=.25, maximum=3):
	A = [(random.randint(s*60, (e - minimum)*60), random.randint(minimum*60, maximum*60)) for _ in range(20)]
	A = [(a[0], min([a[0] + a[1], e * 60])) for a in A]
	return list(map(lambda a: (min2time(a[0]),min2time(a[1])), A))