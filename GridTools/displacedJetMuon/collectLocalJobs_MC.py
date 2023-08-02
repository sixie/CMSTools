#!/usr/bin/python

import os
import datetime
import time
import subprocess
import glob
import sys
import os.path
from collections import OrderedDict

#if (len(sys.argv) -1 < 1):
#    print "Error. Not enough arguments provided.\n"
#    print "Usage: python generateCrabLocalProjects [OSVersion] [DatasetListFile] \n"
#    exit()

#crabProjectLocalDir = sys.argv[1]
#outputLogDir = crabProjectLocalDir + "/batch/out/"
#NumberOfJobs = sum(1 for line in open(crabProjectLocalDir+"/InputArgs.txt"))
#print "Number of Jobs : " + str(NumberOfJobs)

produceLocalResubmissionJobs = True

outputFile = open('LocalSkimmingJobsStatus.txt', 'w')
cleanupFile = open('CleanupFiles.txt', 'w')

workflowList = OrderedDict()

workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/crab_prod/crab_prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_43a12d07fe5194ab07c7c4b629431176_v2/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall18/v1/ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1_v2/200221_190643/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/crab_prod/crab_prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_a387aa52a9ea2f3713a4c3620f5596a6_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall18/v1/ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1_v1/200222_145826/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/crab_prod/crab_prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_f7cb834a5d00483c6bc217a7a7361ac0_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall18/v1/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1_v1/200222_150016/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/crab_prod/crab_prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_c8a9ef590b0398e1f777bea6b707f630_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall18/v1/VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v2_v1_v1/200222_150130/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_VBFH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/crab_prod/crab_prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_ce2b96f24f656b559c8d69b01a623a3a_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall18/v1/VBFH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v2_v1_v1/200222_150250/']

workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_923cd501ad74435ff7913fcf8238016b_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1_v1/200221_191623/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_5792377a759f91c50f38ca3a3fa1750a_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1_v1/200222_145054/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_081f840692243e1ad1807c4dc0681357_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1_v1/200222_145041/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_77ea6caa541341d97625c7c2e644a27e_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v2_v1_v1/200222_145029/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_VBFH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_4c8fef63a15c89c15dfe58bcee5be057_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/VBFH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v2_v1_v1/200222_145017/']


workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_ggH_HToSSTobbbb_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_20805a9d3e9c87658a855c8f8b1903ff_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/ggH_HToSSTobbbb_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1_v1/200221_192212/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_ggH_HToSSTodddd_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_ff1bad5cecd8d222a95e63d2b9bb13aa_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Summer16/v1/sixie/ggH_HToSSTodddd_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1_v1/200222_144459/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_ggH_HToSSTo4Tau_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_8eeec281bc85b7fb64810e53cd12ef09_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Summer16/v1/sixie/ggH_HToSSTo4Tau_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1_v1/200222_144446/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_VBFH_HToSSTo4b_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_81ead234471eb944016e9a070e0e903a_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Summer16/v1/sixie/VBFH_HToSSTo4b_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_v1_v1/200222_144435/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_VBFH_HToSSTo4Tau_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_c861d84db5f25f9e0e68a67d63b73bb0_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Summer16/v1/sixie/VBFH_HToSSTo4Tau_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_v1_v1/200222_144424/']




RawSkimFile = open("displacedJetMuonNtuple_MC.txt","r")


for file in workflowList.keys():
    print file

    #Find the Number of Total Local Jobs
    NumberOfJobs = 0

    if os.path.exists(workflowList[file][0]+"/local/batch/task.jdl"):
        JDLFile = open(workflowList[file][0]+"/local/batch/task.jdl","r")
        tmplines = JDLFile.readlines()
        foundStart = False
        foundEnd = False
        for line in tmplines:
            if line.strip() == ")":
                foundEnd = True            
            if (foundStart == True and foundEnd == False):
                NumberOfJobs = NumberOfJobs + 1            
            if "Queue I from (" in line:
                foundStart = True
            
    clusterNumber = -999
    clusterNumberList = []
    printedWarning = False
    for tmp in glob.glob(workflowList[file][0]+"/local/batch/out/*.out"):
        tmpClusterNumber = tmp.split("prod")[2].split(".")[1]
        if (tmpClusterNumber not in clusterNumberList):
            clusterNumberList.append(tmpClusterNumber)
        if (clusterNumber == -999):
            clusterNumber = tmpClusterNumber
        else:
            if (not clusterNumber == tmpClusterNumber):
                if (printedWarning == False):
                    print "Warning: project has multiple condor submissions"
                    printedWarning = True
    #print clusterNumber 
    print clusterNumberList


    #Loop over all local jobs and find output log file
    if (clusterNumber == -999) :
        print "No jobs were submitted"
    else :
        for i in range(0,NumberOfJobs,1):
            exitCode = "-999"
            joboutputfile = ""

            #check all the condor submissions associated with this task
            for c in clusterNumberList:
                logfileName = workflowList[file][0]+"/local/batch/out/job." + str(c) + "." + str(i) + ".out"
                #print "Job : " + str(i)
                #print "log file: " + logfileName
                if (os.path.exists(logfileName)):
                    outputLogFile = open(logfileName)
                    #print "logfile: " + logfileName
            
                    for l in outputLogFile.readlines():
                        
                        #print "readline " + l 

                        if ("== The job had an exit code of" in l) :
                            exitCode = l.split("== The job had an exit code of")[1].strip()
                            #print "Exit Code = " + str(exitCode)
                        
                        if ("displacedJetMuon_ntupler.root" in l and "->" in l):
                            #print "found outputfile: " + l
                            joboutputfile = l.split("->")[1].replace('`','').replace("\'","").strip()
                            #print "outputfile: " + joboutputfile
             
                    outputLogFile.close()
                    
                #if one of the condor submissions had a successful version of this job, then don't need to check the others
                if (exitCode == "0"):
                    break
                

            if (exitCode == "0"):       

                crabTaskJobNumber = int(joboutputfile.split("displacedJetMuon_ntupler_")[1].replace(".root","").strip())
                remoteOutputDirectoryPart2 = "0000"
                if (crabTaskJobNumber >= 1000 and crabTaskJobNumber < 2000):
                    remoteOutputDirectoryPart2 = "0001"
                if (crabTaskJobNumber >= 2000 and crabTaskJobNumber < 3000):
                    remoteOutputDirectoryPart2 = "0002"
                if (crabTaskJobNumber >= 3000 and crabTaskJobNumber < 4000):
                    remoteOutputDirectoryPart2 = "0003"
                if (crabTaskJobNumber >= 4000 and crabTaskJobNumber < 5000):
                    remoteOutputDirectoryPart2 = "0004"
                if (crabTaskJobNumber >= 5000 and crabTaskJobNumber < 6000):
                    remoteOutputDirectoryPart2 = "0005"
                if (crabTaskJobNumber >= 6000 and crabTaskJobNumber < 7000):
                    remoteOutputDirectoryPart2 = "0006"
                if (crabTaskJobNumber >= 7000 and crabTaskJobNumber < 8000):
                    remoteOutputDirectoryPart2 = "0007"
                if (crabTaskJobNumber >= 8000 and crabTaskJobNumber < 9000):
                    remoteOutputDirectoryPart2 = "0008"
                if (crabTaskJobNumber >= 9000 and crabTaskJobNumber < 10000):
                    remoteOutputDirectoryPart2 = "0009"
                remoteOutputDirectory = workflowList[file][1] + remoteOutputDirectoryPart2 + "/"
                remoteOutputfile = remoteOutputDirectory + "displacedJetMuon_ntupler_" + joboutputfile.split("displacedJetMuon_ntupler_")[1]

                #print "Job Completed Successfully"
                #print "outputfile to copy: " + joboutputfile
                #print "remoteoutputfile = " + remoteOutputfile

                #check if the file exists in local stage out area
                if (os.path.exists(joboutputfile)):                    
             
                    #check if the file is already at Caltech T2
                    RawSkimFile.seek(0)
                    outputAlreadyAtRemoteSite = False
                    for tmpline in RawSkimFile:
                        if ( remoteOutputfile.strip() in tmpline) :
                            #print "file " + remoteOutputfile + " already at T2"
                            outputAlreadyAtRemoteSite = True
                            break
                       
                    #print joboutputfile+ " : " + str(outputAlreadyAtRemoteSite) 

                    if (outputAlreadyAtRemoteSite == False) :
                        outputFile.write("cp -v " + joboutputfile + " " + remoteOutputfile + "\n")

                #else:
                #    print "output file " + joboutputfile + " not found, check log " + logfileName + "\n"

            else :
                #print "Exit Code: " + exitCode + " : " + logfileName
                if (os.path.exists(joboutputfile)):
                    cleanupFile.write(joboutputfile+"\n")

