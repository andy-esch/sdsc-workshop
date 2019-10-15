pip install -r requirements.txt \
  && \
  sudo apt-get update && \
  conda install -y r-rgdal && \
  sudo apt-get install -y gdal-bin && \
  conda install -y r-spdep && \
  sudo apt install libspatialindex-dev