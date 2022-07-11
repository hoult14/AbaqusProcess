# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_05-06.11.02 134264
# Run by hlt on Sun Jul 10 10:01:34 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
# executeOnCaeStartup()
# openMdb('plateBuckling.cae')
#: The model database "C:\Users\hlt\Desktop\modeling range of micro-region\cae\plateBuckling.cae" has been opened.
import time

# change L
boundarys = ["cc-cc", "ss-ss", "cc-fr", "ss-fr", "ss-ss-bending", "cc-cc-bending"]
boundary = "cc-cc-bending"
assert boundary in boundarys
lengths = list(range(400, 4010, 80))
lengths.append(800 * 20)
for L in lengths:
    p = mdb.models[boundary].parts['Part-1']
    s = p.features['Shell planar-1'].sketch
    mdb.models[boundary].ConstrainedSketch(name='__edit__', objectToCopy=s)
    s1 = mdb.models[boundary].sketches['__edit__']
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=s1,
                                  upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
    d[1].setValues(value=L, )
    s1.unsetPrimaryObject()
    p = mdb.models[boundary].parts['Part-1']
    p.features['Shell planar-1'].setValues(sketch=s1)
    del mdb.models[boundary].sketches['__edit__']
    p = mdb.models[boundary].parts['Part-1']
    p.regenerate()
    #: Warning: Failed to attach mesh to part geometry.
    # remesh
    p = mdb.models[boundary].parts['Part-1']
    p.generateMesh()
    a = mdb.models[boundary].rootAssembly
    a.regenerate()
    # submit job
    mdb.Job(name=boundary + '-' + str(L), model=boundary, description='', type=ANALYSIS,
            atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
            memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
            explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
            modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
            scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,
            numGPUs=0)
    # mdb.jobs['Job-'+str(L)].submit(consistencyChecking=OFF)
    # time.sleep(5)
    mdb.jobs[boundary + '-' + str(L)].writeInput(consistencyChecking=OFF)
    del mdb.jobs[boundary + '-' + str(L)]
