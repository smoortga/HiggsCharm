# Summary
This subdirectory aims to convert LHE files into miniAOD or nanoAOD format. Configurations are inspired by the 2017UL production.

### Step 1: Setup the CMSSW environment
Run the [setupProd.sh](setupProd.sh) script, providing the following three arguments:
  * scram architecture (make sure it is available on your system. These instructions assume running on SL7)
  * CMSSW version (make sure it can be built on the given scram architecture)
  * tag: a name to produce a working directory

For example:

```
source setupProd.sh slc7_amd64_gcc700 CMSSW_10_6_19 HcToFourMuons
``` 

### Step 2: Run GEN-SIM-DIGI-RAW-HLT steps
The first step is to run GEN, SIM, DIGI, RAW, and HLT. This is already included in the configuration file [test_GEN-SIM-DIGI-RAW_cfg.py](test_GEN-SIM-DIGI-RAW_cfg.py).
A submission script has been prepared to run in parallel on several .lhe files via condor. This script can be found under [submit_GEN-SIM-DIGI-RAW.py](submit_GEN-SIM-DIGI-RAW.py).

It can be ran providing the following arguments:
  * config: the configuration file to run (will be [test_GEN-SIM-DIGI-RAW_cfg.py](test_GEN-SIM-DIGI-RAW_cfg.py) for this step)
  * indir: path to input directory that contains input LesHouches (.lhe) files
  * outdir: path to output directory in which the .root files will be stored (note that the tag specified later will be appended to this directory name!)
  * jobflavour: Limit to the duration of the job on condor, as specified [here](https://batchdocs.web.cern.ch/local/submit.html)
  * tag: A tag to specify the name of the working directory and output directory

for example:

```
python submit_GEN-SIM-DIGI-RAW.py \
--config=./test_GEN-SIM-DIGI-RAW_cfg.py \
--indir=/pnfs/iihe/cms/store/user/nbreugel/HiggsCharm/HcToFourMuons/ \
--outdir=/pnfs/iihe/cms/store/user/nbreugel/HiggsCharm/GENSIMDIGI/ \
--jobflavour=tomorrow \
--tag=HcToFourMuons
```

### Step 3: Run RECO, AOD, MINIAOD steps
Then one has to run the RECO, AOD and miniAOD steps. This is already included in the configuration file [test_MINIAOD_cfg.py](test_MINIAOD_cfg.py).
A submission script has been prepared to run in parallel on several .lhe files via condor. This script can be found under [submit_RECO-AOD-MINIAOD.py](submit_RECO-AOD-MINIAOD.py).

It can be ran providing the following arguments:
  * config: the configuration file to run (will be [test_MINIAOD_cfg.py](test_MINIAOD_cfg.py) for this step)
  * indir: path to input directory that contains input DIGI-RAW (.root) files
  * outdir: path to output directory in which the .root files will be stored (note that the tag specified later will be appended to this directory name!)
  * jobflavour: Limit to the duration of the job on condor, as specified [here](https://batchdocs.web.cern.ch/local/submit.html)
  * tag: A tag to specify the name of the working directory and output directory

for example:

```
python submit_RECO-AOD-MINIAOD.py \
--config=./test_MINIAOD_cfg.py \
--indir=/pnfs/iihe/cms/store/user/nbreugel/HiggsCharm/GENSIMDIGI_HcToFourMuons/ \
--outdir=/pnfs/iihe/cms/store/user/nbreugel/HiggsCharm/RECOAODMINIAOD \
--jobflavour=tomorrow \
--tag=HcToFourMuons
```

### Step 3: Run NANOAOD step
Finally one has to run the NANOAOD step. This is already included in the configuration file [test_NANOAOD_cfg.py](test_NANOAOD_cfg.py).
A submission script has been prepared to run in parallel on several .lhe files via condor. This script can be found under [submit_NANOAOD.py](submit_NANOAOD.py).

It can be ran providing the following arguments:
  * config: the configuration file to run (will be [test_NANOAOD_cfg.py](test_NANOAOD_cfg.py) for this step)
  * indir: path to input directory that contains input DIGI-RAW (.root) files
  * outdir: path to output directory in which the .root files will be stored (note that the tag specified later will be appended to this directory name!)
  * jobflavour: Limit to the duration of the job on condor, as specified [here](https://batchdocs.web.cern.ch/local/submit.html)
  * tag: A tag to specify the name of the working directory and output directory

for example:

```
python submit_NANOAOD.py \
--config=./test_NANOAOD_cfg.py \
--indir=/pnfs/iihe/cms/store/user/nbreugel/HiggsCharm/RECOAODMINIAOD_HcToFourMuons/ \
--outdir=/pnfs/iihe/cms/store/user/nbreugel/HiggsCharm/NANOAOD \
--jobflavour=tomorrow \
--tag=HcToFourMuons

```

