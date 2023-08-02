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
printRecoveryJson = False

outputFile = open('transferCommands.txt', 'w')

workflowList = OrderedDict()

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/crab_prod/crab_prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_43a12d07fe5194ab07c7c4b629431176_v2/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall18/v1/ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1_v2/200221_190643/0000/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/crab_prod/crab_prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_a387aa52a9ea2f3713a4c3620f5596a6_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall18/v1/ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1_v1/200222_145826/0000/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/crab_prod/crab_prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_f7cb834a5d00483c6bc217a7a7361ac0_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall18/v1/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v1_v1_v1/200222_150016/0000/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/crab_prod/crab_prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_c8a9ef590b0398e1f777bea6b707f630_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall18/v1/VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v2_v1_v1/200222_150130/0000/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_VBFH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2018/MC/crab_prod/crab_prod_Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_v1_ce2b96f24f656b559c8d69b01a623a3a_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall18/v1/VBFH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_Run2_displacedJetMuonNtupler_V1p15_MC_Fall18_RunIIAutumn18DRPremix-rp_102X_upgrade2018_realistic_v15-v2_v1_v1/200222_150250/0000/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_923cd501ad74435ff7913fcf8238016b_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/ggH_HToSSTobbbb_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1_v1/200221_191623/0000/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_5792377a759f91c50f38ca3a3fa1750a_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1_v1/200222_145054/0000/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_081f840692243e1ad1807c4dc0681357_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1_v1/200222_145041/0000/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_77ea6caa541341d97625c7c2e644a27e_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/VBFH_HToSSTo4b_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v2_v1_v1/200222_145029/0000/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_VBFH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2017/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_v1_4c8fef63a15c89c15dfe58bcee5be057_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/VBFH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Fall17_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v2_v1_v1/200222_145017/0000/']


workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_ggH_HToSSTobbbb_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_20805a9d3e9c87658a855c8f8b1903ff_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Fall17/v1/sixie/ggH_HToSSTobbbb_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1_v1/200221_192212/0000/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_ggH_HToSSTodddd_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_ff1bad5cecd8d222a95e63d2b9bb13aa_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Summer16/v1/sixie/ggH_HToSSTodddd_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1_v1/200222_144459/0000/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_ggH_HToSSTo4Tau_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_8eeec281bc85b7fb64810e53cd12ef09_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Summer16/v1/sixie/ggH_HToSSTo4Tau_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_v1_v1/200222_144446/0000/']
workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_VBFH_HToSSTo4b_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_81ead234471eb944016e9a070e0e903a_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Summer16/v1/sixie/VBFH_HToSSTo4b_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_v1_v1/200222_144435/0000/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_VBFH_HToSSTo4Tau_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p15/2016/MC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_v1_c861d84db5f25f9e0e68a67d63b73bb0_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p15/MC_Summer16/v1/sixie/VBFH_HToSSTo4Tau_MH-125_TuneCUETP8M1_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p15_MC_Summer16_RunIISummer16DR80Premix-PUMoriond17_rp_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_v1_v1/200222_144424/0000/']


RemoteDataFile = open("displacedJetMuonNtuple_MC_Caltech.txt","r")

for file in workflowList.keys():
    #print file
    inputDataset = ""
    outputDirectory = ""
    outputPD = ""
    outputDatasetTag = ""
    crabDir = ""

    tempfile = open(file,"r")
    for line in tempfile:
        if "config.Data.inputDataset" in line:
            #print line
            inputDataset = line.strip("config.Data.inputDataset = \"").replace('\"','').rstrip()
        if "config.Data.outLFNDirBase" in line:
            #print line
            outputDirectory = line.strip("config.Data.outLFNDirBase =").replace("\'","").rstrip()
        if "config.Data.outputDatasetTag" in line:
            outputDatasetTag = line.strip("config.Data.outputDatasetTag =").replace('\"',"").rstrip()
            
    outputPD = inputDataset.split("/")[1]
    outputFullPath = outputDirectory+outputPD+"/"+outputDatasetTag    
    #print inputDataset
    #print outputDatasetTag
    #print outputDirectory
    #print outputPD
    
    TotalNumberOfJobs = len(glob.glob(workflowList[file][0] + "/local/run_and_lumis/*.json"))    
    if (TotalNumberOfJobs == 0):
        print "Error: " + workflowList[file][0] + "\n"

    #print outputFullPath
    JobComplete = OrderedDict()
    if not TotalNumberOfJobs==999999:
        for i in range(1,TotalNumberOfJobs,1):
            JobComplete[i] = False
    IncompleteLumiFileList = []
    tmpCount = 0

    for i in range(1,TotalNumberOfJobs,1):
        localFilename = workflowList[file][1] + "displacedJetMuon_ntupler_" + str(i) + ".root"
        remoteFilename = localFilename.replace("/eos/cms/store/group/phys_susy/razor/run2/","/store/group/phys_exotica/delayedjets/")

        #print remoteFilename
        if os.path.exists(localFilename):
            #print "yes"

            #check if the file is already at Caltech T2
            RemoteDataFile.seek(0)
            outputAlreadyAtRemoteSite = False
            for tmpline in RemoteDataFile:
                if ( remoteOutputfile.strip() in tmpline) :
                    #print "file " + remoteOutputfile + " already at T2"
                    outputAlreadyAtRemoteSite = True
                    break
                       
            if not outputAlreadyAtRemoteSite:
                command = "gfal-copy -f -t99999 -T7200 " + localFilename + " gsiftp://transfer.ultralight.org/" + remoteFilename + "\n"
                outputFile.write(command)
        


