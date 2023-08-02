
#!/bin/bash

job=$1

mkdir input_files; cd  input_files; tar xzf ../input_files.tar.gz
echo "import os" > copyScript.py
echo -n "fileList = " >> copyScript.py
cat job_input_file_list_${job}.txt >> copyScript.py
echo " " >> copyScript.py
echo "#print (fileList) " >> copyScript.py
echo "currentDir = \"/eos/cms/store/group/phys_susy/razor/run2/RAW/temp/\"" >> copyScript.py
echo "print(currentDir)" >> copyScript.py
echo "newInputListFile = open(\"job_input_file_list_${job}.txt.new\",\"w\")" >> copyScript.py

echo "newFileList = []" >> copyScript.py

echo "for file in fileList:" >> copyScript.py
echo "    tmpIndex = file.rfind(\"/\")  " >> copyScript.py  
echo "    fileDir = file[:tmpIndex] + \"/\"" >> copyScript.py
echo "    #print ("dir: "+fileDir)" >> copyScript.py
echo "    fileName = file[tmpIndex+1:]" >> copyScript.py
echo "    print (\"filename : \" + fileName)" >> copyScript.py
echo "" >> copyScript.py
echo "    newDir = currentDir+\"/\"+fileDir" >> copyScript.py
echo "    os.system( \"mkdir -p \" + newDir)" >> copyScript.py
echo "    copyCommand = \"xrdcp \" + \"root://cmsxrootd.fnal.gov/\" + file + \"  \" + newDir + \"/\"" >> copyScript.py
#echo "    copyCommand = \"gfal-copy -f -t99999 -T7200 gsiftp://transfer.ultralight.org/\" + file + \"  \" + newDir + \"/\"" >> copyScript.py
#echo "    copyCommand = \"gfal-copy -f -t99999 -T7200 gsiftp://transfer-lb.ultralight.org//storage/cms/\" + file + \"  \" + newDir + \"/\"" >> copyScript.py
echo "" >> copyScript.py
echo "    if (os.path.exists(newDir + \"/\" + fileName)):" >> copyScript.py
echo "       print (\"file \" + newDir + \"/\" + fileName + \" already exists \")" >> copyScript.py
echo "    else :" >> copyScript.py
echo "        print (copyCommand)" >> copyScript.py
echo "        os.system( copyCommand )" >> copyScript.py
echo "" >> copyScript.py
echo "" >> copyScript.py
echo "    newFileList.append(\"file:\" + newDir + \"/\" + fileName)" >> copyScript.py
echo "    " >> copyScript.py
echo "" >> copyScript.py
echo "newInputListFile.write(str(newFileList))" >> copyScript.py
echo "newInputListFile.close()" >> copyScript.py
echo "" >> copyScript.py
echo "" >> copyScript.py
echo "os.system( \"mv -v \" + \"job_input_file_list_${job}.txt.new\" + \" \" + \"job_input_file_list_${job}.txt\")" >> copyScript.py
echo "os.system( \"cp ../input_files.tar.gz ../input_files.tar.gz.backup\")  " >> copyScript.py
echo "os.system( \"tar czf ../input_files.tar.gz job_input_file_list_*.txt\")" >> copyScript.py


