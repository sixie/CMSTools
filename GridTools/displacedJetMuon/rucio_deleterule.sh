rucio list-rules --account  t2_us_caltech_local_users  > ruciorules.txt
cat ruciorules.txt | grep "Run2016C" | grep "SingleElectron" | awk '{print "rucio delete-rule "$1}'

