#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys

tempfile = open("Datasets.txt","r")
templines = tempfile.readlines()
for line in templines:
    tmp = datasetName[1:]
    taskDir = tmp.replace("/","_") 

    print taskDir


#./runCMSSWJob.sh 1 1 /afs/cern.ch/work/s/sixie/public/Production/Skimming/CMSSW_10_5_0 /afs/cern.ch/work/s/sixie/public/Production/Skimming/CMSSW_10_5_0/src/EXOLLPCSCDTDigiCount_SKIM_RAW.py EXOLLLPCSCDTDigiCount.root /tmp/sixie/

