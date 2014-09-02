# Aaron Bonnell-Kangas, July 2014
### INSTRUCTIONS ###

## Insert at the beginning of the script:
# import savemultirun
# outfile = savemultirun.initializeOutput()
# runInfoDict = dict()

## Every time you receive results from a run:
## newRun is a dict containing the run statistics
# runInfoDict = savemultirun.writeRun(runInfoDict, newRun, outfile)

import numpy
import datetime
import os.path
import json
import pickle

# returns the file reference to be used later
def initializeOutput():
	timestamp = datetime.date.today().isoformat()
	filename = 'PPIHC torque-rpm mapping data - ' + timestamp

	# if file exists, make a different one with a number
	if os.path.isfile( filename + '.json'):
		i = 1
		while os.path.isfile( filename + ' ' + str(i) + '.json' ):
			i = i + 1
		filename = filename + ' ' + str(i) + '.json'
	else:
		filename = filename + '.json'
	
	global unwritten 
	unwritten = 0
	
	return open( filename, 'w' )

# Update the output file and the master dictionary, runInfoDict, with the latest run.
# This function only writes data every five times it is called, to save on the cost of
# 	file writes.
# runInfoDict: the master dictionary of all test data
# newRun: the latest run
# outfile: the output file reference
def writeRun( runInfoDict, newRun, outfile ):
    global unwritten
    runRPM = newRun["RPM limit"]
    runTorque = newRun["Torque limit"]
    
    if not runRPM in runInfoDict:
        runInfoDict[runRPM] = dict()
    
    runInfoDict[runRPM][runTorque] = newRun.copy()
    
    
    if unwritten > 5:
        unwritten = 0
        outfile.seek(0)
        outfile.write( json.dumps(runInfoDict) )
    else:
      unwritten = unwritten + 1
    
    return runInfoDict


def closeOutput(runInfoDict,outfile):
    outfile.seek(0)
    outfile.write( json.dumps(runInfoDict) )
    outfile.flush()
    outfile.close()
    
     
	