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

outputFile = open('FileTransferCommands.txt', 'w')
cleanupFile = open('CleanupFiles.txt', 'w')

workflowList = OrderedDict()


#workflowList[''] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/201X/data_RAW/crab_prod//','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data201X_RAW//']

# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleElectron_Run2016B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_64c06b80f784b46a78a6f90e57854509_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleElectron_Run2016B-v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_RAW/v1/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_Run2016B-v1_v1_v1/210116_141935/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleElectron_Run2016B-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_a7ce4a0b0af1ad3286886a04fca80093_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleElectron_Run2016B-v2/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_RAW/v1/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_Run2016B-v2_v1_v1/201217_034907/']
# #/SingleElectron/Run2016B-v2/RAW -> many blocks were not on disk
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleElectron_Run2016C-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_0bbd0f92e1d1fea5fc3cf45968132dd1_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleElectron_Run2016C/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_RAW/v1/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_Run2016C-v2_v1_v1/210116_141944/']
# #workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleElectron_Run2016D-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_f17992072227a148dcb454c3f2f34d11_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleElectron_Run2016D/','']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleElectron_Run2016E-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_278617ead9dd4d4817f81501e8211afb_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleElectron_Run2016E-v2/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_RAW/v1/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_Run2016E-v2_v1_v1/201217_034858/']
# #workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleElectron_Run2016F-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_53955853b232b3f4c5b5dfb96d133f9a_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleElectron_Run2016F/','']
# #workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleElectron_Run2016G-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_9e27ae4c5a77c82bf18e1a004a4224f6_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleElectron_Run2016G/','']
# #/SingleElectron/Run2016H-v1/RAW

# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleMuon_Run2016B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_5e92db095465b7a06c278d91ce3adeb3_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleMuon_Run2016B-v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_Run2016B-v1_v1_v1/210116_141913/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleMuon_Run2016B-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_529bedc1bb5643f4d396e6d18180dcc8_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleMuon_Run2016B-v2/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_Run2016B-v2_v1_v1/201217_034851/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleMuon_Run2016C-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_02f42f85ab6109e8288ae812ba43f875_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleMuon_Run2016C-v2/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_Run2016C-v2_v1_v1/201217_034843/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleMuon_Run2016D-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_1c2086fe537d1b1776cc676798dd9be7_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleMuon_Run2016D/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_Run2016D-v2_v1_v1/210116_141921/']
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleMuon_Run2016E-v2_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_dbb21208b77584bf8ecb69672fb36ff4_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleMuon_Run2016E-v2/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_Run2016E-v2_v1_v1/201217_034836/']
# #/SingleMuon/Run2016F-v1/RAW
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_SingleMuon_Run2016G-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2016/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_v1_6f3704e67c3ef28ebfa246dbb9a22d28_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2016_RAW/SingleMuon_Run2016G-v1/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2016_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2016_RAW_Run2016G-v1_v1_v1/201217_034828/']
# #/SingleMuon/Run2016H-v1/RAW


# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleMuon_Run2017A-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_e09a76c3e07daaf4aaf9d08291460a4a_v2/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleMuon_Run2017A/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_Run2017A-v1_v1_v2/201217_042945/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleMuon_Run2017B-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_32210dbf4dd3b163bc84c1ddc56b5718_v2/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleMuon_Run2017B/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_Run2017B-v1_v1_v2/201217_042953/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleMuon_Run2017C-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_95912d08dccd7e9ab3abcf1486d83744_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleMuon_Run2017C/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_Run2017C-v1_v1_v1/210116_141214/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleMuon_Run2017D-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_33cd049e4090e03f65317ee87e325b2b_v2/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleMuon_Run2017D/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_Run2017D-v1_v1_v2/201217_043000/']
# #/SingleMuon/Run2017D-v1/RAW --> some blocks not on disk
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleMuon_Run2017E-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_8a24e9976d9f196e5a04a58623056c5a_v2/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleMuon_Run2017E/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_Run2017E-v1_v1_v2/201217_043009/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleMuon_Run2017F-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_07c4b6c1af86e474d337910b0b484eda_v2/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleMuon_Run2017F/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_Run2017F-v1_v1_v2/201217_043017/']
# #/SingleMuon/Run2017F-v1/RAW --> some blocks not on disk
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleMuon_Run2017G-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_624b51a647a4df8d80556318fd56feb9_v2/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleMuon_Run2017G/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_Run2017G-v1_v1_v2/201217_043024/']
# #/SingleMuon/Run2017G-v1/RAW --> some blocks not on disk
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleMuon_Run2017H-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_bb1a93534d6d45138cf7e56c330ca061_v2/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleMuon_Run2017H/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_Run2017H-v1_v1_v2/201217_043034/']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleElectron_Run2017A-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_95c71d0f329ad0bb1939cab8bf6075a8_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleElectron_Run2017A/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_RAW/v1/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_Run2017A-v1_v1_v1/210116_141849/']
# #workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleElectron_Run2017B-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_723dcc1d1b17ede5c0b75cd099dfc315_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleElectron_Run2017B/','']
# #workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleElectron_Run2017C-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_c35a5779275aa1ada0611c28ba083520_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleElectron_Run2017C/','']
# #workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleElectron_Run2017D-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_757f4bf517c19fce0aa2f5e5ca9e1f3f_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleElectron_Run2017D/','']
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_SingleElectron_Run2017E-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2017/data_RAW/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_v1_5ee49aad39e9f762f508891f50123b36_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2017_RAW/SingleElectron_Run2017E/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2017_RAW/v1/sixie/SingleElectron/Run2_displacedJetMuonNtupler_V1p17_Data2017_RAW_Run2017E-v1_v1_v1/210116_141920/']
# #/SingleElectron/Run2017F-v1/RAW



# #/SingleMuon/Run2018A-v1/RAW
# #/SingleMuon/Run2018B-v1/RAW
# workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_RAW_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018ABC_RAW_v1_SingleMuon_Run2018C-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_RAW_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018ABC_RAW_v1_65398c98a0b9af91fbc856efb202b4f3_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_RAW/SingleMuon_Run2018C/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018ABC_RAW/v1/sixie/SingleMuon/Run2_displacedJetMuonNtupler_V1p17_Data2018ABC_RAW_Run2018C-v1_v1_v1/201217_013045/']
# #/SingleMuon/Run2018D-v1/RAW

#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_RAW_2018ABC/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018ABC_RAW_v1_EGamma_Run2018A-v1_v1.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_RAW_2018ABC/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018ABC_RAW_v1_5bb5f5b463f74c4d3cb2a36e7c5edd4e_v1/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_RAW/EGamma_Run2018A/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018ABC_RAW/v1/sixie/EGamma/Run2_displacedJetMuonNtupler_V1p17_Data2018ABC_RAW_Run2018A-v1_v1_v1/201217_013058/']
# #/EGamma/Run2018C-v1/RAW
# #/EGamma/Run2018B-v1/RAW
#workflowList['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_RAW_2018D/prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_RAW_v1_EGamma_Run2018D-v1_v2.py'] = ['/afs/cern.ch/work/s/sixie/public/Production/displacedJetMuon/V1p17/2018/data_RAW_2018D/crab_prod/crab_prod_Run2_displacedJetMuonNtupler_V1p17_Data2018D_RAW_v1_aab8d9933c367e8f840ae9a23be62b9d_v2/','/eos/cms/store/group/phys_susy/razor/run2/displacedJetMuonNtuple/V1p17/Data2018_RAW/EGamma_Run2018D/','/store/group/phys_exotica/delayedjets/displacedJetMuonNtuple/V1p17/Data2018D_RAW/v1/sixie/EGamma/Run2_displacedJetMuonNtupler_V1p17_Data2018D_RAW_Run2018D-v1_v1_v2/201217_034613/']





RawSkimFile = open("RAWNTuples.txt","r")
 

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
                            print "found outputfile: " + l
                            tmp_joboutputfile = l.split("->")[1].replace('`','').replace("\'","").strip()
                            #this is a trick to remove weird ' symbol from bash
                            tmp = "/eos/cms/" + tmp_joboutputfile.split("/eos/cms/")[1]
                            joboutputfile = tmp.split(".root")[0] + ".root"
                            print "outputfile: " + joboutputfile
             
                    outputLogFile.close()
                    
                #if one of the condor submissions had a successful version of this job, then don't need to check the others
                if (exitCode == "0"):
                    break
                

            if (exitCode == "0"):       
               
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
                        outputFile.write("gfal-copy -f -t99999 -T7200 " + joboutputfile + " gsiftp://transfer.ultralight.org/" + remoteOutputfile + "\n")
                    else:
                        print "Already at Remote Site"

                else:
                    print "output file " + joboutputfile + " not found, check log " + logfileName + "\n"

            else :
                #print "Exit Code: " + exitCode + " : " + logfileName
                if (os.path.exists(joboutputfile)):
                    cleanupFile.write(joboutputfile+"\n")

