#!/bin/bash

# ./RunServer.sh &
# macaca server --verbose 

#运行python文件
# python tests/macaca-test-android.py

#setconfigure
CurrentEnvironment=`date +%Y%m%d%H%M%S`'Version'
echo $CurrentEnvironment

if [ -d "$CurrentEnvironment" ]; then
	rmdir -p "$CurrentEnvironment"
	echo right
fi
mkdir $CurrentEnvironment

cp -r app_file "$CurrentEnvironment"
cp -r features "$CurrentEnvironment"

cd ./$CurrentEnvironment

python features/run_test.py