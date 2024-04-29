# Import system modules
import arcpy
from arcpy.sa import *
from arcpy.ia import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/Users/sdion/Desktop/Geospatial Programming/Geospatial_Programming_Project.gdb"
# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

arcpy.env.overwriteOutput = True
print(arcpy.env.workspace)


# Import tif, shapefiles and csv files into the geodatabase
from arcpy import env
arcpy.conversion.RasterToGeodatabase("et0_v3_yr.tif;wc2.1_30s_bio_12.tif", 
                                     "Geospatial_Programming_Project.gdb", "")
arcpy.management.XYTableToPoint("Combined_Stations.csv", "Geospatial_Programming_Project.gdb/Weather_Stations", "Longtitude", "Latitude", "#", arcpy.SpatialReference("WGS 1984"))
arcpy.conversion.FeatureClassToFeatureClass("USA_Counties.shp",
                                           "Geospatial_Programming_Project.gdb",
                                           "USA_Counties")

# Input DEM raster file (TIFF format) & Set local variables
Annual_ET0 = "et0_v3_yr.tif"
Annual_Prec = "wc2.1_30s_bio_12.tif"
USA_Counties = "USA_Counties.shp"

# output data
counties_utm = "USA_Counties_utm.shp"

# create a spatial reference object for the output coordinate system
out_coordinate_system = arcpy.SpatialReference('NAD 1983 UTM Zone 15N')

# run the tool
arcpy.Project_management(USA_Counties, counties_utm, out_coordinate_system)

arcpy.Describe(Annual_ET0)

arcpy.Describe(Annual_Prec)

# Define the input raster and output raster paths
input_raster = Annual_ET0
output_raster = "Annual_ET0_utm"

# Remove invalid characters from the output raster name
output_raster = arcpy.ValidateTableName(output_raster)

# Define the spatial reference using a factory code
spatial_ref = arcpy.SpatialReference(26915)  # Factory code for NAD 1983 UTM Zone 15N

# Project the raster
arcpy.ProjectRaster_management(input_raster, output_raster, spatial_ref)

# Define the input raster and output raster paths
input_raster1 = Annual_Prec
output_raster1 = "Annual_Prec_utm"

# Remove invalid characters from the output raster name
output_raster = arcpy.ValidateTableName(output_raster)

# Define the spatial reference using a factory code
spatial_ref = arcpy.SpatialReference(26915)  # Factory code for NAD 1983 UTM Zone 15N

# Project the raster
arcpy.ProjectRaster_management(input_raster1, output_raster1, spatial_ref)

# Select Perry county in Missouri by using the FIPS code and the name of the county
sql = "FIPS = '29157'"
perry_lyr = arcpy.management.SelectLayerByAttribute(counties_utm, "NEW_SELECTION",sql)

# Write the selected features to a new feature class
arcpy.management.CopyFeatures(perry_lyr, 'perry')

# Set input and output raster paths
output_raster2 = "AnET0"

# Clip the raster
arcpy.management.Clip(output_raster, "#", output_raster2, "perry", "#", "ClippingGeometry")

# Set input and output raster paths
output_raster3 = "AnPrec"

# Clip the raster
arcpy.management.Clip(output_raster1, "#", output_raster3, "perry", "#", "ClippingGeometry")

# Set local variables
AnET0_Perry = output_raster2
AnPrec_Perry = output_raster3

# Execute Minus
outMinus = Minus(AnPrec_Perry,AnET0_Perry)

# Save the output 
outMinus.save("C:/Users/sdion/Desktop/Geospatial Programming/Geospatial_Programming_Project.gdb/Eff_Rain_Perry.tif")

arcpy.CoordinateTableToPolygon_defense("Boundary_Polygon.csv", 
                                       "Bound_Perry", "Longtitude", "DD_2", "Latitude")

import arcpy
from arcpy import env  
from arcpy.sa import *

outIDW = Idw("C:/Users/sdion/Desktop/Geospatial Programming/Geospatial_Programming_Project.gdb/Weather_Stations.csv", "Annual_Effective_Rainfall_mm_2023",1.60000000000082E-04, 1)
outIDW.save("C:/Users/sdion/Desktop/Geospatial Programming/Geospatial_Programming_Project.gdb/Idw_Project.tif")


