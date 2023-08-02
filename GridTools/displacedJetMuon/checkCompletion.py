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

outputFile = open('Status.txt', 'w')

workflowList = OrderedDict()


# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SinglePhoton_Run2016F-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_00fb8a2b497a9a2686a069da99144417_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SinglePhoton_Run2016F/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_JetHT_Run2016B-07Aug17_ver1-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_081267698fb41c84a6074a938ad43ae4_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/JetHT_Run2016B-07Aug17_ver1/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SinglePhoton_Run2016B-07Aug17_ver2-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_09cd52d04dd75859dfbb17c5dae2d527_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SinglePhoton_Run2016B-07Aug17_ver2/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016H-07Aug17-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_0b5c2221bab5789c3f7e89bd4b51ba56_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016H/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_MuonEG_Run2016H-07Aug17-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_1f2d694ff31c03b338afc5849aef7b38_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/MuonEG_Run2016H/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleMuon_Run2016B-07Aug17_ver2-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_1f7dc99de834e0ce206fa3eae7d478bb_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleMuon_Run2016B-07Aug17_ver2/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016C-07Aug17-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_272c2d2d37f454979b0c72e4ba754694_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016C/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_JetHT_Run2016D-07Aug17-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_31bc3bdfe0a8cc50b454b19709e30a6a_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/JetHT_Run2016D/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SinglePhoton_Run2016B-07Aug17_ver1-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_34c6f013de91a2f2f604706250dae3a6_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SinglePhoton_Run2016B-07Aug17_ver1/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_JetHT_Run2016G-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_3bdbe95b500b4199ee7a70d78c71e20a_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/JetHT_Run2016G/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016B-07Aug17_ver2-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_3dc579b30a8c68d989e08e06da22ee20_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016B-07Aug17_ver2/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_MuonEG_Run2016G-07Aug17-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_433215001ae045681727bad70fe2dea1_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/MuonEG_Run2016G/v1/']
###workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_JetHT_Run2016H-07Aug17-v1_v5.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_46dac98c3f61ac71ddcd3840bcd50edc_v5','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/JetHT_Run2016H/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_MuonEG_Run2016E-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_4a733385cc23b5e21499f6114257d79c_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/MuonEG_Run2016E/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SinglePhoton_Run2016G-07Aug17-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_56b1a355e9b0a459351943edf94bae42_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SinglePhoton_Run2016G/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleMuon_Run2016D-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_5df7771a4f9372b932fe57cce59a3370_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleMuon_Run2016D/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_MuonEG_Run2016F-07Aug17-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_8006e1e98ab07713e45efa0c2eac6f73_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/MuonEG_Run2016F/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_MuonEG_Run2016D-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_88ee273a8778db569daf60dde2da06ad_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/MuonEG_Run2016D/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_JetHT_Run2016E-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_93755104e0fb5b0ce9f3ba32fa524a43_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/JetHT_Run2016E/v1/']
###workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016E-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_99bd7ae10e56c4512da86e49dd19be94_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016E/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_JetHT_Run2016B-07Aug17_ver2-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_c36c1323b644554dc87cecb38a7c262b_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/JetHT_Run2016B-07Aug17_ver2/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_MuonEG_Run2016C-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_cab651263f7614883b36014433c44736_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/MuonEG_Run2016C/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SinglePhoton_Run2016C-07Aug17-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_cc854afded0a3ef51ccd58c6c8178faf_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SinglePhoton_Run2016C/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016B-07Aug17_ver1-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_d0a0453de56257240e9e4812decb0cb8_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016B-07Aug17_ver1/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_JetHT_Run2016F-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_edcc0fa3af7434ddff2bf4bf19e6f67f_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/JetHT_Run2016F/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016D-07Aug17-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_f14e040df426abc43cdf3110cb7c52d9_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016D/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleElectron_Run2016G-07Aug17-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_f6870eb794d6ffd6ff2a1cd8cdf2af60_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleElectron_Run2016G/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_SingleMuon_Run2016B-07Aug17_ver1-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_f8e49f1af477f76986888d59ea1a2fbe_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/SingleMuon_Run2016B-07Aug17_ver1/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_JetHT_Run2016C-07Aug17-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_AOD_v5_fd23342be631b51dd582cad9fbe68df9_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_AOD/JetHT_Run2016C/v1/']





#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleMuon_Run2017B-17Nov2017-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_07448738b51efce787955e9b38e31515_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleMuon_Run2017B/v1/']
###workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_JetHT_Run2017C-17Nov2017-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_46eaaf7487c86982813de1241b293fb0_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/JetHT_Run2017C/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_JetHT_Run2017E-17Nov2017-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_4ef208aaf011947485c5c6db706cf16c_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/JetHT_Run2017E/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_JetHT_Run2017F-17Nov2017-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_607671bb80f649cfec7383495c233828_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/JetHT_Run2017F/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_JetHT_Run2017B-17Nov2017-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_6225a56210fc2220034cf32bffeb0efa_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/JetHT_Run2017B/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SinglePhoton_Run2017E-17Nov2017-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_6cafb921f1809a33053ecf9959edf86a_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SinglePhoton_Run2017E/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleElectron_Run2017F-17Nov2017-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_8b8c63160a41395e590ba5b1c5d0249e_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleElectron_Run2017F/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleElectron_Run2017E-17Nov2017-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_92db3a5554b5c50324ad6a1804bd860c_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleElectron_Run2017E/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleMuon_Run2017F-17Nov2017-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_9aeaca5852adaa87cad8f4af001daf38_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleMuon_Run2017F/v1/']
###workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleMuon_Run2017E-17Nov2017-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_ac452f8995900e0c6eda6685193b5deb_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleMuon_Run2017E/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleMuon_Run2017G-17Nov2017-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_b31865f39e349ffcc2805ce02461a7ae_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleMuon_Run2017G/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleElectron_Run2017C-17Nov2017-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_c826c4811c6a7289504c5f75e847673d_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleElectron_Run2017C/v1/']
###workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_SingleMuon_Run2017C-17Nov2017-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_AOD/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_AOD_v5_c8ca0c06dc2f268aeed7af7495e3b02b_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_AOD/SingleMuon_Run2017C/v1/']


#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_JetHT_Run2018B-17Sep2018-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_0193505d2760720f389f9c0bfab26880_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/JetHT_Run2018B/v1/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_SingleMuon_Run2018B-17Sep2018-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_210b704687ac3d05bd51cb0beb5654e7_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/SingleMuon_Run2018B/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_EGamma_Run2018B-17Sep2018-v1_v4.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_86b4926bd1c81fda53b1f6b15a787859_v4','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/EGamma_Run2018B/v1/']
###workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_JetHT_Run2018A-17Sep2018-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_afcc4fe8ee218daafb1297d05b9efff9_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/JetHT_Run2018A/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_EGamma_Run2018C-17Sep2018-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_bbe5f10a7f4417fa841a83728e675688_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/EGamma_Run2018C/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_EGamma_Run2018A-17Sep2018-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_c501fe53e92fa28d675ba039b2e259b5_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/EGamma_Run2018A/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_SingleMuon_Run2018A-17Sep2018-v2_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_f332f12682101c1f9973449f9990eb73_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/SingleMuon_Run2018A/v1/']


#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_17Sept2018_AOD_v5_JetHT_Run2018D-PromptReco-v2_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_AOD_v5_1de191ecd92e431bc5a4165d9bd9656c_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/JetHT_Run2018D/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_17Sept2018_AOD_v5_SingleMuon_Run2018D-PromptReco-v2_v5.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_AOD_v5_31a9564d7ca745f3514569231d7f4ca5_v5','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/SingleMuon_Run2018D/v1/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_17Sept2018_AOD_v5_EGamma_Run2018D-PromptReco-v2_v5.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018D/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_AOD_v5_f6999bc5f321f17f0e4c3b63ac1c2667_v5','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/EGamma_Run2018D/v1/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/MC_RECO/prod_Run2_displacedJetMuonNtupler_V1p17_Fall17_RECO_v1_ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/MC_RECO/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Fall17_RECO_v1_5792377a759f91c50f38ca3a3fa1750a_v2','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/MC_Fall17/ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8/v1/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/MC_RECO/prod_Run2_displacedJetMuonNtupler_V1p17_Fall17_RECO_v1_ggH_HToSSTo4Tau_MH-125_TuneCP5_13TeV-powheg-pythia8_RunIIFall17DRPremix-PU2017_rp_94X_mc2017_realistic_v11-v1_v3.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/MC_RECO/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Fall17_RECO_v1_081f840692243e1ad1807c4dc0681357_v3','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/MC_Fall17/ggH_HToSSTodddd_MH-125_TuneCP5_13TeV-powheg-pythia8/v1/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_17Sept2018_AOD_v5_EGamma_Run2018A-17Sep2018-v2_part2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_AOD_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018_AOD_v5_c501fe53e92fa28d675ba039b2e259b5_part2_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_AOD/EGamma_Run2018A_part2/v1/']


#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms1p0_pl25_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms1p0_pl25_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms1p0_pl25_batch1/v1/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms2p0_pl250_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms2p0_pl250_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms2p0_pl250_batch1/v1/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms2p0_pl50_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms2p0_pl50_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms2p0_pl50_batch1/v1/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms4p0_pl100_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms4p0_pl100_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms4p0_pl100_batch1/v1/']

workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms4p0_pl500_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms4p0_pl500_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms4p0_pl500_batch1/v1/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToSS_SToEE_ms1p0_pl125_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7//crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_MC_Fall18_SL7_v2_ggH_HToSS_SToEE_ms1p0_pl125_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToEE_ms1p0_pl125_batch1/v1/']

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/prod_v2_ggH_HToPiPlusPiMinus_ms2p0_pl250_batch1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/MC_RECO_SL7/crab_prod/crab_displacedJetMuonNtupler_V1p17_MC_Fall18_ggH_HToSS_SToPiPlusPiMinus_ms2p0_pl250_batch1_v1','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Fall18/ggH_HToSS_SToPiPlusPiMinus_ms2p0_pl250_batch1/v1/']


RawSkimFile = open("displacedJetMuonNtuple_ggH_HToSS_SToEE_ms4p0_pl500.txt","r")

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
    #outputPD = "EGamma"

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
    RawSkimFile.seek(0)

    for line in RawSkimFile:
        if (outputFullPath in line) and (".root" in line):
            #print line
            tmpCount = tmpCount + 1

        if not TotalNumberOfJobs==999999:
            for i in range(1,TotalNumberOfJobs,1):
                if (outputFullPath in line) and ("_"+str(i)+".root" in line):
                    JobComplete[i] = True

    IncompleteJobs = ""
    IncompleteLumiMaskCommand = "mergeJSON.py "
    if not TotalNumberOfJobs==999999:
        for i in JobComplete.keys():
            if JobComplete[i] == False :
                IncompleteJobs = IncompleteJobs + str(i) + ","
                IncompleteLumiMaskCommand = IncompleteLumiMaskCommand + " " + workflowList[file][0] + "/local/run_and_lumis/job_lumis_" + str(i) + ".json"

    completionRatio = 100*(float(tmpCount) / TotalNumberOfJobs)
    #print inputDataset + " : (" + str(tmpCount) + "/" + str(TotalNumberOfJobs) + ") = " + "%.1f"%completionRatio + "%"

    print '{0:<40} {1:>20} {2:>10}'.format(inputDataset," : (" + str(tmpCount) + "/" + str(TotalNumberOfJobs) + ") = ", "%.1f"%completionRatio + "%")
    print IncompleteJobs

    outputFile.write('{0:<40} {1:>20} {2:>10}'.format(inputDataset," : (" + str(tmpCount) + "/" + str(TotalNumberOfJobs) + ") = ", "%.1f"%completionRatio + "%"))
    outputFile.write("\n")

    #get incomplete jobs lumi-mask, and produce a combined lumi-mask for recovery task
    if printRecoveryJson:
        outputFile.write(IncompleteLumiMaskCommand)
    outputFile.write("\n")


    #cleanup
    crabProjectLocalDir = workflowList[file][0] + "/local/"
    print "CrabDir: " + inputDataset + " : " + crabProjectLocalDir+"batch/"




    #Write condor submit script for local resubmission jobs
    if produceLocalResubmissionJobs == True:

        crabProjectLocalDir = workflowList[file][0] + "/local/"
        os.system("mkdir -p " + crabProjectLocalDir + "/batch/")
        os.system("mkdir -p " + crabProjectLocalDir + "/batch/out/")
        os.system("mkdir -p " + crabProjectLocalDir + "/batch/err/")
        os.system("mkdir -p " + crabProjectLocalDir + "/batch/log/")
        os.system("chmod +x " + crabProjectLocalDir + "/run_job.sh")
    
 

        condorJDLFile = open(crabProjectLocalDir+"/batch/task.jdl","w+")

        condorJDLFileTemplate = """
Universe  = vanilla
Executable = ../run_job.sh
Arguments = $(I)
Log = log/job.$(Cluster).$(Process).log
Output = out/job.$(Cluster).$(Process).out
Error = err/job.$(Cluster).$(Process).err
x509userproxy = $ENV(X509_USER_PROXY)
transfer_input_files = ../CMSRunAnalysis.sh, ../CMSRunAnalysis.tar.gz, ../InputArgs.txt, ../Job.submit, ../cmscp.py, ../gWMS-CMSRunAnalysis.sh, ../input_files.tar.gz, ../run_and_lumis.tar.gz, ../sandbox.tar.gz
should_transfer_files = YES
when_to_transfer_output = ON_EXIT

# Resources request
"""
        condorJDLFile.write(condorJDLFileTemplate)
        OSRequirement = "requirements = (OpSysAndVer =?= \"CentOS7\")"
        condorJDLFile.write(OSRequirement+"\n")
        condorJDLFile.write("RequestCpus = 1 \n")
        condorJDLFile.write("RequestMemory = 4000 \n")
        #QueueType = "workday"
        QueueType = "tomorrow"
        condorJDLFile.write("+JobFlavour = \"" + QueueType + "\"")
 
    
           
        condorJDLFileTemplate = """
# Jobs selection
Queue I from (
"""
                
        condorJDLFile.write(condorJDLFileTemplate)
        for i in JobComplete.keys():
            if JobComplete[i] == False :
                condorJDLFile.write(str(i)+"\n")

        condorJDLFile.write(")\n")
        condorJDLFile.close()

        if not os.path.exists(crabProjectLocalDir+"/run_job.original.sh") :
            os.system("cp " + crabProjectLocalDir+"/run_job.sh " + crabProjectLocalDir+"/run_job.original.sh ")
            print "run_job.original.sh does not exist. copy it from run_job.sh"
        runScript = open(crabProjectLocalDir+"/run_job.sh","w+")
        runScript.write("#!/bin/bash \n\n")
        runScript.write("export X509_USER_PROXY=/afs/cern.ch/user/s/sixie/my_proxy\n")
        runScript.close()
        os.system("cat " + crabProjectLocalDir+"/run_job.original.sh | grep -v CMSRunAnalysis.sh >> " +  crabProjectLocalDir+"/run_job.sh \n")
        runScript = open(crabProjectLocalDir+"/run_job.sh","a")
        runScript.write("sh /afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/createCopyScript.sh ${1} \n")
        runScript.write("cd input_files \n")
        runScript.write("python copyScript.py \n")
        runScript.write("cd - \n")
        runScript.close()
        os.system("cat " + crabProjectLocalDir+"/run_job.original.sh | grep CMSRunAnalysis.sh >> " +  crabProjectLocalDir+"/run_job.sh \n")
        runScript = open(crabProjectLocalDir+"/run_job.sh","a")
        runScript.write("\n")
        #runScript.write("gfal-copy -f " + outputFilename + " gsiftp://transfer.ultralight.org/" + remoteOutputDir + "/" + outputFilename.strip(".root") + "_${1}.root\n")
        runScript.write("mkdir -p " + workflowList[file][1] + "\n")
        runScript.write("cp -v displacedJetMuon_ntupler.root " + workflowList[file][1] + "/displacedJetMuon_ntupler_${1}.root\n")
        runScript.write("ls ./ -ltr\n")
        runScript.write("ls " + workflowList[file][1] + "/ -ltr\n")
        runScript.write("rm displacedJetMuon_ntupler.root \n")

        runScript.close()


