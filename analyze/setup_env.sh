#!/bin/bash

# source setup_env.sh slc7_amd64_gcc700 CMSSW_10_6_19 

if [ -n "$1" ]
  then
    scram_arch=${1}
  else
    scram_arch=slc7_amd64_gcc700
fi
echo "Using SCRAM architecture ${scram_arch}"

if [ -n "$2" ]
  then
    cmssw_version=${2}
  else
    cmssw_version=CMSSW_10_6_19
fi
echo "Running in ${cmssw_version}"



echo "creating grid proxy..."
voms-proxy-init --voms cms -valid 192:00

echo "setting up CMSSW environment..."
export SCRAM_ARCH=$scram_arch
cmsrel $cmssw_version
cd $cmssw_version/src
cmsenv
cd ../../





