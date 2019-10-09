#!/bin/bash

usage()
{
    echo "Usage:"
    echo ""
    echo "   $ $0 ntuple_version2016 tagname2016 ntuple_version2017 tagname2017 ntuple_version2018 tagname2018"
    echo ""
    echo ""
    exit
}

if [ -z $1 ]; then usage; fi
if [ -z $2 ]; then usage; fi
if [ -z $3 ]; then usage; fi
if [ -z $4 ]; then usage; fi
if [ -z $5 ]; then usage; fi
if [ -z $6 ]; then usage; fi

if [ ! -d outputs/$1/$2 ]; then
    echo ">>> Error! cannot find outputs/$1/$2"
    echo ">>> Check your ntuple_version and tagname that you've provided!"
    exit
fi

if [ ! -d outputs/$3/$4 ]; then
    echo ">>> Error! cannot find outputs/$3/$4"
    echo ">>> Check your ntuple_version and tagname that you've provided!"
    exit
fi

if [ ! -d outputs/$5/$6 ]; then
    echo ">>> Error! cannot find outputs/$5/$6"
    echo ">>> Check your ntuple_version and tagname that you've provided!"
    exit
fi

mkdir -p outputs/${1}_${3}_${5}/${2}_${4}_${6}

echo "" > .hadd.cmds.txt

if [[ $1 == *"WVZ"* ]] || [[ $1 == *"Trilep"* ]] || [[ $1 == *"TTZ"* ]]; then
    echo "hadd -f outputs/${1}_${3}_${5}/${2}_${4}_${6}/sig.root      outputs/${1}/${2}/sig.root      outputs/${3}/${4}/sig.root      outputs/${5}/${6}/sig.root" >> .hadd.cmds.txt
    echo "hadd -f outputs/${1}_${3}_${5}/${2}_${4}_${6}/zh_wwz.root   outputs/${1}/${2}/zh_wwz.root   outputs/${3}/${4}/zh_wwz.root   outputs/${5}/${6}/zh_wwz.root" >> .hadd.cmds.txt
    echo "hadd -f outputs/${1}_${3}_${5}/${2}_${4}_${6}/ggzh_wwz.root   outputs/${1}/${2}/ggzh_wwz.root   outputs/${3}/${4}/ggzh_wwz.root   outputs/${5}/${6}/ggzh_wwz.root" >> .hadd.cmds.txt
    echo "hadd -f outputs/${1}_${3}_${5}/${2}_${4}_${6}/mad_zh_wwz.root   outputs/${1}/${2}/mad_zh_wwz.root   outputs/${3}/${4}/mad_zh_wwz.root   outputs/${5}/${6}/mad_zh_wwz.root" >> .hadd.cmds.txt
fi

sh rooutil/xargs.sh .hadd.cmds.txt
