# !/bin/bash

if [ -f ~/.bashrc ];
then
   Loc=`find "$(cd ..; pwd)" -name "BuffPre.py"`;
   echo "alias BuffPre='python3 ${Loc}'" >> ~/.bashrc;
else
   echo "Your .bashrc does NOT exist";
fi
