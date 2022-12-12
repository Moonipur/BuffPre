#!/bin/bash

comm=`find "$(cd ..; pwd)" -name "BuffPre.py"`

Loc=`grep -n "alias BuffPre='python3 ${comm}'" ~/.bashrc | cut -b 1-3`

sed -i "${Loc}d" ~/.bashrc

echo "Uninstallation is already finished"