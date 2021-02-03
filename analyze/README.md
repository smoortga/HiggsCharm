# Summary
This code is meant to analyze nanoAOD samples for the Higgs Charm studies

### Step 0: Setup CMSSW environment
If you use the code for the first time, run the [setup_env.sh](setup_env.sh) script with the desired SCRAM_ARCH and CMSSW version, for example:

```
source setup_env.sh slc7_amd64_gcc700 CMSSW_10_6_19 
```

Each time you log in again after that, you can go into this CMSSW environment and use `cmsenv`:

```
cd  CMSSW_10_6_19/src
cmsenv
cd ../../
```

### Step 1: Define the samples
Open the [samples.py](samples.py) script and adapt the directory in there to your needs. You can add new samples by defining a tag, a path, a cross section and whether or not it was privately produced (therefore including MadGraph weights to vary the Yukawa couplings). You do not need to define the `cmsenv` or `nevents` variables, they will be filled automatically. Samples can be found via [DAS](https://cmsweb.cern.ch/das/), and cross sections are gathered in the cross-section database ([XSDB](https://cms-gen-dev.cern.ch/xsdb)). The path to private samples can simply be a path to some accesible mass storage (pnfs), whereas centrally produced samples by CMS should be given the name that is entered in DAS (`/SAMPLE/SOFTWAREVERSION/NANOAODSIM`).

Once everything is defined, run this script (has to be repeated every time you change someting). It will dump a .pkl file that contains the dictionary with all the files that are associated to that sample. This .pkl file will serve as input to further steps.

```
python samples.py
```

### Step 2: Define you analysis selection
You can define you selections in [Analyze_nanoAOD.py](Analyze_nanoAOD.py). You can add variables to the `dict_variableName_Leaves`, and fill them in the loop. The content of the variables in the nanoAOD files can be found [via this link](https://cms-nanoaod-integration.web.cern.ch/integration/master-106X/mc106X_doc.html). You could do a small local test of this script using for example (change path names to your needs!):
```
python Analyze_nanoAOD.py \
--sampletag=HcTo4mu \
--outfile=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/Selection/selected_HcTo4mu_events_400_599.root \
--sampledict=/storage_mnt/storage/user/smoortga/HiggsCharm/analyze/sample_dict.pkl \
--firstEvt=550 \
--lastEvt=1399 \
--splitted=1 \
--private=1
```

### Step 3: Run large scale production via condorHT
You can launch a full large production of all samples (via the batch system, condorHT) using the [submit_analyze_nanoAOD.py](submit_analyze_nanoAOD.py) script. If you are satisfied with your event selection and ntuple content, run this for example doing:
```
python submit_analyze_nanoAOD.py \
--outdir=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/Selection/ \
--CMSSWdir=/user/smoortga/HiggsCharm/analyze/CMSSW_10_6_19/src/ \
--sampledict=/storage_mnt/storage/user/smoortga/HiggsCharm/analyze/sample_dict.pkl \
--tag=testing \
--nmaxevtsperjob=50000 \
--jobflavour=longlunch
```
This will create a `condor.submit` file that you can launch using `condor_submit`. The script will tell you where to find it.

### Step 4: Merge all files together
Once all jobs are done, you can merge all .root files of a given sample together using the [hadd_batch.py](hadd_batch.py) script. This will run several batch jobs (one for each sample) in which all splitted output .root files are merged into one for further analysis. You can run this for example via
```
python hadd_batch.py \
--indir=/pnfs/iihe/cms/store/user/smoortga/HiggsCharm/Selection/ \
--CMSSWdir=/user/smoortga/HiggsCharm/analyze/CMSSW_10_6_19/src/ \
--jobflavour=longlunch \
--tag=testing
```
followed by an appropriate `condor_submit`.

### Step 5: Plotting
You can plot variations of the charm yukawa using the [plotting/PlotKappaCharmVariations.py](plotting/PlotKappaCharmVariations.py) script. Or you can add your own plotting scripts in this directory.

