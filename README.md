# `BuffPre`

The `BuffPre` is a simple program for calculating and preparing solution.

# Install
chmod +x install.sh

./install.sh

source ~/.bashrc

# Run test
cd test

python3 test_BuffPre.py

# Usage: 
BuffPre [options] -h

# Optional argruments:
    -b, --buffer    Buffer preparation (efault acid; base)
    -d, --dilute    Dilution of solution
    -m, --Molar     Calculate Molar of solution
    -r, --recovery  Calculate the percentage of recovery

File config: BuffPre -i <path> -o <path>
    -i <path>       Input config file path
    -o <path>       Your output directory path (default current directory)
    --conf          Display confic file pattern

Library & Test:
    -l, --library   Display pKa library
    -t, --test      Test example confic file

History:
    --hist          Display all command and output (Showed dates)

Other:
    -h, --help      Show this help message and exit
    -v, --version   The lastest version of BuffPre
    
# Author's email:
    moo_sutthittha@hotmail.com (Moonipur)

# The lastest version:
    BuffPre v0.0.1    

** Please contact us if you have any questions or problems with the program.
