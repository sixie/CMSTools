#cat k  | awk '{print "rucio add-rule --account \"t2_us_caltech_local_users\" \"cms:"$1"\" 1 T2_US_Caltech"}' > k.sh

cat k  | awk '{print "rucio add-rule --ask-approval --account \"t2_us_caltech_local_users\" \"cms:"$1"\" 1 T2_US_Caltech"}' > k.sh

