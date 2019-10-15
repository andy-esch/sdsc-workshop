# Material for the workshop `Spatial Modeling Problems & Decision Tree`

## Clone Github repository with workshop material

Download Git Large File System: https://git-lfs.github.com/

and clone repository

`git clone git@github.com:CartoDB/tech-workshops.git`

## Download and install docker

Follow instructions here: https://docs.docker.com/install/

## Run image

Open your terminal and run

```
$ docker run --user root -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -e GRANT_SUDO=yes -v "$PWD":/home/jovyan/workspace jupyter/datascience-notebook
```

A local address will be created. Copy and paste the address in your browser, this will launch Jupyter.

**Note**: If you have another Jupyter server running, make sure it's on a different port than 8888. Otherwise change the port number above or close down the other notebook server.

## Install libraries and packages

Click New -> Terminal and go to the directory where you cloned the Github repository and run this script to install the required libraries

`$ bash notebooks_start.sh`

Note: the installation can take a while (10-15 min)

## Go to the `chapters` folder and have fun :)
