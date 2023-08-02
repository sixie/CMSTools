#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys
import json

#############################################################################
#These are the inputs you have to give for your own dataset
#############################################################################
jobList = [2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118,2119,2120,2121,2122,2123,2124,2125,2126,2127,2128,2129,2130,2131,2132,2133,2134,2135,2136,2137,2138,2139,2140,2141,2142,2143,2144,2145,2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163]
fileListLocation = "/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_8a24e9976d9f196e5a04a58623056c5a_v6/local/files/"
#############################################################################


fileList = []
#for i in jobList:
#    print "job "+str(i)
#    f = open(fileListLocation+"/job_input_file_list_"+str(i)+".txt", "r")
#    line = f.readline()
#    list = line.replace("[","").replace("]","").replace('"','').split(",")
#    #print line.replace("[","").replace("]","").replace('"','').split(",")
#    for a in list:
#        fileList.append(a.strip())

fileList.append("/store/data/Run2018C/EGamma/RAW-RECO/ZElectron-PromptReco-v2/000/319/524/00000/206C1F73-CE87-E811-A910-FA163E2F2005.root")
#print fileList
print "Number of Files: " + str(len(fileList))


##############################################################################################################
#Get the json file by running: dasgoclient -query="file dataset=/SingleMuon/Run2016G-v1/RAW" -json > files.txt
jsonFile = open("files.txt","r")
data = json.load(jsonFile)
##############################################################################################################


fileToBlockMap = {}

for p in data:
    #print p['file'][0]['name']
    #print p['file'][0]['block.name']
    fileToBlockMap[p['file'][0]['name']] = p['file'][0]['block.name']
    #print "\n"
    
BlockList = []

#Loop over fileList and find the blocks
for f in fileList:
    if f in fileToBlockMap.keys():
        if fileToBlockMap[f] not in BlockList:
            BlockList.append(fileToBlockMap[f])
    else:
        print "File "+f+" not found in json file"
for b in  BlockList:
    print b
print "Number of Blocks: " + str(len(BlockList))

