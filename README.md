# PeakBlockAI
This repo is one of the three components of the PeakBlock project, one of the submissions to the #CodeVsCovid19 hackathon
organized by Hack Zurich and ETH. 

The goal of this project is to contribute to the ongoing effort to combat the COVID19 pandemic by
preventing a second peak of infections after this first peak is contained.
It accomplishes this by providing a system to monitor the appearance and spread of COVID19-like symptoms after the end
of the quarantine and self-isolation period. 

This repo contains analytics engine of the project and is divided into three main modules: a webserver based on Sanic,
a patient diagnosis predictor based on naive Bayesian estimation and a geographic pandemic spread model based on SIR. 

## Build
To build this repo, simply clone it then run 

`pip install -r requirements.txt`

To run the webserver

`python run.py`

A custom configuration file can be written and loaded via

`python run.py path_to_custom_config`

where `path_to_custom_config` is the location of the custom config file in the root folder. Otherwise, the default config, which 
can be found in the Input_files folder, will be used.

The API endpoint addresses interfacing with the analytics routines can be found in `app\app_core.py`

## Docker
To build with Docker, clone the repo and run

`docker build -t my_service_image .`

`docker run -ti --ulimit core=0:0 --user runner --name my_service my_service_image`

By default, the webserver will listen on 0.0.0.0:5555