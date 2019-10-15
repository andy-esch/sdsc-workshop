import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import shapely
from libpysal.weights import Queen
import pointpats
import pointpats.centrography

from cartoframes.auth import set_default_credentials
from cartoframes.data import Dataset

set_default_credentials('eschbacher')

## The Meuse dataset from R gstat package
class GetMeuse():
    def __init__(self):
        self.data = gpd.GeoDataFrame(Dataset('meuse').download(decode_geom=True))
        self.data['log_zinc'] = np.log(self.data['zinc'])

        self.data.crs = {'init': 'epsg:4326'}
        self.data = self.data.to_crs({'init': 'epsg:28992'})
        self.data_lonlat = self.data.to_crs({'init': 'epsg:4326'})

        self.data_grid = gpd.GeoDataFrame(Dataset('meuse_grid').download(decode_geom=True))
        self.data_grid.crs = {'init': 'epsg:4326'}
        self.data_grid = self.data_grid.to_crs({'init': 'epsg:28992'})
        self.data_grid_lonlat = self.data_grid.to_crs({'init': 'epsg:4326'})

    def loadpred_krg(self):

        self.data_krg = gpd.GeoDataFrame(Dataset('meuse_krg').download(decode_geom=True))
        self.data_krg.crs = {'init': 'epsg:4326'}
        self.data_krg = self.data_krg.to_crs({'init': 'epsg:28992'})
        self.data_krg_lonlat = self.data_krg.to_crs({'init': 'epsg:4326'})

        self.data_grid_krg = gpd.GeoDataFrame(Dataset('meuse_grid_krg').download(decode_geom=True))
        self.data_grid_krg.crs = {'init': 'epsg:4326'}
        self.data_grid_krg_lonlat = self.data_grid_krg.to_crs({'init': 'epsg:4326'})

    def loadpred_INLAspde(self):
        """"""
        self.data_INLAspde = gpd.GeoDataFrame(Dataset('meuse_inlaspde').download(decode_geom=True))
        self.data_INLAspde.crs = {'init': 'epsg:4326'}
        self.data_INLAspde = self.data_INLAspde.to_crs({'init': 'epsg:28992'})
        self.data_INLAspde_lonlat = self.data_INLAspde.to_crs({'init': 'epsg:4326'})

        self.data_grid_INLAspde = gpd.GeoDataFrame(Dataset('meuse_grid_inlaspde').download(decode_geom=True))
        self.data_grid_INLAspde.crs = {'init': 'epsg:4326'}
        self.data_grid_INLAspde = self.data_grid_INLAspde.to_crs({'init': 'epsg:28992'})
        self.data_grid_INLAspde_lonlat = self.data_grid_INLAspde.to_crs({'init': 'epsg:4326'})

## The Boston dataset from R spData package
class GetBostonHousing():
    def __init__(self):
        self.data = gpd.GeoDataFrame(Dataset('boston_housing').download(decode_geom=True))# gpd.read_file(self.filename)
        self.data.crs = {'init': 'epsg:4326'}
        self.w = Queen.from_dataframe(self.data)

    def loadpred_MRF_INLA(self):
        self.data_MRF_INLA = gpd.GeoDataFrame(Dataset('boston_housing_mrf_inla').download(decode_geom=True))
        self.data_MRF_INLA.crs = {'init': 'epsg:4326'}

## The Crime dataset from UK Police data
class GetCrimeLondon():
    def __init__(self, var, var_value):
        self.filename = './data/UK_Police_street_crimes_2019_04.csv'
        self.data = gpd.GeoDataFrame(Dataset('uk_police_street_crimes_2019_04').download(decode_geom=True))
        self.data.crs = {'init': 'epsg:4326'}
        self.data = self.data[self.data[var] == var_value]
        self.data_lonlat = self.data
        self.data_lonlat = Dataset('''
            SELECT c.*
              FROM uk_police_street_crimes_2019_04 as c
              JOIN london_borough_excluding_mhw as g
              ON ST_Intersects(c.the_geom, g.the_geom)
        
        ''').download(decode_geom=True)
        self.data_lonlat = gpd.GeoDataFrame(self.data_lonlat)

        self.data = self.data.to_crs({'init': 'epsg:32630'})

    def pp(self):
        self.pointpattern = pointpats.PointPattern(
            pd.concat([self.data.geometry.x,self.data.geometry.y], axis=1)
        )
        self.pp_lonlat = pointpats.PointPattern(
            pd.concat([self.data_lonlat.geometry.x,self.data_lonlat.geometry.y], axis=1)
        )