import savemultirun
import random
import time

file = savemultirun.initializeOutput()

masterRunThing = dict()
run = dict()
times = []

for rpm in range(0, 1000):
	for y in range(0, 6):
		# dict format
		run["Finish time"] = random.random() * 1800
		run["Average mph"] = random.random() * 100
		run["Average power"] = random.random() * 18000
		run["Maximum power"] = random.random() * 100000
		run["Energy used"] = random.random() * 20000
		run["Max lateral acceleration"] = random.random() * 10
		run["% rpm limit"] = random.random()
		run["% torque limit"] = random.random()
		run["RPM limit"] = random.randint(0,15000)
		run["Torque limit"] = random.randint(0,15000)
		run["Passed"] = True if random.randint(0,1) == 1 else False
		
		start = time.clock()
		masterRunThing = savemultirun.writeRun( masterRunThing, run, file )
		dur = time.clock() - start
		times.append(dur)

print 'Avg execution: ' + str( sum(times)/float(len(times)) )