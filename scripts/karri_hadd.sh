#!/bin/bash

usage()
{
    echo "Usage:"
    echo ""
    echo "   $ $0 ntuple_version tagname"
    echo ""
    echo ""
    exit
}

PREFIX=MC_
if [ -z $1 ]; then usage; fi
if [ -z $2 ]; then usage; fi
if [ -n "$3" ]; then PREFIX=BDTinputTree_MC_; fi

if [ ! -d outputs/$1/$2 ]; then
    echo ">>> Error! cannot find outputs/$1/$2"
    echo ">>> Check your ntuple_version and tagname that you've provided!"
    exit
fi

cd outputs/$1/$2

echo "" > .hadd.cmds.txt

if [[ $1 == *"WVZ2017_v0.1.12."* ]] || [[ $1 == *"WVZ2018_v0.1.12."* ]]; then
    echo "hadd -f sig.root ${PREFIX}www_amcatnlo_1_results.root ${PREFIX}wwz_amcatnlo_1_results.root ${PREFIX}wzz_amcatnlo_1_results.root ${PREFIX}zzz_amcatnlo_1_results.root ${PREFIX}wh_ww_amcatnlo_1_results.root ${PREFIX}wh_zz_amcatnlo_1_results.root ${PREFIX}zh_ww_4l_powheg_1_results.root ${PREFIX}zh_zz_amcatnlo_1_results.root ${PREFIX}wwz_4l2v_amcatnlo_1_results.root ${PREFIX}ggzh_4l_powheg_1_results.root" >> .hadd.cmds.txt
else
    echo "hadd -f sig.root ${PREFIX}www_amcatnlo_1_results.root ${PREFIX}wwz_amcatnlo_1_results.root ${PREFIX}wzz_amcatnlo_1_results.root ${PREFIX}zzz_amcatnlo_1_results.root ${PREFIX}wh_ww_amcatnlo_1_results.root ${PREFIX}wh_zz_amcatnlo_1_results.root ${PREFIX}zh_ww_4l_powheg_1_results.root ${PREFIX}zh_zz_amcatnlo_1_results.root ${PREFIX}ggzh_4l_powheg_1_results.root" >> .hadd.cmds.txt
fi
if [[ $1 == *"WVZ2017_v0.1.12."* ]] || [[ $1 == *"WVZ2018_v0.1.12."* ]]; then
   echo "hadd -f wwz.root ${PREFIX}wwz_amcatnlo_1_results.root ${PREFIX}zh_ww_4l_powheg_1_results.root ${PREFIX}wwz_4l2v_amcatnlo_1_results.root ${PREFIX}ggzh_4l_powheg_1_results.root" >> .hadd.cmds.txt
else
   echo "hadd -f wwz.root ${PREFIX}wwz_amcatnlo_1_results.root ${PREFIX}zh_ww_4l_powheg_1_results.root ${PREFIX}ggzh_4l_powheg_1_results.root" >> .hadd.cmds.txt
fi

echo "hadd -f ggzh_wwz.root ${PREFIX}ggzh_4l_powheg_1_results.root" >> .hadd.cmds.txt
echo "hadd -f zh_wwz.root ${PREFIX}zh_ww_4l_powheg_1_results.root" >> .hadd.cmds.txt
echo "hadd -f mad_zh_wwz.root ${PREFIX}zh_ww_amcatnlo_1_results.root" >> .hadd.cmds.txt
echo "hadd -f karri_mad_zh_wwz.root ${PREFIX}karri_zh_ww_amcatnlo_1_results.root" >> .hadd.cmds.txt

sh ../../../rooutil/xargs.sh .hadd.cmds.txt

cd - > /dev/null
