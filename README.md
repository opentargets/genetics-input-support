# Open Targets: genetics-input-support overview

The aim of this application is to allow the reproducibility of OpenTarget Genetics data release pipeline.
The input files are copied in a local hard disk and eventually in a specific google storage bucket 

Currently, the application executes 3 steps and finally it generates the input resources for the ETL pipeline (https://github.com/opentargets/data_pipeline)

List of available steps:
- LookupTable
- Variant
- Disease


Within this application you can simply download a file from FTP, HTTP or Google Cloud Bucket but at the same time the file can be processed in order to generate a new resource.
The final files are located under the output directory while the files used for the computation are saved under stages. 

Below more details about how to execute the script.

# Installation Requirements

* Conda
* git
* Google Cloud SDK

## Conda for Linux/MAC

Download Conda3 for Mac here: <br>
 https://www.anaconda.com/products/individual <br>
[download Anaconda3-2021.05-MacOSX-x86_64.sh]

Download Conda3 for Linux x86_84 <br>
 https://www.anaconda.com/products/individual <br>
[download Anaconda3-2021.05-Linux-x86_64.sh]

Conda: installation commands
```
bash path_where_downloaded_the_file/Anaconda3-2020.07-Linux-x86_64.sh
source ~/.bashrc
conda update
```
Eg. for linux
```
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
bash Anaconda3-2020.07-Linux-x86_64.sh
source ~/.bashrc
```
## Conda in Docker (for PyCharm)

If you would rather run a containerised version of Conda use the provided Dockerfile. 

```
# build the image
docker build --tag gis-py3.8 <path to Dockerfile>
```
You can use the Docker image from within PyCharm by selecting 'Add Interpreter -> Docker -> <image>'

# Set up application (first time)
```
git clone https://github.com/opentargets/genetics-input-support
cd genetics-input-support
conda env create -f environment.yaml
conda activate gis-py3.8

python genetics-input-support.py -h
```

## Usage

```
conda activate gis-py3.8
cd your_path_application
python genetics-input-support.py  -h
usage: genetics-input-support.py [-h] [-c CONFIG]
                                 [-gkey GOOGLE_CREDENTIAL_KEY]
                                 [-gb GOOGLE_BUCKET] [-o OUTPUT_DIR] [-t]
                                 [-s SUFFIX] [-steps STEPS [STEPS ...]]
                                 [-exclude EXCLUDE [EXCLUDE ...]] [--skip]
                                 [-l] [--log-level LOG_LEVEL]
                                 [--log-config LOG_CONFIG]

...

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        path to config file (YAML) [env var: CONFIG] (default:
                        None)
  -gkey GOOGLE_CREDENTIAL_KEY, --google_credential_key GOOGLE_CREDENTIAL_KEY
                        The path were the JSON credential file is stored. [env
                        var: GOOGLE_APPLICATION_CREDENTIALS] (default: None)
  -gb GOOGLE_BUCKET, --google_bucket GOOGLE_BUCKET
                        Copy the files from the output directory to a specific
                        google bucket (default: None)
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        By default, the files are generated in the root
                        directory [env var: OT_OUTPUT_DIR] (default: None)
  -t, --thread          Run the script with thread [env var: OT_THREAD]
                        (default: False)
  -s SUFFIX, --suffix SUFFIX
                        The default suffix is yyyy-mm-dd [env var:
                        OT_SUFFIX_INPUT] (default: None)
  -steps STEPS [STEPS ...]
                        Run a specific list of sections of the config file. Eg
                        annotations annotations_from_buckets (default: None)
  -exclude EXCLUDE [EXCLUDE ...]
                        Exclude a specific list of sections of the config
                        file. Eg annotations annotations_from_buckets
                        (default: None)
  --log-level LOG_LEVEL
                        set the log level [env var: LOG_LEVEL] (default: INFO)

```

# Google bucket requirements
To copy the files in a specific google storage bucket valid credentials must be used.
The required parameter -gkey (--google_credential_key) allows the specification of Google storage JSON credential.
Eg.
```
python genetics-input-support.py -gkey /path/open-targets-gac.json -gb bucket/object_path
or
python genetics-input-support.py
       -steps  Variant
       -gkey /path/open-targets-genetics-dev-svn.json
       -gb genetics-portal-dev-data/22.02/input
```