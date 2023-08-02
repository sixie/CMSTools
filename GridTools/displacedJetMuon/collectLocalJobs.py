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

outputFile = open('Transfer_LocalJobs.sh', 'w')
cleanupFile = open('CleanupFiles.txt', 'w')

workflowList = OrderedDict()



##workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016E-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_99bd7ae10e56c4512da86e49dd19be94_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016E/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016E-07Aug17-v1_v5_v1/200531_004812/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_JetHT_Run2018A-17Sep2018-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_afcc4fe8ee218daafb1297d05b9efff9_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/JetHT_Run2018A/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018ABC_AOD/v5/sixie/JetHT/Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_Run2018A-17Sep2018-v1_v5_v1/200531_045902/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_JetHT_Run2017C-17Nov2017-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_46eaaf7487c86982813de1241b293fb0_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/JetHT_Run2017C/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_AOD/v5/sixie/JetHT/Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_Run2017C-17Nov2017-v1_v5_v1/200531_025815/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleMuon_Run2017E-17Nov2017-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_ac452f8995900e0c6eda6685193b5deb_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleMuon_Run2017E/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_AOD/v5/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_Run2017E-17Nov2017-v1_v5_v1/200531_030227/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleMuon_Run2017G-17Nov2017-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_b31865f39e349ffcc2805ce02461a7ae_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleMuon_Run2017G/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_AOD/v5/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_Run2017G-17Nov2017-v1_v5_v2/200611_040430/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_SingleMuon_Run2018A-17Sep2018-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_f332f12682101c1f9973449f9990eb73_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/SingleMuon_Run2018A/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018ABC_AOD/v5/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_Run2018A-17Sep2018-v2_v5_v2/200531_045531/'] 

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016H-07Aug17-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_0b5c2221bab5789c3f7e89bd4b51ba56_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016H/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016H-07Aug17-v1_v5_v4/200609_201446/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_EGamma_Run2018A-17Sep2018-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_c501fe53e92fa28d675ba039b2e259b5_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/EGamma_Run2018A/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018ABC_AOD/v5/sixie/EGamma/Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_Run2018A-17Sep2018-v2_v5_v2/200629_025904/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_EGamma_Run2018B-17Sep2018-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_86b4926bd1c81fda53b1f6b15a787859_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/EGamma_Run2018B/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018ABC_AOD/v5/sixie/EGamma/Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_Run2018B-17Sep2018-v1_v5_v4/200701_022500/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_EGamma_Run2018C-17Sep2018-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_bbe5f10a7f4417fa841a83728e675688_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/EGamma_Run2018C/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018ABC_AOD/v5/sixie/EGamma/Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_Run2018C-17Sep2018-v1_v5_v3/200701_022510/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SinglePhoton_Run2016B-07Aug17_ver2-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_09cd52d04dd75859dfbb17c5dae2d527_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SinglePhoton_Run2016B-07Aug17_ver2/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/SinglePhoton/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016B-07Aug17_ver2-v1_v5_v4/200615_185429/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_MuonEG_Run2016G-07Aug17-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_433215001ae045681727bad70fe2dea1_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/MuonEG_Run2016G/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/MuonEG/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016G-07Aug17-v1_v5_v2/200619_152801/']


#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_JetHT_Run2018B-17Sep2018-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_0193505d2760720f389f9c0bfab26880_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/JetHT_Run2018B/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018ABC_AOD/v5/sixie/JetHT/Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_Run2018B-17Sep2018-v1_v5_v4/200608_203017/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_JetHT_Run2017B-17Nov2017-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_6225a56210fc2220034cf32bffeb0efa_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/JetHT_Run2017B/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_AOD/v5/sixie/JetHT/Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_Run2017B-17Nov2017-v1_v5_v3/200606_200147/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_JetHT_Run2016D-07Aug17-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_31bc3bdfe0a8cc50b454b19709e30a6a_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/JetHT_Run2016D/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/JetHT/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016D-07Aug17-v1_v5_v2/200615_190709']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_JetHT_Run2016H-07Aug17-v1_v5.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_46dac98c3f61ac71ddcd3840bcd50edc_v5','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/JetHT_Run2016H/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/JetHT/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016H-07Aug17-v1_v5_v5/200615_205934/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleMuon_Run2017B-17Nov2017-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_07448738b51efce787955e9b38e31515_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleMuon_Run2017B/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_AOD/v5/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_Run2017B-17Nov2017-v1_v5_v1/200531_030148/']
 
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016G-07Aug17-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_f6870eb794d6ffd6ff2a1cd8cdf2af60_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016G/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016G-07Aug17-v1_v5_v2/200609_203609/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_MuonEG_Run2016F-07Aug17-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_8006e1e98ab07713e45efa0c2eac6f73_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/MuonEG_Run2016F/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/MuonEG/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016F-07Aug17-v1_v5_v3/200625_161410/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SinglePhoton_Run2016C-07Aug17-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_cc854afded0a3ef51ccd58c6c8178faf_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SinglePhoton_Run2016C/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/SinglePhoton/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016C-07Aug17-v1_v5_v3/200625_161738/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_17Sept2018_AOD_v5_EGamma_Run2018D-PromptReco-v2_v5.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_AOD_v5_f6999bc5f321f17f0e4c3b63ac1c2667_v5','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/EGamma_Run2018D/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018D_AOD/v5/sixie/EGamma/Run2_displacedJetMuonNtupler_V1p17_Data2018D_17Sept2018_AOD_Run2018D-PromptReco-v2_v5_v5/200619_151121/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_17Sept2018_AOD_v5_SingleMuon_Run2018D-PromptReco-v2_v5.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_AOD_v5_31a9564d7ca745f3514569231d7f4ca5_v5','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/SingleMuon_Run2018D/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018D_AOD/v5/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2018D_17Sept2018_AOD_Run2018D-PromptReco-v2_v5_v5/200626_151758/']
 
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleElectron_Run2017C-17Nov2017-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_c826c4811c6a7289504c5f75e847673d_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleElectron_Run2017C/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_AOD/v5/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_Run2017C-17Nov2017-v1_v5_v3/200625_163633/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleMuon_Run2017F-17Nov2017-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_9aeaca5852adaa87cad8f4af001daf38_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleMuon_Run2017F/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_AOD/v5/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_Run2017F-17Nov2017-v1_v5_v4/200626_145359/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleElectron_Run2017F-17Nov2017-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_8b8c63160a41395e590ba5b1c5d0249e_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleElectron_Run2017F/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_AOD/v5/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_Run2017F-17Nov2017-v1_v5_v3/200626_145651/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_JetHT_Run2017E-17Nov2017-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_4ef208aaf011947485c5c6db706cf16c_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/JetHT_Run2017E/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_AOD/v5/sixie/JetHT/Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_Run2017E-17Nov2017-v1_v5_v4/200626_150833/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_JetHT_Run2017F-17Nov2017-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_607671bb80f649cfec7383495c233828_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/JetHT_Run2017F/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_AOD/v5/sixie/JetHT/Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_Run2017F-17Nov2017-v1_v5_v2/200630_191211/']


#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/MC_RECO/prod_Run2_displacedJetMuonNtupler_V1p17_Fall17_RECO_v1_ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/MC_RECO/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Fall17_RECO_v1_5792377a759f91c50f38ca3a3fa1750a_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/MC_Fall17/ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/MC_Fall17/v1/sixie/ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p17_Fall17_RECO_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1_v2/200701_163029/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/MC_RECO/prod_Run2_displacedJetMuonNtupler_V1p17_Fall17_RECO_v1_ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/MC_RECO/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Fall17_RECO_v1_081f840692243e1ad1807c4dc0681357_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/MC_Fall17/ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/MC_Fall17/v1/sixie/ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8/Run2_displacedJetMuonNtupler_V1p17_Fall17_RECO_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v1_v3/200615_174402/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016D-07Aug17-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_f14e040df426abc43cdf3110cb7c52d9_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016D/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016D-07Aug17-v1_v5_v3/200703_115657/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_EGamma_Run2018A-17Sep2018-v2_part2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_c501fe53e92fa28d675ba039b2e259b5_part2_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/EGamma_Run2018A_part2/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018ABC_AOD/v5/sixie/EGamma/Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_Run2018A-17Sep2018-v2_part2_v5_v2/200718_214504/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_17Sept2018_AOD_v5_JetHT_Run2018D-PromptReco-v2_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_AOD_v5_1de191ecd92e431bc5a4165d9bd9656c_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/JetHT_Run2018D/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018D_AOD/v5/sixie/JetHT/Run2_displacedJetMuonNtupler_V1p17_Data2018D_17Sept2018_AOD_Run2018D-PromptReco-v2_v5_v3/200719_165532/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016B-07Aug17_ver2-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_3dc579b30a8c68d989e08e06da22ee20_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016B-07Aug17_ver2/v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_AOD/v5/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_Run2016B-07Aug17_ver2-v2_v5_v2/200719_163934/']


# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms1p0_pl25_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms1p0_pl25_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms1p0_pl25_batch1/v1/','/storage/cms/store/user/apresyan/delayedjets/displacedJetMuonNtuple/V1p17/MC_Fall18/v2/ggH_HToSS_SToEE_ms1p0_pl25/Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_batch1_v1/210528_174718/']

#need to resubmit it#
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms2p0_pl250_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms2p0_pl250_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms2p0_pl250_batch1/v1/','/storage/cms/store/user/apresyan/delayedjets/displacedJetMuonNtuple/V1p17/MC_Fall18/v2/ggH_HToSS_SToEE_ms2p0_pl250/Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_batch1_v1/210529_114248/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms2p0_pl50_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms2p0_pl50_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms2p0_pl50_batch1/v1/','/storage/cms//store/user/apresyan/delayedjets/displacedJetMuonNtuple/V1p17/MC_Fall18/v2/ggH_HToSS_SToEE_ms2p0_pl50/Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_batch1_v1/210529_114655/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms4p0_pl100_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms4p0_pl100_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms4p0_pl100_batch1/v1/','/store/user/apresyan/delayedjets/displacedJetMuonNtuple/V1p17/MC_Fall18/v2/ggH_HToSS_SToEE_ms4p0_pl100/Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_batch1_v1/210528_114519/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms4p0_pl500_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms4p0_pl500_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms4p0_pl500_batch1/v1/','']

workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms1p0_pl125_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms1p0_pl125_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms1p0_pl125_batch1/v1/','']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToPiPlusPiMinus_ms2p0_pl250_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/crab_prod/crab_displacedJetMuonNtupler_V1p17_MC_Fall18_ggH_HToSS_SToPiPlusPiMinus_ms2p0_pl250_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToPiPlusPiMinus_ms2p0_pl250_batch1/v1/','']




RawSkimFile = open("displacedJetMuonNtuple_ggH_HToSS_SToEE_ms2p0_pl50.txt","r")
 

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
    print clusterNumber 

    #clusterNumber = 5793571
    #clusterNumberList = []
    #clusterNumberList.append(5793571)
  
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
                print "Job : " + str(i)
                print "log file: " + logfileName
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
                            tmp_joboutputfile = l.split("->")[1].replace('`','').replace("\'","").strip()
                            #this is a trick to remove weird ' symbol from bash
                            tmp = "/eos/cms/" + tmp_joboutputfile.split("/eos/cms/")[1]
                            joboutputfile = tmp.split(".root")[0] + ".root"
                            #print "outputfile: " + joboutputfile
             
                    outputLogFile.close()
                    
                #if one of the condor submissions had a successful version of this job, then don't need to check the others
                if (exitCode == "0"):
                    break
                

            if (exitCode == "0"):       
                print (joboutputfile.split("displacedJetMuon_ntupler_")[1].replace(".root","").strip())
                crabTaskJobNumber = int(joboutputfile.split("displacedJetMuon_ntupler_")[1].split(".root")[0])
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
                remoteOutputDirectory = workflowList[file][2] + remoteOutputDirectoryPart2 + "/"
                remoteOutputfile = remoteOutputDirectory + "displacedJetMuon_ntupler_" + joboutputfile.split("displacedJetMuon_ntupler_")[1]

                print "Job Completed Successfully"
                print "outputfile to copy: " + joboutputfile
                print "remoteoutputfile = " + remoteOutputfile

                print ("Outputfile exists: " + str( os.path.exists(joboutputfile)))
                
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
                        outputFile.write("gfal-copy -f -t99999 -T7200 " + joboutputfile + " gsiftp://transfer-lb.ultralight.org/" + remoteOutputfile + "\n")
                    else:
                        print "Already at Remote Site"

                else:
                    print "output file " + joboutputfile + " not found, check log " + logfileName + "\n"

            else :
                #print "Exit Code: " + exitCode + " : " + logfileName
                if (os.path.exists(joboutputfile)):
                    cleanupFile.write(joboutputfile+"\n")

