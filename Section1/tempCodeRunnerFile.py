shapefile = ogr.Open(shapefile_path)
layer = shapefile.GetLayer()
print(f'Number of features: {layer.GetFeatureCount()}')