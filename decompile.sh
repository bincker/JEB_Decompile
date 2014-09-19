!#/bin/bash
echo "usage: input the apk name like test.apk etc;"
read -p "input apk name: " dl
java -jar /home/bincker/Security/jeb/bin/jeb.jar --automation --script=/home/bincker/Security/jeb/plugins/JEBDecompileAll.py /home/bincker/Desktop/$dl
