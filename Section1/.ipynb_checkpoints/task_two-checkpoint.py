import numpy as np
import geopandas as gp
from geopandas.tools import sjoin, overlay  
from osgeo import gdal, gdalnumeric, ogr, osr 

#reading the shp file 
shapefile_path = '/Users/tejaspatil/Desktop/Programming_Club_PM_App/Section1/India-State-and-Country-Shapefile-Updated-Jan-2020/India_Country_Boundary.shp'
df = gp.read_file(shapefile_path)

#data analysis using osgeo 
#snipet to find teh number of layer 
shapefile = ogr.Open(shapefile_path)
layer = shapefile.GetLayer()
print(f'Number of features: {layer.GetFeatureCount()}')

#printing the fields give in the .shp file
layer_defn = layer.GetLayerDefn()
print("Fields:")
for i in range(layer_defn.GetFieldCount()):
    field_defn = layer_defn.GetFieldDefn(i)
    print(f"{field_defn.GetName()} ({field_defn.GetTypeName()})")

#printing out some specific number of area for data analysis, this can be done by iterating for different i for analysing some specific area
for i, feature in enumerate(layer):
    if i < 20:
        print(feature.items())