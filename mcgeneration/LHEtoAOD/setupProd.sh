#!/bin/bash

# source setupProd.sh slc7_amd64_gcc700 CMSSW_10_6_19 HcToFourMuons

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

if [ -n "$3" ]
  then
    tag=${3}
  else
    tag=$(date +'%m_%d_%Y_%Ih_%Mm_%Ss')
fi
echo "Using tag ${tag}"


echo "creating grid proxy..."
voms-proxy-init --voms cms -valid 192:00

echo "setting up CMSSW environment..."
export SCRAM_ARCH=$scram_arch
mkdir "prod_${tag}"
cd "prod_${tag}"
cmsrel $cmssw_version
cd $cmssw_version/src
cmsenv
git cms-addpkg Configuration/Generator
mkdir -p Configuration/GenProduction/python
cp ../../../HIG-RunIISummer19UL17wmLHEGEN-00275-fragment.py ./Configuration/GenProduction/python/
git cms-addpkg PhysicsTools/NanoAOD
cp ../../../GenWeightsTableProducer.cc ./PhysicsTools/NanoAOD/plugins/GenWeightsTableProducer.cc
scram b -j6

cp ../../../test_GEN-SIM-DIGI-RAW_cfg.py ./test_GEN-SIM-DIGI-RAW_cfg.py
cp ../../../test_MINIAOD_cfg.py ./test_MINIAOD_cfg.py
cp ../../../test_NANOAOD_cfg.py ./test_NANOAOD_cfg.py
cp ../../../submit_GEN-SIM-DIGI-RAW.py ./submit_GEN-SIM-DIGI-RAW.py
cp ../../../submit_RECO-AOD-MINIAOD.py ./submit_RECO-AOD-MINIAOD.py
cp ../../../submit_NANOAOD.py ./submit_NANOAOD.py

# echo "creating GEN-SIM-DIGI-HLT config..."
# cmsDriver.py Configuration/GenProduction/python/HIG-RunIISummer19UL17wmLHEGEN-00275-fragment.py \
# --filein file:test.lhe \
# --fileout file:test_GEN-SIM-DIGI-RAW.root \
# --mc \
# --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer19ULPrePremix-UL17_106X_mc2017_realistic_v6-v1/PREMIX" \
# --eventcontent PREMIXRAW \
# --datatier GEN-SIM-DIGI \
# --conditions 106X_mc2017_realistic_v6 \
# --beamspot Realistic25ns13TeVEarly2017Collision \
# --step GEN,SIM,DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2017 \
# --procModifiers premix_stage2 \
# --datamix PreMix \
# --era Run2_2017 \
# --runUnscheduled \
# --nThreads 1 \
# --geometry DB:Extended \
# --python_filename test_GEN-SIM-DIGI-RAW_cfg.py \
# -n 2 \
# --no_exec \
# --customise Configuration/DataProcessing/Utils.addMonitoring
# 
# 
# echo "creating RECO-AOD-MINIAOD config..."
# cmsDriver.py MINIAOD \
# --python_filename test_MINIAOD_cfg.py \
# --mc \
# --eventcontent MINIAODSIM \
# --runUnscheduled \
# --datatier MINIAODSIM \
# --conditions 106X_mc2017_realistic_v6 \
# --step RAW2DIGI,RECO,EI,PAT \
# --era Run2_2017 \
# --filein file:test_GEN-SIM-DIGI-RAW.root \
# --fileout file:test_MINIAOD.root \
# -n 2 \
# --no_exec

# echo "creating RECO-AOD-MINIAOD-NANOAOD config..."
# cmsDriver.py NANOAOD \
# --python_filename test_RECO-AOD-MINIAOD-NANOAOD_cfg.py \
# --mc \
# --eventcontent NANOAODSIM \
# --runUnscheduled \
# --datatier NANOAODSIM  \
# --conditions 106X_mc2017_realistic_v6 \
# --step RAW2DIGI,RECO,EI,PAT,NANO \
# --era Run2_2017,run2_nanoAOD_94XMiniAODv2 \
# --filein file:test_GEN-SIM-DIGI-RAW.root \
# --fileout file:test_NANOAOD.root \
# -n 2 \
# --no_exec





