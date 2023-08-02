#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys
import json


targetBlocks = ['/JetHT/Run2018D-PromptReco-v2/AOD#1685cc9c-317f-46ad-a1dc-8401673a8710', '/JetHT/Run2018D-PromptReco-v2/AOD#52d30042-3060-4873-b38b-1b539f4ffb4c', '/JetHT/Run2018D-PromptReco-v2/AOD#9b123843-9a9c-480f-8c45-0848014058f1', '/JetHT/Run2018D-PromptReco-v2/AOD#38004809-ec9a-4269-b7c4-46daf05285f8', '/JetHT/Run2018D-PromptReco-v2/AOD#2d100a34-2f1e-4025-93fa-40c05297a205', '/JetHT/Run2018D-PromptReco-v2/AOD#2f8458ea-cd49-4b58-86dd-fea1201b98d3', '/JetHT/Run2018D-PromptReco-v2/AOD#61da8d48-d332-4e94-9055-5ba2ba33de31', '/JetHT/Run2018D-PromptReco-v2/AOD#9b353d19-0d09-4856-a502-2718e598103b', '/JetHT/Run2018D-PromptReco-v2/AOD#c102beec-97ec-4ed2-944b-1be34c6e4e0a', '/JetHT/Run2018D-PromptReco-v2/AOD#36b48cce-a07d-45f1-a9be-a68ca642bb92', '/JetHT/Run2018D-PromptReco-v2/AOD#4a8f0bf7-0788-43ec-8f4a-97c10f1f067a', '/JetHT/Run2018D-PromptReco-v2/AOD#7997f656-52b9-4dd3-8aa1-67dc42e78177', '/JetHT/Run2018D-PromptReco-v2/AOD#c8b50b2d-2070-4c74-9fc3-abbde54995e6']


if (len(sys.argv) -1 < 1):
    print "Error. Not enough arguments provided.\n"
    print "Usage: python printFilesInGivenBlocks.py [DatasetName]  \n"
    exit()

datasetName = sys.argv[1]
outputFile = open("fileList.txt","w")
print datasetName
command = "dasgoclient -query=\"file dataset=" + datasetName + "\" -json > tmpOutput.json"
os.system(command)

jsonFile = open("tmpOutput.json","r")
data = json.load(jsonFile)

for p in data:

    blockName = p['file'][0]['block.name']
    fileName = p['file'][0]['name']
    if blockName in targetBlocks:
        outputFile.write(fileName+"\n")
    

    

